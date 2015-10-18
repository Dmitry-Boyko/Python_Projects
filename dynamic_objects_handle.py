
from selenium import webdriver
chromedriverpath= "C:\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
driver.get("https://paytm.com/")

# added "contain" define dynamically change element
driver.find_element_by_xpath("//input[contains(@id,'mobile')]").send_keys("96766") 

# added "*" define dynamically changed element 
driver.find_element_by_css_selector("[id*='amou']").send_keys("400") 
