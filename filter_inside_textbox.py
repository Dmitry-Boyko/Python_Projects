def main(): 
    fl = forms_filter(driver())
    fl.login(forms_filter)
    fl.clear_click(forms_filter)
    fl.rand_abc(forms_filter)
    fl.rep_rand(forms_filter)
    
class forms_filter():
    def __init__(self, driver):
        self.selenium_driver = driver
        
    def login(self, driver):
    
       # Select "Filter" box
    def clear_click(self, driver):
        self.selenium_driver.find_element(By.XPATH,'.//*[@id=\'searchBox\']').clear()
        self.selenium_driver.find_element(By.XPATH,'.//*[@id=\'searchBox\']').click()
 
    def rand_abc(self, driver):
        #abc = ['a','ab','abc','abcd', 'abcde','abcdef',]
        abc = ['a','b','c','d', 'e','f','g','h','i']  
        
    #### Random 01 ####
        random_abc = (''.join(random.choice(abc) for i in range(2)))
        self.selenium_driver.find_element(By.XPATH,'.//*[@id=\'searchBox\']').send_keys(random_abc)
        print 'Random: ' + random_abc
        time.sleep(2)
        self.selenium_driver.find_element(By.XPATH,'.//*[@id=\'searchBox\']').clear()
    
    def rep_rand(self, driver): # repeat rand_abc
        for i in range(100):self.rand_abc(driver)
