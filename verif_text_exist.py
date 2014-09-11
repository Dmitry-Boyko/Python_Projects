    print '\n "On This Page" menu'
    exp_menu = ["It's Easy!", 'Meet a Wufoo powered team', 'Notification Options', 'Integration & Branding', 'Themes & Templates']
    act_menu = list()
    elems_list = selenium_driver.find_elements(By.XPATH, './/*[@id=\'blah\']/div[1]/ul/li')
    for elem in elems_list:
        menu_elem = elem.text.replace('\n', '')
        act_menu.append(menu_elem)
        print menu_elem
    menu_result = cmp(exp_menu, act_menu) == 0
    print '"On This Page menu" Menu comparison result: ', menu_result
    if not menu_result:
        print 'Expected menu: ', exp_menu
        print 'Actual menu: ', act_menu
