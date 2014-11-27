### Explicit Waits ###
'''
An explicit waits is code you define to wait for a certain condition to occur 
before proceeding further in the code. The worst case of this is time.sleep(), 
which sets the condition to an exact time period to wait. There are some 
convenience methods provided that help you write code that will wait only as 
long as required. WebDriverWait in combination with ExpectedCondition is one 
way this can be accomplished.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

ff = webdriver.Firefox()
ff.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
finally:
    ff.quit()
    
'''
Expected Conditions
There are some common conditions that are frequently come across when automating web browsers. Listed below are Implementations of each. Java happens to have convienence methods so you don’t have to code an ExpectedCondition class yourself or create your own utility package for them.

Element is Clickable - it is Displayed and Enabled.
'''
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

### Implicit Waits ###
'''
An implicit wait is to tell WebDriver to poll the DOM for a certain amount of 
time when trying to find an element or elements if they are not immediately available. 
The default setting is 0. Once set, the implicit wait is set for the life of the 
WebDriver object instance.
'''
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
