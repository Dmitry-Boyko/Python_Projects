'''
Sources:
    find_element_by*
    in operator
    comparison '!='
    assertion
'''
driver = webdriver.Firefox()

mytext = driver.find_element_by_id(“myID”).text
if “Selenium WebDriver” in mytext
    print “I found my text!”
else:
    .........
    
# or some more simple
if element.text != u'SomeText':
    print "Verify Failed: element text is not %r" % element.text

# or ...
assertTrue(findElement(By.id("myID")).getText().equals("foo")

Obviously object indentifier can to be changed like: (CSS, XPATH, tagName, ... etc)
