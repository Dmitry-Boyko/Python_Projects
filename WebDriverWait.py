from selenium.webdriver.support.ui  import WebDriverWait

url_elem = WebDriverWait(driver, 10).\
        until(lambda driver: selenium_driver.find_element(By.LINK_TEXT, "Link"))
url_elem.click()
