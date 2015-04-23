# coding: utf-8

# Copyright (c) 2015, TravelGene.
from scrapy_redis.spiders import RedisMixin

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from example.items import ExampleLoader
from bs4 import BeautifulSoup
import re
import json
import sys
import time
import random
import urllib2


class MyCrawler(RedisMixin, CrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'
    
    rules = (
        # follow all links
        Rule(SgmlLinkExtractor(), callback='parse_page', follow=True),
    )
    def set_crawler(self, crawler):
        CrawlSpider.set_crawler(self, crawler)
        RedisMixin.setup_redis(self)

def parse_page(self, response):
    el = ExampleLoader(response=response)
    el.add_xpath('name', '//title[1]/text()')
    el.add_value('url', response.url)
    return el.load_item()



def url_open(pageUrl):
    headers = {  'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  , 'Referer':'https://itunes.apple.com'} 
    req = urllib2.Request(  url = pageUrl,   headers = headers  ) 
    try:
        response = urllib2.urlopen(req)
        contents= response.read()
    except urllib2.Exception, error:
        print error, contents

    return contents

def dump_url(url):
    # print "xxxxx", url
    content = url_open(url)
    fname = "html/" + url.split("/")[-1]
    f = open(fname, "w+")
    f.write(content)
    f.close()
    return BeautifulSoup(content)


def get_title(element, res):
    title = element.find("h1")
    res["title"] = unicode(title.text).strip()

def parseHotelList(url):
    dump_url(url)
    visited_url={}
    html = url_open(url)
    soup = BeautifulSoup(html, "html5lib")
    re_action = re.compile(r"(.*)-(.*)-(.*).*")
    page_no = get_last_page_no(soup)
    # print page_no
    m = re_action.search(url)
    hotelUrl = []
    for i in xrange(0,page_no):
        nurl = m.group(1)+'-'+m.group(2)+'-'+'oa'+(str)(i*30)+'-'+m.group(3)
        if nurl in visited_url.keys(): 
            continue
        visited_url[nurl]=1
        html = url_open(nurl)
        soup = BeautifulSoup(html, "html5lib")
        dump_url(nurl)
        print "xxxxx", url
        titlelist = soup.find_all('div',attrs={"class":"listing_title"})
        for title in titlelist:
            if title.find('a'):
                t = title.find('a')['href']
                hotelUrl.append(root+t)
    # input()
    # print hotelUrl
    # print len(hotelUrl)
    res = []
    for hotel in hotelUrl:
        res.append(parseHotel(hotel))
    writeToFile(res,'Hotels')
    return len(hotelUrl)


def parseHotel(url):
    html = url_open(url)
    soup = BeautifulSoup(html,"html5lib")
    #soup = dump_url(url)
    dump_url(url)
    res = {}
    get_title(soup,res)
    get_hotel_address(soup,res)
    # print "start crawling description..."
    # print url
    # get_description(soup,res)
    get_reviews(soup, res)
    get_ratings(soup, res)
    get_hotel_img(soup, res)

    get_location(soup)
    get_img_url(soup)
    get_open_hour(soup)
    return res


