"""
__author__ dmitry.boyko

This file run automation.
Will call each "button" located inside submenu pages with Roles verification dependency.

"""


import os
import sys
import binascii
from tabs_subMenu_buttons.page_object_elem.report_path import path_report
import datetime
from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support.select  import Select # use for drop down menu
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tabs_subMenu_buttons.page_object_elem.ap_elements import presets
from tabs_subMenu_buttons.page_object_elem.ap_variables import my_credentials, common_funcs
from tabs_subMenu_buttons.tab_Dashboard_subMenu_objects import verification
from tabs_subMenu_buttons.tab_Events_subMenu_objects import ui_Events
from tabs_subMenu_buttons.tab_Templates_subMenu_objects import ui_Templates
from tabs_subMenu_buttons.tab_Deployments_subMenu_objects import ui_Deployments
from tabs_subMenu_buttons.tab_Images_subMenu_objects import ui_Images
from tabs_subMenu_buttons.tab_Users_subMenu_objects import ui_Users
from tabs_subMenu_buttons.tab_Roles_subMenu_objects import ui_Roles
from tabs_subMenu_buttons.tab_Entities_subMenu_objects import ui_Entities
from tabs_subMenu_buttons.tab_Reports_subMenu_objects import ui_Reports
from tabs_subMenu_buttons.tab_Systems_subMenu_objects import ui_Systems
from tabs_subMenu_buttons.tab_Vouchers_subMenu_objects import ui_Vouchers
from tabs_subMenu_buttons.tab_Billing_subMenu_objects import ui_Billing
from tabs_subMenu_buttons.page_object_elem.ap_variables import my_credentials
from tabs_subMenu_buttons.page_object_elem.ap_elements import presets

def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(30)
    selenium_driver.delete_all_cookies()
    return selenium_driver


#   Dashboard   ########################################################################################################

class Dashboard_buttons():
    f = open(os.path.join(path_report, "AP_Dashboard_pageButtons.log"), 'w')


    def save_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "dashboard_save_button"
        button_name = u"Save"

        verif.verification_button(selenium_driver, IDLocator, button_name)

    def cancel_button(self, selenium_driver):
        verif = verification(self)
        IDLocator = "dashboard_cancel_button"
        button_name = u"Edit"

        verif.verification_button(selenium_driver, IDLocator, button_name)
        '''
        btnPresent = presets(selenium_driver)

        page_button = selenium_driver.find_elements(By.ID, btnPresent.page_buttons()['dashboard_cancel_button'])
        for button in page_button:
            if button.is_displayed():
                f.write(btnPresent.page_buttons()['dashboard_cancel_button'], 'observed')
        '''

#   Event   ############################################################################################################

class Events_buttons():
    f = open(os.path.join(path_report, "AP_Events_pageButtons.log"), 'w')

    def events__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Event"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def events__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_event"
        button_name = u"Search Event"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def events__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def events__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Event"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def events__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Event"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def events__cancel_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "cancel_button"
        button_name = u"Cancel Event"
        verif.verification_button(selenium_driver, IDLocator, button_name)


#   Templates   ########################################################################################################

class Templates_buttons():
    f = open(os.path.join(path_report, "AP_Templates_pageButtons.log"), 'w')

    def templates__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Template"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def templates__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_template"
        button_name = u"Search Template"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def templates__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def templates__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Template"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def templates__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Template"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def templates__Go_filterEvent_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go_filterEvent"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

#   Deployments   ######################################################################################################

class Deployments_buttons():
    f = open(os.path.join(path_report, "AP_Deployments_pageButtons.log"), 'w')

    def deployments__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Deployment"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def deployments__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_template"
        button_name = u"Search Deployment"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def deployments__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def deployments__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Deployment"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def deployments__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Deployment"
        verif.verification_button(selenium_driver, IDLocator, button_name)


#   Images   ###########################################################################################################


class Images_buttons():
    f = open(os.path.join(path_report, "AP_Images_pageButtons.log"), 'w')

    def images__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Image"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def images__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_images"
        button_name = u"Search Image"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def images__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def images__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Image"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def images__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Image"
        verif.verification_button(selenium_driver, IDLocator, button_name)

#   Users   ############################################################################################################

class Users_buttons():
    f = open(os.path.join(path_report, "AP_Users_pageButtons.log"), 'w')

    def users__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New User"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def users__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_images"
        button_name = u"Search User"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def users__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def users__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit User"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def users__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete User"
        verif.verification_button(selenium_driver, IDLocator, button_name)


#   Roles   ############################################################################################################

class Roles_buttons():
    f = open(os.path.join(path_report, "AP_Roles_pageButtons.log"), 'w')

    def roles__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Role"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def roles__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Role"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def roles__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Role"
        verif.verification_button(selenium_driver, IDLocator, button_name)


#   Entities   #########################################################################################################

class Entities_buttons():
    f = open(os.path.join(path_report, "AP_Entities_pageButtons.log"), 'w')

    # Go to Details page
    def entities__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Billing Entity"
        verif.verification_button(selenium_driver, IDLocator, button_name)

#   Reports   #########################################################################################################

class Reports_buttons():
    f = open(os.path.join(path_report, "AP_Reports_pageButtons.log"), 'w')

    def reports__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

#   Systems   ##########################################################################################################

class Systems_buttons():
    f = open(os.path.join(path_report, "AP_Systems_pageButtons.log"), 'w')

    def systems__prev_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "systems_prev"
        button_name = u"Prev"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def systems__next_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "systems_next"
        button_name = u"Next"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def systems__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)


#   Vouchers   #########################################################################################################

class Vouchers_buttons():
    f = open(os.path.join(path_report, "AP_Vouchers_pageButtons.log"), 'w')

    def vouchers__new_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "new_button"
        button_name = u"New Voucher Block"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def vouchers__search_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "search_images"
        button_name = u"Search Voucher Block"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def vouchers__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    # Go to Details page
    def vouchers__edit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "edit_button"
        button_name = u"Edit Voucher Block"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def vouchers__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete Voucher Block"
        verif.verification_button(selenium_driver, IDLocator, button_name)

#   Billing   ##########################################################################################################

class Billing_buttons():
    f = open(os.path.join(path_report, "AP_Billing_pageButtons.log"), 'w')

    def billing__go_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "go"
        button_name = u"Go"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def vouchers__delete_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "delete_button"
        button_name = u"Delete No Data"
        verif.verification_button(selenium_driver, IDLocator, button_name)

    def vouchers__payByCredit_button(self, selenium_driver):
        # btnPresent = presets(selenium_driver)
        verif = verification(self)
        IDLocator = "billing_payByCard"
        button_name = u"Pay By Credit Card"
        verif.verification_button(selenium_driver, IDLocator, button_name)

########################################################################################################################
