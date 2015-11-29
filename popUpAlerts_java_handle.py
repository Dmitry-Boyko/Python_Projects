from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.tizag.com/javascriptT/javascriptalert.php")
driver.find_element_by_xpath("//div[@class='display']/form/input").click()
print(driver.switch_to_alert().text) # will grab the text from popup window
driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()
driver.switch_to_alert().send_keys("adafds") # will add information inside textbox which implemented in popup window.

## or, if popUp(alert) only possible:
try:
  alert = selenium_driver.switch_to.alert
  alert.accept()
except:
  pass
