# Verify_element_by_text

        element = 'Deployment Usage and Aging Report'
        selenium_driver.find_element(By.CSS_SELECTOR, '#<..>')
        if element != u'Deployment Usage and Aging Report':
            print "Text verification Failed: element text is not %r" % element
        else:
            print('Deployment Usage and Aging Report - verified')

# Verify word in sentence exist

from selenium.webdriver.support.ui import WebDriverWait

sentence = WebDriverWait(driver, 10).\
        until(lambda driver: selenium_driver.find_element(By.ID, 'custom_text'))
for elem in sentence:
        if elem.text == u"hope":
                print('Element "hope" in text found, test pass')
        else:
                selenium_driver.refresh()
                        
