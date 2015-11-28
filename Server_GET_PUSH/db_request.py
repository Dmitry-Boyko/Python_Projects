from bs4 import BeautifulSoup
import time
import urllib.request

from dbconnect import connection

req = urllib.request.urlopen('http:/www.nation...')

xml = BeautifulSoup(req, 'xml')

c, conn = connection()

for item in xml.findAll('link')[3:]:
    url = item.text
    c.execute('INSERT ITO links (time, link) VALUES (%s, %s)',
              (time.time(), link))
    conn.commit()

conn.close()