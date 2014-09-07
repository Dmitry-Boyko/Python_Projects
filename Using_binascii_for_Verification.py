import os, binascii

name = binascii.b2a_hex(os.urandom(6))
email_n = name + '@blah.blah.ah'

selenium_driver.find_element(By.XPATH, "<//XPATH HERE>").send_keys(name)

class Bounced(): # Verification Bounced group
    def bounce_verification(self, selenium_driver):
        print('Bounce verification')
        try:
            element = selenium_driver.find_element(By.XPATH,"//ul[@id='ab-group-list']/li[2]/div/span")
            assert element.text == 'Bounced'
            print "Bounced Email found"
        except:
            print "_____Oops, Bounced group doesn't found"
