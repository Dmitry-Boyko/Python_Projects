def delete_newCustomer(self, selenium_driver):
### "code will delete created value(Customers) with two steps verification" ###
        ui_customers = ui_map_customers_tab(selenium_driver) # populate(import) dictionary keys from element.py file

        shortName = selenium_driver.find_elements(By.ID, "short_name")
        for elem in shortName:
            if elem.text == u'automation_test':
                ui_customers.tms_newCustomer_delete_button(selenium_driver).click()
                # Browser alert agreement. Sometimes we have pop-up mesage, sometimes no. By this reason using "exception"
                try: 
                    alert = selenium_driver.switch_to.alert
                    alert.accept()
                except:
                    pass
                f.write('\nNew Customer Delete: Pass')
            elif elem.text != u'automation_test':
            
                ## Navigate to "List" and use search filter for find "custome" value.
                ui_customers.tms_List_button(selenium_driver).click()
                ui_customers.tms_newCustomer_search_txtb(selenium_driver).send_keys('automation_test')
                ui_customers.tms_newCustomer_search_button(selenium_driver).click()

                shortName = selenium_driver.find_elements(By.XPATH, "//td[4]")
                for elem in shortName:
                    if elem.text == u'db_automation_test':
                        ui_customers.tms_newCustomer_X_delete_button(selenium_driver).click()
                        try:
                            alert = selenium_driver.switch_to.alert
                            alert.accept()
                        except:
                            pass
            else:
                print('\nCustomer Delete Confirmation: Pass')
