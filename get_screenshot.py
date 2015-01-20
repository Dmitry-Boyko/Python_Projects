from selenium import webdriver

browser = webdriver.Firefox()

try:
    # do some webdriver stuff here
except Exception as e:
    print e
    browser.get_screenshot_as_file('screenshot-%s.png' % now)
