#!/usr/bin/env python
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
    


def get_item_list(element):
    return element.find_all("div", class_ = re.compile("^listing.*"), id = re.compile("^attraction_.*"))

def get_title(element, res):
    title = element.find("a", class_ = "property_title")
    res["title"] = unicode(title.string).strip()

def get_target_url(element, res):
    title = element.find("a", class_ = "property_title")
    res["target_url"] = unicode("http://www.tripadvisor.com").strip()+unicode(title.get("href")).strip()


def get_photo_url(element, res):
    photo = element.find("img", class_ = "photo_image")
    if photo:
        res["photo_url"] = unicode(photo.get("src")).strip()


def get_rank(element, res):
    rank_res = {}
    rank = element.find("div", class_ = "popRanking")

    if rank == None:
        return

    pos_re = re.compile(r"Ranked #([0-9]+)")
    m = pos_re.search(unicode(rank.b.string))
    if m:
        rank_res["pos"] = int(m.group(1))

    #total_re = re.compile(r"of ([0-9]+) attractions")
    total_re = re.compile(r"of ([0-9]+) .* in .*")
    m = total_re.search(unicode(rank.b.next_sibling.string))
    if m:
        rank_res["total"] = int(m.group(1))

    res["rank"] = rank_res

def get_rating(element, res):
    rate_res = {}
    rate = element.find("img", class_ = "sprite-ratings")
    if rate == None:
        return

    rate_re = re.compile("of (\d+) stars")
    m = rate_re.search(rate["alt"])
    if m:
        rate_res["max"] = m.group(1)

    rate_res["score"] = rate["content"]
    res["rate"] = rate_res

def get_review_count(element, res):
    """
    :type element: bs4.element.Tag
    """
    review= element.find("a", onclick = re.compile(".*ReviewCount.*"))
    review_re=re.compile("(\d+) reviews")

    if review == None:
        return

    m = review_re.search(review.text)
    if m:
        review_count = unicode(m.group(1))
        res["reviewCount"] = review_count

def get_reviews(element, res):
    reviews = []
    review_list = element.find_all("li", id = re.compile("^review_"), class_ = "review_stubs_item")

    if review_list == None or len(review_list) == 0:
        return

    for r in review_list:
        reviews.append(unicode(r.a.string))

    res["reviews"] = reviews

def get_tag(element, res):
    tag = element.find("div", class_ = "attraction-type")
    if tag:
        tag = unicode(tag.span.next_sibling.string).strip().strip('"').strip()
        res["tag"] += tag.split(";")


def get_description(element, res):
    """
    :type element: bs4.element.Tag
    """
    desp = element.find("b", text=re.compile("description") )
    if desp:
        desp_res =  unicode(desp.next_sibling.string.strip())
        res["description"] = desp_res 
        return

    desp = element.find("p", class_=re.compile("description") )
    if desp:
        desp_res =  unicode(desp.text.strip('"').strip())
        res["description"] = desp_res 
        return

    desp = element.find("div", class_=re.compile("description") )
    if desp:
        desp_res =  unicode(desp.text.strip('"').strip())
        res["description"] = desp_res 
        return

    desp = element.find(class_=re.compile("description") )
    if desp:
        desp_res =  unicode(desp.text.strip('"').strip())
        res["description"] = desp_res 
        return

def get_last_page_no(soup):
    page_no = -1
    for page in soup.find_all("a",attrs ={"class":"paging taLnk "} ) :
        p = unicode (page.string.strip())
        if p != None and int(p) > page_no:
            page_no = int(p)
    return page_no


def get_content(element, page_tag):
    res = {}
    res["tag"] = list(page_tag)
    get_title(element, res)
    print "xxxxx", res["title"]
    get_photo_url(element, res)
    get_rank(element, res)
    get_rating(element, res)
    get_review_count(element, res)
    get_reviews(element, res)
    get_tag(element, res)
    get_description(element, res)
    get_target_url(element, res)
    return res

def get_cat_url(cat, action_re ):
    #print "\ncat:", cat["onclick"]
    m = action_re.search(cat["onclick"])
    cur = {}
    if m:
        cur["cat"] = m.group(1)
        cur["subcat"] = m.group(2)
        cur["urlid"] = m.group(3)
        cur["cid"] = m.group(4)
        if cur["subcat"].lower() != "all":
            #cur["url_pattern"] = "%s/%s-g%s-%s-c%s%%s-%s.html"  %("http://www.tripadvisor.com",unicode(cur["cat"]), unicode(cur["urlid"]), unicode("activities") , unicode(cur["cid"]), unicode("seattle_washington") )
            cur["url_pattern"] = "%s/%s-g%s-%s-c%s%%s-%s.html" %("http://www.tripadvisor.com",unicode(cur["cat"]), unicode(cur["urlid"]), unicode("activities") , unicode(cur["cid"].strip()), unicode("bellevue_washington") )
    

    return cur
    

def get_all_categories(soup):
    res = []
    action_re = re.compile(r'ta.trackEventOnPage\("(.*)","(.*)",".*"\).*ta.servlet.Attractions.*\((.*),(.*)\)')
    cats=[]
    for cat in soup.find_all("h2", attrs={"class":"header_tab sprite-tab-idle"} ) :
        res.append(get_cat_url(cat,action_re  ))
    action_re = re.compile(r"ta.trackEventOnPage\('(.*)','(.*)','.*'\).*ta.servlet.Attractions.viewCategoryButtonClicked\((.*),(.*)\)")
    for cat in soup.find_all("td", class_ = "sprite-filter-attraction"):
        res.append(get_cat_url(cat, action_re ))

    return res

def parse_page(soup, category):
    items = get_item_list(soup)
    page_tag = [category["cat"], category["subcat"]]

    for t in items:
        print json.dumps(get_content(t, page_tag), separators=(',',':'), sort_keys=True)

def dump_url(url):
    print "xxxxx", url
    content = url_open(url)
    fname = "html/" + url.split("/")[-1]
    f = open(fname, "w")
    f.write(content)
    f.close()
    return BeautifulSoup(content)



if __name__ == "__main__":
    #root_url = "http://www.tripadvisor.com/Attractions-g60878-Activities-Seattle_Washington.html"
    #root_url = "http://www.tripadvisor.com/Attractions-g58349-Activities-Bellevue_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58702-Activities-Redmond_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58541-Activities-Kirkland_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58605-Activities-Mercer_Island_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58528-Activities-Issaquah_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58578-Activities-Lynnwood_Washington.html"
    root_url="http://www.tripadvisor.com/Attractions-g58704-Activities-Renton_Washington.html"
    # root_url="http://www.yelp.com/c/pittsburgh/restaurants"
    visited_url={}
    visited_url[root_url]=1

    root_html = url_open(root_url)
    root_soup = BeautifulSoup(root_html)
    print "xxxx %s begin ..." %root_url

    #root_soup = BeautifulSoup(open("Bellevue.html"))
    #root_soup = BeautifulSoup(open("Redmond.html"))

    cats = get_all_categories(root_soup)
    '''print json.dumps(cats, separators=(',',':'), sort_keys=True)'''

    if len(cats)==0:
        cur={}
        cur["cat"] = "none" 
        cur["subcat"] = "none"
        cur["url_pattern"] = root_url.strip() 
        cats.append(cur)
        # print cats
        
    for cat in cats:
        #print  cat["url_pattern"]
        if cat["cat"] == "none": 
            url = cat["url_pattern"]
        else:
            url = cat["url_pattern"]%("")
        print "aaa",url
        soup = dump_url(url)
        pageno = get_last_page_no(soup)
        parse_page(soup, cat)
        if pageno > 1:
            for i in xrange(1, pageno):
                url = cat["url_pattern"]%("-oa"+str(30*i))
                if url in visited_url.keys(): continue
                visited_url[url]=1
                soup = dump_url(url)
                parse_page(soup, cat)
                sys.stdout.flush()
