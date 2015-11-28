
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

moved = selenium_driver.find_element(By.XPATH, <''>)
target = selenium_driver.find_element(By.CSS_SELECTOR, <''>)
ActionChains(selenium_driver).drag_and_drop(moved, target).perform()
