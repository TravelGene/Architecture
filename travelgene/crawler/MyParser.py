#hotel crawler
from bs4 import BeautifulSoup
import re
import json
import sys
import time
import random
import urllib2


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
    print "xxxxx", url
    content = url_open(url)
    fname = "html/" + url.split("/")[-1]
    f = open(fname, "w+")
    f.write(content)
    f.close()
    return BeautifulSoup(content)

def parseHotelList(root_url):
    root_html = url_open(root_url)
    root_soup = BeautifulSoup(root_html,'html5lib')
    soup = dump_url(root_url)
    # print root_soup
    titlelist = root_soup.find_all('div',attrs={"class":"listing_title"})
    # input()
    hotelUrl = []
    for title in titlelist:
        if title.find('a'):
            t = title.find('a')['href']
            hotelUrl.append(root+t)
    # print hotelUrl
    # print len(hotelUrl)
    res = []
    for hotel in hotelUrl:
        res.append(parseHotel(hotel))
    writeToFile(res)

def parseHotel(url):
    html = url_open(url)
    soup = BeautifulSoup(html,"html5lib")
    #soup = dump_url(url)
    dump_url(url)
    res = {}
    get_title(soup,res)
    get_address(soup,res)
    print "start crawling description..."
    print url
    # get_description(soup,res)
    get_reviews(soup, res)
    get_ratings(soup, res)

    return res

# def get_content(element, page_tag):
#     res = {}
#     res["tag"] = list(page_tag)
#     get_title(element, res)
#     print "xxxxx", res["title"]
#     get_photo_url(element, res)
#     get_rank(element, res)
#     get_rating(element, res)
#     get_review_count(element, res)
#     get_reviews(element, res)
#     get_tag(element, res)
#     get_description(element, res)
#     get_target_url(element, res)
#     return res

def get_title(element, res):
    title = element.find("h1")
    res["title"] = unicode(title.text).strip()

def get_address(element, res):
    info = element.find("div",attrs={"class":"header_contact_info"})
    if info==None:
        res['address']=None
        return
    address = ""
    for part in info.find_all("span",attrs={"class":"format_address"}):
        address += part.text
    res['address'] = address

def get_description(element, res):
    descp = element.find("div",attrs={"id":"BODYCON"}).find("div",attrs={"class":"answers_in_head"})
    print descp
    print "@@@@@@@@@@@@@1"

    # ret=descp.

    print ret

    # print descp.find("div",atrrs={"class":"hr_tabs content_block hr_tabs_block"})

    # res['description']=descp.find("div",attrs={"class":"tabs_descriptive_text"}).text


def get_reviews(element, res):
    reviewlist=[]
    review=element.find("div",attrs={"id":"REVIEWS"})
    reviews=review.find_all("div",attrs={"class":"reviewSelector"})
    if reviews != None:
        for r in reviews:
            ret = r.find("p",attrs={"class":"partial_entry"})
            if ret != None:
                d = unicode(ret.text).strip()
                reviewlist.append(d)
        res['review_list']=reviewlist
        # print reviewlist

def get_ratings(element, res):
    rating_div=element.find("div",attrs={"class":"rs rating"})
    cnt=rating_div.find("span",attrs={"property":"v:count"})
    rate=rating_div.find("img")
    res['review_count']=cnt.text
    res['rating_string']=rate["content"]
    

def writeToFile(res):
    f = open("out.json", "w")
    for item in res:
    	   f.write(str(item)+'\n')
    f.close()

root="http://www.tripadvisor.com"
if __name__ == "__main__":
    # url_="/Users/zhiyuel/Desktop/html"+"Hotel_Review-g53449-d74348-Reviews-Quality_Inn_University_Center-Pittsburgh_Pennsylvania.html"
    # parseHotel(url_)

    #
    root_url="http://www.tripadvisor.com/Tourism-g53449-Pittsburgh_Pennsylvania-Vacations.html"
    visited_url={}
    visited_url[root_url]=1
    urlqueue=[]
    root_html = url_open(root_url)
    root_soup = BeautifulSoup(root_html)
    soup = dump_url(root_url)
    navLinks = soup.find('div',attrs={"class":"navLinks"})
    # print navLinks
    for cat in navLinks.find_all('li'):
        if cat.find('a'):
            t = cat.find('a')['href']
            action_re = re.compile(r"/(.*)-g(\d*)-([a-zA-Z0-9-_]*).html")
            m = action_re.search(t)
            aspect = m.group(1)
            if aspect != 'ShowForum' and aspect != 'Travel_Guide':
                urlqueue.append(root+t)
    print urlqueue
        # suffix = activity.find("a")['href']
        # page = root + suffix
        # soup = dump_url(page)
        # parse_page(soup)
    parseHotelList(urlqueue[0])