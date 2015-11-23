from bs4 import BeautifulSoup
import urllib2, sys
import json


site = 'http://home.woot.com/?ref=w_gh_hm_3'

page = urllib2.urlopen(site, 'link')
soup = BeautifulSoup(page, 'lxml')
print soup
print(20 * "#")
for item in soup.findAll(page)[1:]:
    print('\n',item)

print(20 * "#")
"""
site= "http://en.wikipedia.org/wiki/StackOverflow"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
print soup
"""
print(20 * "#")

req2 = urllib2.urlopen('http://www.nationaljournal.com/politics?rss=1').read()

xml = BeautifulSoup(req2, 'xml')

for item in xml.findAll('a')[3:1]:
    url = item.text
    news = urllib2.urlopen(url).read()
    print(news)

print(20 * "#")
for p in xml.findAll('p'):
    print(p.text)
