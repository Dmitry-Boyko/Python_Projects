__author__ = 'dmitry'



import os
from selenium import webdriver
from tabs_subMenu_buttons.page_object_elem.report_path import path_report
from role_setup import roles
from ap_Roles_page_buttonsAction import Dashboard_buttons, Events_buttons, Templates_buttons, Deployments_buttons
from ap_Roles_page_buttonsAction import Images_buttons, Users_buttons, Roles_buttons, Entities_buttons, Reports_buttons
from ap_Roles_page_buttonsAction import Systems_buttons, Vouchers_buttons, Billing_buttons
from ap_Roles_subMenu_buttonAction import test_Dashboard, test_Events, test_Templates, test_Deployments, test_Vouchers, test_Billing
from ap_Roles_subMenu_buttonAction import test_Images, test_Users, test_Roles, test_Entities, test_Reports, test_Systems


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

f = open(os.path.join(path_report, "ap_role_SysAdmin_tab.log"), 'w')




def main():
    d = driver()

    # Login as a System Administrator
    login_me = roles()
    login_me.tms_logIn(d)
    login_me.systemAdmin_role(d)
    # Launch Admin Portal with selected role
    login_me.ap_logIn(d)

#   Dashboard tab    ###################################################################################################
    # Verify Dashboard tab, sub menu, page buttons
    dashboard_bttnVerf = test_Dashboard()
    dashboard_bttnVerf.open_dashboard_tab(d)
    dashboard_bttnVerf.select_view_button(d)
    dashboard_bttnVerf.select_edit_button(d)
    # Verify Dashboard page buttons
    dashboard_pageButtons = Dashboard_buttons()
    dashboard_pageButtons.save_button(d)
    dashboard_pageButtons.cancel_button(d)

#   Events tab    ######################################################################################################
    # Verify Events tab, sub menu, page buttons
    event_bttnVerf = test_Events()
    events_pageButtons = Events_buttons()

    event_bttnVerf.open_events_tab(d)
    # select List sub-menu button
    event_bttnVerf.select_list_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__search_button(d)
    events_pageButtons.events__go_button(d)

    # select detail sub-menu button
    event_bttnVerf.select_detail_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_access_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_labs_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_sessions_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_notifications_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_history_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

    event_bttnVerf.select_notes_button(d)
    # Verify visible page buttons here
    events_pageButtons.events__new_button(d)
    events_pageButtons.events__edit_button(d)
    events_pageButtons.events__delete_button(d)
    events_pageButtons.events__cancel_button(d)

#   Templates tab    ###################################################################################################

    template_btnVerf = test_Templates()
    template_pageButtons = Templates_buttons()

    template_btnVerf.open_template_tab(d)
    # Verify visible page buttons here
    template_btnVerf.select_list_button(d)
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__search_button(d)
    template_pageButtons.templates__Go_filterEvent_button(d)

    template_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__edit_button(d)
    template_pageButtons.templates__delete_button(d)

    template_btnVerf.select_events_button(d)
    # Verify visible page buttons here
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__edit_button(d)
    template_pageButtons.templates__delete_button(d)
    template_pageButtons.templates__Go_filterEvent_button(d)

    template_btnVerf.select_templateVouchers_button(d)
    # Verify visible page buttons here
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__edit_button(d)
    template_pageButtons.templates__delete_button(d)

    template_btnVerf.select_content_button(d)
    # Verify visible page buttons here
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__edit_button(d)
    template_pageButtons.templates__delete_button(d)

    template_btnVerf.select_history_button(d)
    # Verify visible page buttons here
    template_pageButtons.templates__new_button(d)
    template_pageButtons.templates__edit_button(d)
    template_pageButtons.templates__delete_button(d)

#   Deployments tab    #################################################################################################

    deployments_btnVerf = test_Deployments()
    deployments_pageButtons = Deployments_buttons()

    deployments_btnVerf.open_deployments_tab(d)
    deployments_btnVerf.select_list_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__search_button(d)
    deployments_pageButtons.deployments__go_button(d)

    deployments_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

    deployments_btnVerf.select_channels_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

    deployments_btnVerf.select_templates_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

    deployments_btnVerf.select_events_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

    deployments_btnVerf.select_images_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

    deployments_btnVerf.select_history_button(d)
    # Verify visible page buttons here
    deployments_pageButtons.deployments__new_button(d)
    deployments_pageButtons.deployments__edit_button(d)
    deployments_pageButtons.deployments__delete_button(d)

#   Images tab    ######################################################################################################

    images_btnVerf = test_Images()
    images_pageButtons = Images_buttons()

    images_btnVerf.open_images_tab(d)

    images_btnVerf.select_list_button(d)
    # Verify visible page buttons here
    images_pageButtons.images__new_button(d)
    images_pageButtons.images__search_button(d)
    images_pageButtons.images__go_button(d)

    images_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    images_pageButtons.images__new_button(d)
    images_pageButtons.images__edit_button(d)
    images_pageButtons.images__delete_button(d)

    images_btnVerf.select_deployments_button(d)
    # Verify visible page buttons here
    images_pageButtons.images__new_button(d)
    images_pageButtons.images__edit_button(d)
    images_pageButtons.images__delete_button(d)

    images_btnVerf.select_history_button(d)
    # Verify visible page buttons here
    images_pageButtons.images__new_button(d)
    images_pageButtons.images__edit_button(d)
    images_pageButtons.images__delete_button(d)

    images_btnVerf.select_spla_button(d)
    # Verify visible page buttons here
    images_pageButtons.images__new_button(d)
    images_pageButtons.images__edit_button(d)
    images_pageButtons.images__delete_button(d)

#   Users tab    #######################################################################################################

    users_btnVerf = test_Users()
    users_pageButtons = Users_buttons()

    users_btnVerf.open_users_tab(d)

    users_btnVerf.select_list_button(d)
    # Verify visible page buttons here
    users_pageButtons.users__new_button(d)
    users_pageButtons.users__search_button(d)
    users_pageButtons.users__go_button(d)

    users_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    users_pageButtons.users__new_button(d)
    users_pageButtons.users__edit_button(d)
    users_pageButtons.users__delete_button(d)

    users_btnVerf.select_events_button(d)
    # Verify visible page buttons here
    users_pageButtons.users__new_button(d)
    users_pageButtons.users__edit_button(d)
    users_pageButtons.users__delete_button(d)
    users_pageButtons.users__go_button(d)

#   Roles tab    #######################################################################################################

    roles_btnVerif = test_Roles()
    roles_pageButtons = Roles_buttons()

    roles_btnVerif.open_roles_tab(d)

    roles_btnVerif.select_list_button(d)
    # Verify visible page buttons here
    roles_pageButtons.roles__new_button(d)

    roles_btnVerif.select_detail_button(d)
    # Verify visible page buttons here
    roles_pageButtons.roles__new_button(d)
    roles_pageButtons.roles__edit_button(d)
    roles_pageButtons.roles__delete_button(d)

    roles_btnVerif.select_users_button(d)
    # Verify visible page buttons here
    roles_pageButtons.roles__new_button(d)
    roles_pageButtons.roles__edit_button(d)
    roles_pageButtons.roles__delete_button(d)

    roles_btnVerif.select_permissions_button(d)
    # Verify visible page buttons here
    roles_pageButtons.roles__new_button(d)
    roles_pageButtons.roles__edit_button(d)
    roles_pageButtons.roles__delete_button(d)

#   Entities tab    ####################################################################################################

    entities_btnVerf = test_Entities()
    entities_pageButtons = Entities_buttons()

    entities_btnVerf.open_entities_tab(d)

    entities_btnVerf.select_list_button(d)
    entities_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    entities_pageButtons.entities__delete_button(d)

#   Reports tab    #####################################################################################################

    reports_btnVerf = test_Reports()
    reports_pageButtons = Reports_buttons()

    reports_btnVerf.open_reports_tab(d)
    reports_btnVerf.select_eventReport_button(d)
    # Verify visible page buttons here
    reports_pageButtons.reports__go_button(d)

#   Systems tab    #####################################################################################################

    systems_btnVerf = test_Systems()
    system_pageButtons = Systems_buttons()

    systems_btnVerf.open_systems_tab(d)
    systems_btnVerf.select_systemUsage_button(d)
    # Verify visible page buttons here
    system_pageButtons.systems__go_button(d)
    system_pageButtons.systems__prev_button(d)
    system_pageButtons.systems__next_button(d)

#   Vouchers tab    ####################################################################################################

    voucher_btnVerf = test_Vouchers()
    voucher_pageButtons = Vouchers_buttons()

    voucher_btnVerf.open_vouchers_tab(d)

    voucher_btnVerf.select_list_button(d)
    # Verify visible page buttons here
    voucher_pageButtons.vouchers__new_button(d)
    voucher_pageButtons.vouchers__search_button(d)
    voucher_pageButtons.vouchers__go_button(d)

    voucher_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    voucher_pageButtons.vouchers__new_button(d)
    voucher_pageButtons.vouchers__edit_button(d)
    voucher_pageButtons.vouchers__delete_button(d)

    voucher_btnVerf.select_notifications_button(d)
    # Verify visible page buttons here
    voucher_pageButtons.vouchers__new_button(d)
    voucher_pageButtons.vouchers__edit_button(d)
    voucher_pageButtons.vouchers__delete_button(d)

    voucher_btnVerf.select_templateVouchers_button(d)
    # Verify visible page buttons here
    voucher_pageButtons.vouchers__go_button(d)

#   Billing tab    #####################################################################################################

    billing_btnVerf = test_Billing()
    billing_pageButtons = Billing_buttons()

    billing_btnVerf.open_billing_tab(d)

    billing_btnVerf.select_list_button(d)
    # Verify visible page buttons here
    voucher_pageButtons.vouchers__go_button(d)

    billing_btnVerf.select_detail_button(d)
    # Verify visible page buttons here
    billing_pageButtons.vouchers__delete_button(d)

    billing_btnVerf.select_payments_button(d)
    # Verify visible page buttons here
    billing_pageButtons.vouchers__payByCredit_button(d)

#   End    #############################################################################################################


    #display.stop()
    d.quit()

if __name__ == "__main__":
    main()
