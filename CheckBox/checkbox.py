from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://blah_blah_blah.com")
try:
    elem= driver.find_element_by_name("chk_email")
    if (elem.is_selected()):
        print("Checkbox is selected..now deselecting")
        elem.click()
    else:
        print("Checkbox is not selected..now selecting it")
        elem.click()
   
    driver.close()
    
except Exception as e:
    print ("Exception occured", format(e));

finally:
    driver.quit()
    print ("done")
