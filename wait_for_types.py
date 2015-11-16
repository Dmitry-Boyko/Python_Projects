# Havy Hamer
time.sleep(sec)

### Smooth types: ###

# implicitly_wait
def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(10)

# If element UI displayed
def is_<Module_name>_displayed_and_loaded(driver):
    url_correct = '/module_name/' in driver.current_url
    sidebar_visible = driver.find_element(By.XPATH, "<XPATH>") is not None
    main_column_visible = driver.find_element(By.XPATH, "<XPATH>") is not None
    addContacts_visible = driver.find_element(By.ID, "<ID>") is not None
    return (url_correct and sidebar_visible and main_column_visible and addContacts_visible)
