def login():
 user_elements = browser.find_elements_by_xpath('//input[contains(@name, "user")]')
 for user in user_elements:
  if user.is_displayed():
   if user.is_enabled():
    user.send_keys(username)
    pass_elements = browser.find_elements_by_xpath('//input[contains(@name, "pass")]')
    for passw in pass_elements:
     if passw.is_displayed():
       if passw.is_enabled():
        passw.clear()
        passw.send_keys(password + Keys.RETURN)   #Crashes here
        time.sleep(4)
        return
