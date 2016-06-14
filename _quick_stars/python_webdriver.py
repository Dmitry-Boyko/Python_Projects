from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("https://www.skype.com/en/")


def login():
    
    username = 'name.Sam'
    password = 'passw.Sam'

    driver.find_element_by_link_text('Sign in').click()

    user_elements = driver.find_elements_by_xpath('//input[contains(@name, "user")]')
    for user in user_elements:
        if user.is_displayed():
            if user.is_enabled():
                user.send_keys(username)
                pass_elements = driver.find_elements_by_xpath('//input[contains(@name, "pass")]')
                for passw in pass_elements:
                    if passw.is_displayed():
                        if passw.is_enabled():
                            passw.clear()
                            passw.send_keys(password)
                            submit_elements = driver.find_elements_by_id('signIn')
                            for submit in submit_elements:
                                if submit.is_displayed():
                                    if submit.is_enabled():
                                        submit.click()
                                        return

login()
