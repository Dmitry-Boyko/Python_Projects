numberOfCells=selenium_driver.find_elements(By.XPATH, tablexPath)
row=selenium_driver.find_element(By.XPATH, tablexPath)
columns_list=row.find_elements(By.XPATH, "td")
print'Table',(len(columns_list)),'x',(len(numberOfCells)),'found.'
