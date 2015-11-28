__author__ = 'dmitryboyko'
# Dmitry Boyko
# cell.8184160900@yahoo.com
# MAC / Yosemite / 10.10.1

'''
OS: Windows or Mac
Browser: IE or Safari

1. Go to https://dev2.pley.com (our dev site)
2. Click on "Start My free trial" (Sign up) process
3. Complete all steps (3 in total)
4. Use 4111 1111 1111 1111 (fake card) for billing info.
5. Go up to step-4 where congratulations message is displayed.
'''

import os
import binascii
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By

from _MyGit.Python_Scripts.csv_file import write_csv_File


url = 'https://dev2.pley.com'
fullName = 'Mickey Mouse'
password = 'test_!@#$%^&-01'
addrLn1 = '1288 W El Camino Real'
addrLn2 = 'ap 0987654321'
city = 'Mountain View'
zip = '94040'
name = binascii.b2a_hex(os.urandom(3))
email = '1@1.com'
payCard = '4111111111111111'
cvv = '123'
month = '6'
year = '2020'

# For negative test
#state = 'TEST'
#country = 'blah-bla-blah'

# Using CSV file for test result:
csvFile = write_csv_File()

def driver():

    #### For Safary usage ####
    #browser = webbrowser.get('safari')
    #browser.open(url)
    #selenium_driver = webdriver.Safari()
    #### End ####
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(10)
    selenium_driver.delete_all_cookies()

    return selenium_driver

def main():
    try:
        d = driver()

        createAccount = create_Account()
        createAccount.statMyTrial(d)

        address = enter_Address()
        address.address_Reg(d)

        bill = billing()
        bill.payCard(d)

    except:
        pass

class create_Account():
    def statMyTrial(self, selenium_driver):
        try:
            selenium_driver.get(url)
            #selenium_driver.browser.open(url)
            print 'Start My Free Trial'
            selenium_driver.find_element(By.XPATH, "//section[@id='hero']/div/div/div/a").click()
            print 'button selected'
            # enter full name
            selenium_driver.find_element(By.ID, "fullname").clear()
            #selenium_driver.find_element(By.ID, "fullname").send_keys(name + " " + name)
            selenium_driver.find_element(By.ID, "fullname").send_keys(fullName)
            print 'full name added'
            # enter Email
            selenium_driver.find_element(By.ID, "email").clear()
            selenium_driver.find_element(By.ID, "email").send_keys(name + "@" + name + ".com")
            #selenium_driver.find_element(By.ID, "email").send_keys(email)
            print 'Email added'
            # enter password
            selenium_driver.find_element(By.ID, "password").clear()
            selenium_driver.find_element(By.ID, "password").send_keys(password)
            print 'password added'
            # select button "Continue"
            selenium_driver.find_element(By.XPATH, ".//*[@id='signup1']/div[4]/div/button").click()


        except Exception, err:
            print traceback.format_exc()
            #or
            print sys.exc_info()[0]
            print '_____Ooops! That was not successful "Sign In" test'

class enter_Address():
    def address_Reg(self, selenium_driver):
        try:
            selenium_driver.get("https://dev2.pley.com/signup-shipping")

            selenium_driver.find_element(By.ID, "address1").clear()
            selenium_driver.find_element(By.ID, "address1").send_keys(addrLn1)
            print 'Address 1 line added'
            selenium_driver.find_element(By.ID, "address2").clear()
            selenium_driver.find_element(By.ID, "address2").send_keys(addrLn2)
            print 'Address 2 line added'
            selenium_driver.find_element(By.ID, "city").clear()
            selenium_driver.find_element(By.ID, "city").send_keys(city)
            print 'City added'
            selenium_driver.find_element(By.ID, "state").send_keys("California")
            print 'State added'
            selenium_driver.find_element(By.ID, 'country').send_keys('United States')
            print 'Country added'
            '''
            dropDownStateID    = "state"
            dropDownElement    = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_id(dropDownStateID))
            Select(dropDownElement).select_by_visible_text("California")

            dropDownCountryID  = "country"
            dropDownElement    = WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_id(dropDownCountryID))
            Select(dropDownElement).select_by_visible_text("United States")
            '''
            # Enter a ZIP code
            selenium_driver.find_element(By.ID, "zip_code").clear()
            selenium_driver.find_element(By.ID, "zip_code").send_keys(zip)
            print 'Zip code added'
            # Select Continue button
            selenium_driver.find_element((By.XPATH, "//button[@type='submit']")).click()
            print 'Continue button selected'


        except Exception, err:
            print traceback.format_exc()
            #or
            print sys.exc_info()[0]
            print "_____Oops, Address tab not found"

class billing():
    def payCard(self, selenium_driver):
        try:
            selenium_driver.get("https://dev2.pley.com/signup-billing")

            selenium_driver.find_element(By.ID, 'cc_number').send_keys(payCard)
            print 'Pay card number added'
            selenium_driver.find_element(By.ID, 'expMonth').send_keys(month)
            print 'Exp. Month added'
            selenium_driver.find_element(By.ID, 'expYear').send_keys(year)
            print 'Exp. Month added'
            selenium_driver.find_element(By.ID, 'security_code').send_keys(cvv)
            print 'Security code added'
            #select "Get My First Set" button
            selenium_driver.find_element(By.ID,'form-submit').click()

        except Exception, err:
            print traceback.format_exc()
            #or
            print sys.exc_info()[0]
            print "_____Oops, Issue found in Billing page"



def test_done(self, selenium_driver):
    self.selenium_driver.quit()
    print '\n Done!!!'

if __name__ == "__main__":
    main()
