from selenium.webdriver.common.alert import Alert

... ... ... (code placeholder)

### 1 ###
browser.execute_script("document.roomBookingForm.submit(); return true;")
alert = browser.switch_to_alert()
alert.dismiss()
browser.execute_script("processPayment(); return true;")

### 2 ###
if button.text == "Run":
    button.click()
try:
    alert = self.driver.switch_to_alert()
    print alert.text
except UnexpectedAlertPresentException:
    alert.send_keys('8080')
    alert.dismiss()
    
### 3 ###    
    try:
    if button.text == "Run":
        button.click()
except UnexpectedAlertPresentException:
    alert = self.driver.switch_to_alert()
    print alert.text
    alert.send_keys('8080')
    alert.dismiss()
    
    
