### Verification relation between radio buttons and actual table(3x3) ###

            selenium_driver.find_element(By.ID, "<..>").click()
            print("3x3 radio button selected")
            numberOfCells=selenium_driver.find_elements(By.XPATH, tablexPath)
            row=selenium_driver.find_element(By.XPATH, tablexPath)
            columns_list=row.find_elements(By.XPATH, "td")
            print'Table',(len(columns_list)),'x',(len(numberOfCells)),'found.'
            selenium_driver.implicitly_wait(2)
