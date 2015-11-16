# Selecting element from drop down list (now not just select command), e.g.:

el = driver.find_element_by_id('id_line')
for option in el.find_elements_by_tag_name('option'):
    if option.text == "line to select":
        option.click()
        break
        
# If there are lot of element existence checks that wrapped in try-catch block \
# it is useful to reduce implicit timeout to reduce overall test execution time, e.g. for Firefox driver:

def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(5)
    self.verificationErrors = []

# Try to avoid time.sleep(N) commands in tests it is better to wait for some \
# action or change in system. So the best way to make construction:

try:
    if self.is_element_present(By.CSS_SELECTOR, "h3 > strong"):
        driver.find_element_by_link_text("169_convertedvideo_425").click()
        self.assertTrue(int(driver.find_elements_by_css_selector("#video_source span.black")[0].text) >= 0)
    else:
        raise Exception(self.id() + ".ErrorText!")
except Exception as e: self.verificationErrors.append(str(e))
finally:
    self.removeAllMonitoringSources(driver)
    
#...or wait by small ticks:

for i in range(60):
    try:
        if self.is_element_present(By.LINK_TEXT, "Exit"): break
    except: pass
 
    time.sleep(1)
 
else: self.fail("time out")
