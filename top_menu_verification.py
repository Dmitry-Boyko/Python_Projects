class TestPricing:
    
    def __init__(self):
        pass

    def Per_Year_Top(self, selenium_driver, xpath, expected):
        actual = list()
        elems_list = selenium_driver.find_elements(By.XPATH, xpath)
        for elem in elems_list:
            menu_elem = elem.text.replace('\n', '')
            actual.append(menu_elem)
            print menu_elem
        menu_result = cmp(expected, actual) == 0
        print 'Menu comparison result: ', menu_result, '\n'
        if not menu_result:
            print 'Expected menu: ', expected, '\n'
            print 'Actual menu: ', actual, '\n'
        time.sleep(3)
        
def main():
    
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(10)
    selenium_driver.delete_all_cookies()
    selenium_driver.get("http://www.blahblah.com/blah/")
    
####    T O P  T A B L E    #####
    print 'T O P  T A B L E\n'
    
    tp = TestPricing()
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[1]', ['<text for verification here>'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[2]', ['<text for verification here>'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[3]', ['<text for verification here>']) 
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[4]', ['<text for verification here>'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[5]', ['<text for verification here>'])
    

    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[3]', ['<text for verification here>']) 
     
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[4]', ['<text for verification here>'])
    
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[5]', ['<text for verification here>'])
    
