"""
__author__ dmitry.boyko

This file run automation.
Will call each "Tab" and verify submenu buttons will open expected page with expected buttons inside.

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
from tabs_subMenu_buttons.tab_Dashboard_subMenu_objects import ui_Dashboard
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

def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(30)
    selenium_driver.delete_all_cookies()
    return selenium_driver

#   Login   ############################################################################################################

                # class login():

#   Dashboard   ########################################################################################################

class test_Dashboard():
    f = open(os.path.join(path_report, "AP_Dashboard.log"), 'w')

    def open_dashboard_tab(self, selenium_driver):
        dashboard = ui_Dashboard(selenium_driver)
        dashboard.ap_dashboard_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        # crdn = my_credentials(selenium_driver)
        xPathLocator = "h2"
        # test_str = crdn.subMenu_strings()['testDashboard_Dashboard']
        test_str = u'Dashboard'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_view_button(self, selenium_driver):
        dashboard = ui_Dashboard(selenium_driver)
        dashboard.ap_subMenu_dashboard_view_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Dashboard'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_edit_button(self, selenium_driver):
        dashboard = ui_Dashboard(selenium_driver)
        dashboard.ap_subMenu_dashboard_edit_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//div[2]/fieldset/legend"
        test_str = u'Dashboard Layout'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Events  ############################################################################################################

class test_Events():
    f = open(os.path.join(path_report, "AP_Event.log"), 'w')

    def open_events_tab(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_events_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th/span"
        test_str = u'!'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th/span"
        test_str = u'!'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_details_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'Basic Information'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_access_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_access_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Access Codes'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_labs_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_labs_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Labs'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_sessions_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_sessions_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Sessions'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_notifications_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_notifications_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Notifications'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_history_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_history_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'History'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_notes_button(self, selenium_driver):
        event = ui_Events(selenium_driver)
        event.ap_subMenu_notes_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Event Notes'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Templates   ########################################################################################################

class test_Templates():
    f = open(os.path.join(path_report, "AP_Templates.log"), 'w')

    def open_template_tab(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_templates_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[6]/span"
        test_str = u'Deployment Type'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Catalog Num'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//div[2]/span/table/tbody/tr/td/span"
        test_str = u'Deployment Type'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_events_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_events_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Events'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_templateVouchers_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_templateVouchers_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Vouchers'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_content_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_content_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Content'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_history_button(self, selenium_driver):
        template = ui_Templates(selenium_driver)
        template.ap_subMenu_history_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'History'
        verif.verification(selenium_driver, xPathLocator, test_str)

#   Deployments   ######################################################################################################

class test_Deployments():
    f = open(os.path.join(path_report, "AP_Deployments.log"), 'w')

    def open_deployments_tab(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_deployments_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[6]/span"
        test_str = u'Target Platform'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Image'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'Deployment'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_channels_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_channels_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Channels'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_templates_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_templates_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Templates'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_events_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_events_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Events'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_images_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_images_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Images'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_history_button(self, selenium_driver):
        deployments = ui_Deployments(selenium_driver)
        deployments.ap_subMenu_history_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'History'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Images    ##########################################################################################################

class test_Images():
    f = open(os.path.join(path_report, "AP_Deployments.log"), 'w')

    def open_images_tab(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_images_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[6]/span"
        test_str = u'OS Type'
        verif.verification(selenium_driver, xPathLocator, test_str)


    def select_list_button(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Short Name'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_subMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'Image'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_deployments_button(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_subMenu_deployments_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Deployments'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_history_button(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_subMenu_history_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'History'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_spla_button(self, selenium_driver):
        images = ui_Images(selenium_driver)
        images.ap_subMenu_spla_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'SPLA'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Users   ############################################################################################################
class test_Users():
    f = open(os.path.join(path_report, "AP_Users.log"), 'w')

    def open_users_tab(self, selenium_driver):
        users = ui_Users(selenium_driver)
        users.ap_users_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[6]/span"
        test_str = u'Billing Entity'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        users = ui_Users(selenium_driver)
        users.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Primary Email'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        users = ui_Users(selenium_driver)
        users.ap_subMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'User'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_events_button(self, selenium_driver):
        users = ui_Users(selenium_driver)
        users.ap_subMenu_events_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Events'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Roles   ############################################################################################################
class test_Roles():
    f = open(os.path.join(path_report, "AP_Roles.log"), 'w')

    def open_roles_tab(self, selenium_driver):
        roles = ui_Roles(selenium_driver)
        roles.ap_roles_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[4]/span"
        test_str = u'Built-In'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        roles = ui_Roles(selenium_driver)
        roles.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[3]/span"
        test_str = u'Name'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        roles = ui_Roles(selenium_driver)
        roles.ap_esubMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'Role'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_users_button(self, selenium_driver):
        roles = ui_Roles(selenium_driver)
        roles.ap_subMenu_users_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Users'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_permissions_button(self, selenium_driver):
        roles = ui_Roles(selenium_driver)
        roles.ap_subMenu_permissions_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Permissions'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Entities    ########################################################################################################
class test_Entities():
    f = open(os.path.join(path_report, "AP_Entities.log"), 'w')

    def open_entities_tab(self, selenium_driver):
        entities = ui_Entities(selenium_driver)
        entities.ap_entities_tab(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[6]/span"
        test_str = u'Billing User'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        entities = ui_Entities(selenium_driver)
        entities.ap_subMenu_list_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Currency'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        entities = ui_Entities(selenium_driver)
        entities.ap_subMenu_detail_button(selenium_driver).click()
        # verification
        verif = common_funcs(self)
        xPathLocator = "//h3/span"
        test_str = u'Billing Entity'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Reports    #########################################################################################################

class test_Reports():
    f = open(os.path.join(path_report, "AP_Reports.log"), 'w')

    def open_reports_tab(self, selenium_driver):
        reports = ui_Reports(selenium_driver)
        reports.ap_reports_tab(selenium_driver).click()

        # reports_tab_verification
        verif = common_funcs(self)
        xPathLocator = "//span[5]"
        test_str = u'Skip unassigned Events:'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_eventReport_button(self, selenium_driver):
        reports = ui_Reports(selenium_driver)
        reports.ap_subMenu_eventReport_button(selenium_driver).click()

        # reports_eventReport_button_verification
        verif = common_funcs(self)
        xPathLocator = "//div/span"
        test_str = u'exact:Report:'
        verif.verification(selenium_driver, xPathLocator, test_str)

#   Systems    #########################################################################################################

class test_Systems():
    f = open(os.path.join(path_report, "AP_Systems.log"), 'w')

    def open_systems_tab(self, selenium_driver):
        systems = ui_Systems(selenium_driver)
        systems.ap_systems_tab(selenium_driver).click()

        # systems_tab_verification
        verif = common_funcs(self)
        xPathLocator = "//div[2]/a"
        test_str = u'Systems usage'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_systemUsage_button(self, selenium_driver):
        systems = ui_Systems(selenium_driver)
        systems.ap_subMenu_systemUsage_button(selenium_driver).click()

        # systems_systemUsage_button_verification
        verif = common_funcs(self)
        xPathLocator = "//button"
        test_str = u'Go'
        verif.verification(selenium_driver, xPathLocator, test_str)


#   Vouchers    ########################################################################################################

class test_Vouchers():
    f = open(os.path.join(path_report, "AP_Vouchers.log"), 'w')

    def open_vouchers_tab(self, selenium_driver):
        vouchers = ui_Vouchers(selenium_driver)
        vouchers.ap_vouchers_tab(selenium_driver)

        # vouchers_tab_verification
        verif = common_funcs(self)
        xPathLocator = "//th[2]/span"
        test_str = u'ID'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        vouchers = ui_Vouchers(selenium_driver)
        vouchers.ap_subMenu_list_button(selenium_driver).click()

        # select_list_button_verification
        verif = common_funcs(self)
        xPathLocator = "//th[3]/span"
        test_str = u'Customer'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        vouchers = ui_Vouchers(selenium_driver)
        vouchers.ap_subMenu_detail_button(selenium_driver).click()

        # select_detail_button_verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Template Vouchers'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_notifications_button(self, selenium_driver):
        vouchers = ui_Vouchers(selenium_driver)
        vouchers.ap_subMenu_notifications_button(selenium_driver).click()

        # select_notifications_button_verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Notifications'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_templateVouchers_button(self, selenium_driver):
        vouchers = ui_Vouchers(selenium_driver)
        vouchers.ap_subMenu_templateVouchers_button(selenium_driver).click()

        # select_templateVouchers_button_verification
        verif = common_funcs(self)
        xPathLocator = "//th/span"
        test_str = u'ID'
        verif.verification(selenium_driver, xPathLocator, test_str)

#   Billing    #########################################################################################################
class test_Billing():
    f = open(os.path.join(path_report, "AP_Billing.log"), 'w')

    def open_billing_tab(self, selenium_driver):
        billing = ui_Billing(selenium_driver)
        billing.ap_billing_tab(selenium_driver).click()

        # billing_tab_verification
        verif = common_funcs(self)
        xPathLocator = "//th[3]/span"
        test_str = u'Billing Entity'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_list_button(self, selenium_driver):
        billing = ui_Billing(selenium_driver)
        billing.ap_subMenu_list_button(selenium_driver).click()

        # select_list_button_verification
        verif = common_funcs(self)
        xPathLocator = "//th[5]/span"
        test_str = u'Event Name'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_detail_button(self, selenium_driver):
        billing = ui_Billing(selenium_driver)
        billing.ap_subMenu_detail_button(selenium_driver).click()

        # select_detail_button_verification
        verif = common_funcs(self)
        xPathLocator = "//h2"
        test_str = u'Estimated Price Detail'
        verif.verification(selenium_driver, xPathLocator, test_str)

    def select_payments_button(self, selenium_driver):
        billing = ui_Billing(selenium_driver)
        billing.ap_subMenu_payments_button(selenium_driver).click()

        # select_notifications_button_verification
        verif = common_funcs(self)
        xPathLocator = "//div[2]/h2"
        test_str = u'Pay By Wire Transfer - Non-US Customers'
        verif.verification(selenium_driver, xPathLocator, test_str)

#   End    #############################################################################################################
