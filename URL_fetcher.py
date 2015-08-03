import urllib2
response = urllib2.urlopen("http://www.cinemark.com/home.aspx")
# html = response.read()
# print html
for line in response.readlines():
    print line
print "Done!"
response.close()
