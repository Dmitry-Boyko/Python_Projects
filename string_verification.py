###   File: object_map.py   ###

class verification():

    def __init__(self, selenium_driver):
        self.selenium_driver = selenium_driver

    def verification_string(self, selenium_driver, xPathLocator, text_str):
        f = open(os.path.join(path_report, "access_tab.log"), 'aw')

        ver_str = selenium_driver.find_elements(By.XPATH, xPathLocator)
        for elem in ver_str:
            if elem.text != text_str:
                f.write("\nVerification Failed: element text is not %r" % elem.text)
            else:
                f.write("\nVerification %r: Pass" % elem.text)
                
###  File test.py  ###

from objects_map import verification

f = open(os.path.join(path_report, "access_tab.log"), 'w')

class name():

    def access_tab(self, selenium_driver):
        ui_access = ui_map_access_tab(selenium_driver)
        ui_button = ui_map_buttons(selenium_driver)
        
        verif = verification(self)

        # verification by string on page: Access
        xPathLocator = "//h3"
        text_str = u"Access"
        verif.verification_string(selenium_driver, xPathLocator, text_str)

