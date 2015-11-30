# Send date to text-box
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def driver():
    selenium_driver = webdriver.Firefox()

def set_a_date(selenium_driver):

    ## Data tuday
    selenium_driver.find_element(By.ID, "text-box Date").send_keys(time.strftime("%d/%m/%Y"))

    ## Data tomorrow
    td = datetime.datetime.now() + datetime.timedelta(days=1)
    selenium_driver.find_element(By.ID, "text-box Date").send_keys((td.strftime("%m/%d/%Y")))
