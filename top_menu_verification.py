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
    selenium_driver.get("http://www.wustage.com/annual/")
    
####    T O P  T A B L E    #####
    print 'T O P  T A B L E\n'
    
    tp = TestPricing()
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[1]', ['AD INFINITUM$1,799per YearSign Up!60 UsersUnlimited FormsUnlimited ReportsMax Fields *100,000 Entries / Month10 GB StorageSSL EncryptionPayment Integration'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[2]', ['CARPE DIEM$599per YearSign Up!20 UsersUnlimited FormsUnlimited ReportsMax Fields *15,000 Entries / Month3 GB StorageSSL EncryptionPayment Integration'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[3]', ['BONA FIDE$259per YearSign Up!5 UsersUnlimited FormsUnlimited ReportsMax Fields *3,000 Entries / Month1 GB StorageSSL EncryptionPayment Integration']) 
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[4]', ['AD HOC$129per YearSign Up!1 User10 Forms20 ReportsMax Fields *500 Entries / Month250 MB StorageSSL Encryption'])
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[5]', ['GRATISFREE!ForeverSign Up!1 User3 Forms3 Reports10 Fields100 Entries / MonthSSL Encryption'])
    

    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[3]', ['BONA FIDE$259per YearSign Up!5 UsersUnlimited FormsUnlimited ReportsMax Fields *3,000 Entries / Month1 GB StorageSSL EncryptionPayment Integration']) 
     
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[4]', ['AD HOC$129per YearSign Up!1 User10 Forms20 ReportsMax Fields *500 Entries / Month250 MB StorageSSL Encryption'])
    
    tp.Per_Year_Top(selenium_driver, './/*[@id=\'main\']/div/table/tbody/tr/td[5]', ['GRATISFREE!ForeverSign Up!1 User3 Forms3 Reports10 Fields100 Entries / MonthSSL Encryption'])
    
