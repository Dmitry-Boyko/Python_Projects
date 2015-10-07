import os, binascii

name = binascii.b2a_hex(os.urandom(6))
email_n = name + '@blah.blah.ah'

selenium_driver.find_element(By.XPATH, "<//XPATH HERE>").send_keys(name)

class Bounced(): # Verification Bounced group
    def bounce_verification(self, selenium_driver):
        print('Bounce verification')
        try:
            strElement = selenium_driver.find_element(By.XPATH,"<//XPATH HERE>")
            for elem in strElement:
                if elem.text != 'TextStr':
                    print('TextStr verification Fail: is not %r' % elem.text)
     
