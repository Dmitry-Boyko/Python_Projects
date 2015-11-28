def is_addressbook_displayed_and_loaded(driver):
    url_correct = '/addressbook/' in driver.current_url
    sidebar_visible = driver.find_element(By.XPATH, "<xpath>") is not None
    main_column_visible = driver.find_element(By.XPATH, "<xpath>']") is not None
    addContacts_visible = driver.find_element(By.ID, "<id>") is not None
    return (url_correct and sidebar_visible and main_column_visible and addContacts_visible)
