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
    writeToFile(res,'Hotels')
    return len(hotelUrl)


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

def get_hotel_address(element, res):
    info = element.find("div",attrs={"class":"header_contact_info"})
    if info==None:
        res['address']=None
        return
    address = ""
    for part in info.find_all("span",attrs={"class":"format_address"}):
        address += part.text
    res['address'] = address.strip()

def get_description(element, res):
    descp = element.find("div",attrs={"id":"BODYCON"})
    print descp.find("div",attrs={"class":"tabs_description_content"})
    input()
    print descp.find("div",atrrs={"class":"hr_tabs content_block hr_tabs_block"})
    
    # res['description']=descp.find("div",attrs={"class":"tabs_descriptive_text"}).text

def parseHotel(url):
    html = url_open(url)
    soup = BeautifulSoup(html,"html5lib")
    dump_url(url)
    res = {}
    get_title(soup,res)
    get_hotel_address(soup,res)
    # get_description(soup,res)
    return res
    


def parseRestaurantList(url):
    html = url_open(url)
    soup = BeautifulSoup(html, "html5lib")
    dump_url(url)
    titlelist = soup.find_all('div',attrs={"class":"listing"})
    # print titlelist[0]
    restaurantList = []
    for r in titlelist:
        if r.find('a',attrs={"class":"property_title"}):
            t = r.find('a')['href']
            restaurantList.append(root+t)
    # print restaurantList
    # print len(restaurantList)
    # input()
    res = []    
    for rest in restaurantList:
        res.append(parseRestaurant(rest))
    writeToFile(res,'Restaurant')
    return len(titlelist)

def get_restaurant_address(element,res):
    address = ""
    address = element.find("address").find("span").text
    res['address'] = address.strip()



def parseRestaurant(url):
    html = url_open(url)
    soup = BeautifulSoup(html, "html5lib")
    dump_url(url)
    res = {}
    get_title(soup,res)
    get_restaurant_address(soup,res)
    return res


def parseAttractionList(url):
    html = url_open(url)
    soup = BeautifulSoup(html, "html5lib")
    dump_url(url)
    titlelist = soup.find_all('div',attrs={"class":"property_title"})
    attractionList = []
    for title in titlelist:
        attractionList.append(root+title.find("a")['href'])
    # print attractionList
    # print len(attractionList)
    res = []
    for attraction in attractionList:
        res.append(parseAttraction(attraction))
    writeToFile(res,"Attractions")
    return len(titlelist)

def parseAttraction(url):
    html = url_open(url)
    soup = BeautifulSoup(html, "html5lib")
    dump_url(url)
    res = {}
    get_title(soup,res)
    get_attraction_address(soup,res)
    return res

def get_attraction_address(element,res):
    ad = element.find('address')
    if ad == None:
    	res['address'] = "Unknown"
    	return
    else:
    	ad = ad.text
    action_re = re.compile(r"Address:(.*)")
    m = action_re.search(ad)
    res['address']=m.group(1).strip()

def writeToFile(res,catagory):
    filename = catagory+"_out.json"
    f = open(filename, "w")
    for item in res:
       f.write(str(item)+'\n')
    f.close()

root="http://www.tripadvisor.com"
if __name__ == "__main__":
    # parseHotel("http://www.tripadvisor.com/Hotel_Review-g53449-d1563869-Reviews-Fairmont_Pittsburgh-Pittsburgh_Pennsylvania")

    
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
            if aspect != 'ShowForum' and aspect != 'Travel_Guide' and aspect != 'Flights':
                urlqueue.append(root+t)
    # print urlqueue

        # suffix = activity.find("a")['href']
        # page = root + suffix
        # soup = dump_url(page)
        # parse_page(soup)

    # while True:
    # 	if parseHotelList(urlqueue[0])!=0:
    # 		break
    # 	print 'try again'
    # # print urlqueue[2]
    while True:
    	if parseAttractionList(urlqueue[2])!=0:
    		break
        print 'try again'
    # while True:
    # 	if parseRestaurantList(urlqueue[3]):
    # 		break
    # 	print 'try again'
