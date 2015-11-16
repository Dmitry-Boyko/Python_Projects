for url in ["http://www.yahoo.com"]:
            try:
                connection = urllib2.urlopen(<'url'>)
                print connection.getcode()
                connection.close()
                print'"More Information" URL lInk found'
            except urllib2.HTTPError, e:
                print'# 404 [from the except block]'
                print e.getcode()
 
                # Prints:
                # 200 [from the try block]
                # 404 [from the except block
