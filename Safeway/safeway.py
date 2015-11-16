#!/usr/bin/python
__author__ = 'dmitryboyko'

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # "Expected Condition"
from nose.tools import assert_true, assert_false

from credentials import my_credentials


def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(5)
    #selenium_verificationErrors = []
    #selenium_driver.delete_all_coocies()
    selenium_driver.get(my_credentials().get("url"))
    return selenium_driver

class login(): # login should be separate file
    def credentions(self, selenium_driver):
        try:
            #element = WebDriverWait(selenium_driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, my_acc))
            selenium_driver.find_element(By.LINK_TEXT, "Sign In").click()
            selenium_driver.implicitly_wait(4)
            print 'SignIn found'
            selenium_driver.find_element(By.ID, "userId").clear()
            #selenium_driver.find_element(By.ID, "userID_tb").send_keys("email")
            selenium_driver.find_element(By.ID, "userId").send_keys("dboyko@gmail.com")
            selenium_driver.implicitly_wait(3)
            selenium_driver.find_element(By.ID, "password").clear()
            selenium_driver.find_element(By.ID, "password").send_keys("dima1234")
            selenium_driver.implicitly_wait(3)
            selenium_driver.find_element(By.ID, "SignInBtn").click()
        except:
            print 'SignIn not found'
            #webdriver.Firefox.quit()
class save_up(): # redirecting to "Usave"
    def elem_present(self, selenium_driver): # verify banner exist
        try:
            selenium_driver.implicitly_wait(5)
            el = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#promo_eyebrow>a>img")))
        except:
            pass

    def saving(self, selenium_driver): # select banner
        try:
            selenium_driver.find_element(By.CSS_SELECTOR, "#promo_eyebrow>a>img").click()
            print "Saving button clicked"
        except:
            pass

    def coupon_center(self, selenium_driver): # Coupons page
        try:
            selenium_driver.find_element(By.CSS_SELECTOR, 'img[alt="Coupon Center. Digital Coupons. No Clipping. Click here to view coupons."]').click()
            print "Coupon Center found and clicked"
        except:
            print "Coupon Center not found"

    def sorts(self, selenium_driver): # drop down menu
        try:
            selenium_driver.implicitly_wait(5)
            el = selenium_driver.find_element(By.ID, "topSortOrder")
            for option in el.find_element(By.ID, "ext-gen1096"):
                if option.text == 'New Offers':
                    option.click() # select() in earlier versions of webdriver

            #selenium_driver.find_element(By.ID, "topSortOrder").click()
            #selenium_driver.find_element(By.ID, "ext-gen1096").click()
            print "New Offers choosed"
        except:
            print "Drop down menu not found"

    def click_on(self, selenium_driver): # Add items to my card #//div[8]/div[4]/div/a/span
        try:
            my_dict_coupon = dict()
            for i in range(2, 51):
                #my_dict_coupon ['keyAddCoupon' + str(i+1)] = ".#ext-gen" + str(i+1) + "]"
                selenium_driver.find_element(By.XPATH, "//div["+str(i+1)+"]/div[4]/div/a/span").click()

            for key in my_dict_coupon:
                print key

#            add_coupon = selenium_driver.find_element(By.ID, "ext-gen"+'[]')
#            for coupon in add_coupon:
#                if not coupon.isSelecter():
#                    coupon.click()

            print "Coupons found and clicked"
        except:
            print "No more Coupos"

def main():
    #selenium_driver = driver()
    d = driver()

    log_in = login()
    log_in.credentions(d)

    saveup = save_up()
    saveup.elem_present(d)
    saveup.saving(d)
    saveup.coupon_center(d)
    saveup.sorts(d)
    saveup.click_on(d)

if __name__ == "__main__":
    main()
