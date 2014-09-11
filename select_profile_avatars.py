# Select Change Your Profile Picture > Girls
    selenium_driver.find_element(By.XPATH, ".//*[@id='choiceMenu']/ul/li[2]/a").click()
    my_dict_GirlImage = dict()
    for i in range(9):
        my_dict_GirlImage['KeyGirlImage' + str(i+1)] = ".//*[@id='blahImage']/img[" + str(i+1) + ']'
    print "blah Images tested"
