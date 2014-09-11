# URL links in text
    
    elemThemeDes = selenium_driver.find_element(By.XPATH, './/*[@id=\'blah\']/p[4]/a[1]')
    if elemThemeDes.is_displayed():
        print '\n"Theme Designer" URL link exist'
    else:
        print '"Theme Designer" URL link not found'
    
