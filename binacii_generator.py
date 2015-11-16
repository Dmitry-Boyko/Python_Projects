import os, binascii
 
    def customize(self, selenium_driver):
        try:
            selenium_driver.find_element(By.ID, 'url-customize').click() # "Customize" button selected
            selenium_driver.find_element(By.ID, 'weblink-slug').clear()
            #### Random Generator ####
 
            #lst = [random.choice(string.ascii_letters + string.digits) for i in xrange(10)]
            #str = "".join(lst)
            #selenium_driver.find_element(By.ID, 'weblink-slug').send_keys(str)
            #selenium_driver.find_element(By.ID, 'slug-save').click()
 
            print binascii.b2a_hex(os.urandom(6))
            selenium_driver.find_element(By.ID, 'weblink-slug').send_keys(binascii.b2a_hex(os.urandom(6)))
            selenium_driver.find_element(By.ID, 'slug-save').click()
            print 'Custom URL saved'
 
        except ValueError:
            print 'Custom URL doesn\'t saved'
