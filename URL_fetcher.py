# V1

import urllib2
response = urllib2.urlopen("http://www.cinemark.com/home.aspx")
# html = response.read()
# print html
for line in response.readlines():
    print line
print "Done!"
response.close()

# V2

import csv
import urllib2

downloaded_data  = urllib2.urlopen("http://www.cinemark.com/home.aspx")
csv_data = csv.reader(downloaded_data)

for row in csv_data:
    print row

downloaded_data.close()
