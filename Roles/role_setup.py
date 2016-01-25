__author__ = 'dboyko'

"""
This file contain Log-In/Log-Out to TMS function and numbers of roles.
Each role function should setup TMS/AP and be called before role test.
"""

#
#
#
import os
import sys
from selenium                                               import webdriver
from selenium.webdriver.common.by                           import By
from tabs_subMenu_buttons.page_object_elem.ap_variables     import my_credentials
from selenium.webdriver.support.select                      import Select # use for drop down menu
from selenium.webdriver.support.ui                          import WebDriverWait
from tabs_subMenu_buttons.page_object_elem.report_path      import path_report


'''
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()
'''

def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(30)
    selenium_driver.delete_all_cookies()
    return selenium_driver

f = open(os.path.join(path_report, "role_setup.log"), 'w')

def main():
    d = driver()

    role = roles()
    role.ap_logIn(d)


class roles():
    # open __tms url
    # navigate to Edit Profile
    # Verify type of account
    # crdn = my_credentials()

    def tms_logIn(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.get(crdn.login_var()["tms_146"])
        selenium_driver.get(crdn.urls()["tms_url"])
        selenium_driver.find_element(By.ID, "j_username").send_keys(crdn.login()["username"])
        selenium_driver.find_element(By.ID, "j_password").send_keys(crdn.login()["password"])
        selenium_driver.find_element(By.NAME, crdn.login()["login_button"]).click()
        selenium_driver.find_element(By.LINK_TEXT, "Events")
        selenium_driver.find_element(By.ID, "arrow").click()
        selenium_driver.find_element(By.LINK_TEXT, "Edit Profile").click()

    def ap_logIn(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.get(crdn.login_var()["tms_146"])
        selenium_driver.get(crdn.urls()["ap_url"])
        selenium_driver.find_element(By.ID, "j_customername").send_keys(crdn.login()["customername"])
        selenium_driver.find_element(By.ID, "j_username").send_keys(crdn.login()["username"])
        selenium_driver.find_element(By.ID, "password").send_keys(crdn.login()["password"])
        selenium_driver.find_element(By.ID, crdn.login()["login_button"]).click()


    def systemAdmin_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("System Administrator")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("System Administrator")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: System Administrator")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"System Administrator":
                print('\nRole selection Fail, role not a %r' % role.text)
        '''
        try:
            exp_text = ['System Administrator']
            act_text = list()
            elems_list = selenium_driver.find_elements(By.XPATH, "//tr[13]/td[2]")
            for elem in elems_list:
                menu_elem = elem.text.replace('\n', '')
                act_text.append(menu_elem)
                f.write(menu_elem)

            menu_result = cmp(exp_text, act_text) == 0
            f.write('Role comparison result: ' + str(menu_result))
            if not menu_result:
                f.write('Expected text: ' + str(exp_text))
                f.write('Actual text: ' + str(act_text))
                #f.write("Portal Role: Partner Instructor")

        except Exception, err:
            sys.stderr.write('ERROR: %sn' % str(err))
            return 1
            #f.write("____Portal Role: System Administrator not selected")
        '''

    def globalManager_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("Global Manager")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("Global Manager")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: Global Manager")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"Global Manager":
                f.write('\nRole selection Fail, role not a %r' % role.text)

    def partnerInstructor_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("Partner Instructor")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("Partner Instructor")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: Partner Instructor")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"Partner Instructor":
                f.write('\nRole selection Fail, role not a %r' % role.text)

    def partnerManager_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("Partner Manager")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("Partner Manager")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: Partner Manager")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"Partner Manager":
                f.write('\nRole selection Fail, role not a %r' % role.text)

    def ReadOnly_Manager_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("Read-Only Manager")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("Read-Only Manager")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: Read-Only Manager")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"Read-Only Manager":
                f.write('\nRole selection Fail, role not a %r' % role.text)

    def employeeInstructor_role(self, selenium_driver):
        crdn = my_credentials()

        #selenium_driver.find_element(By.ID, "portalRoleId").click()
        dropDownElement = WebDriverWait(driver, 10).\
            until(lambda driver: selenium_driver.find_element(By.ID, "portalRoleId"))
        Select(dropDownElement).select_by_visible_text("Employee Instructor")
        # selenium_driver.find_element(By.ID, "portalRoleId").send_keys("Employee Instructor")
        # Save setting
        selenium_driver.find_element(By.ID, crdn.profile()['profile_save_button']).click()
        f.write("\nPortal Role: Employee Instructor")

        # Role Verification
        role_verif = selenium_driver.find_elements(By.ID, crdn.profile()['portalRole'])
        for role in role_verif:
            if role.text != u"Employee Instructor":
                f.write('\nRole selection Fail, role not a %r' % role.text)



    def log_out(self, selenium_driver):
        crdn = my_credentials()
        try:
            selenium_driver.find_element(By.ID, "arrow").click()
            selenium_driver.find_element(By.LINK_TEXT, "Logout").click()
            f.write("Logout: Pass")
        except Exception, err:
            sys.stderr.write('ERROR: %sn' % str(err))
            return 1
            #f.write("Logout: Fail")

if __name__ == "__main__":
    main()

