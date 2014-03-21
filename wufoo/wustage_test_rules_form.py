'''
Created on Jan 24, 2014
 
wustage_test_rules_form.py
 
@author: dmitryb
'''
 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
#baseurl = "https://secure.wustage.com/signup/1/"
baseurl = "https://secure.wustage.com/login/"
username = 'PageRulesTest'
password = '2693l'
email = 'wufooman@gmail.com'
XPATH = {'emailTxtBox' : ".//*[@id='email']", 'passwordTxtBox1' : './/*[@id=\'password\']', 'passwordTxtBox2' : './/*[@id=\'password1\']','accountName' : ".//*[@id='wufooName']",'createAccButton' : './/*[@id=\'signupButton\']'}
def main():
  
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(10)
    #selenium_driver.get('https://secure.wustage.com/login/')
    #selenium_driver.get('https://secure.wustage.com/signup/1/')
    selenium_driver.delete_all_cookies()
    selenium_driver.get(baseurl)
 
   
    selenium_driver.get('https://secure.wustage.com/login/')
    selenium_driver.find_element(By.ID,'email').send_keys('wufooman@gmail.com')
    selenium_driver.find_element(By.ID,'password').send_keys('2693l')
    selenium_driver.find_element(By.ID,'saveForm').click()
   
    '''
    selenium_driver.find_element(By.XPATH, XPATH['emailTxtBox']).clear()
    selenium_driver.find_element(By.XPATH, XPATH['emailTxtBox']).send_keys(email)
    print 'emailTxtBox - done!'
    selenium_driver.find_element(By.XPATH, XPATH['passwordTxtBox1']).send_keys(password)
    selenium_driver.find_element(By.XPATH, XPATH['passwordTxtBox2']).send_keys(password)
    print 'password - done!'
    selenium_driver.find_element(By.XPATH, XPATH['accountName']).send_keys(username)
    print 'wufooName - done!'
    selenium_driver.find_element(By.XPATH, XPATH['createAccButton']).click()
    time.sleep(10)
    print 'Account Created'
    '''
   
    #### Create New Form ####
#def Create_Form(self, selenium_driver):
    print'Ready to create 3 pages Form'
    selenium_driver.find_element(By.XPATH, './/*[@id=\'stage\']/div[1]/div[1]/a').click()   # CLick "New Form!" button
    time.sleep(5)
    selenium_driver.find_element(By.ID, 'sl').click()
    selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
    time.sleep(3)
    selenium_driver.find_element(By.ID, 'foli1').click()
    selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').clear()
    selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').send_keys('text field')
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').send_keys('text field<img src="http://images4.wikia.nocookie.net/__cb20060520005228/starwars/images/c/c6/Spaceballs_DVD_cover.jpg" />')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
    selenium_driver.find_element(By.ID, 'ml').click()
    selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
    selenium_driver.find_element(By.ID,'title2').click()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').clear()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').send_keys('text box')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
    time.sleep(3)
    selenium_driver.find_element(By.ID, 'em').click()
    #selenium_driver.find_element(By.ID, 'na').click()
    print'Page 1: Created'
    time.sleep(3)
    selenium_driver.find_element(By.ID, 'pb').click()   # page breaker 2/3
    selenium_driver.find_element(By.ID, 'sl').click()
    selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
    time.sleep(3)
    selenium_driver.find_element(By.ID, 'foli1').click()
    #selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').clear()
    #selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').send_keys('text field')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
    selenium_driver.find_element(By.ID, 'ml').click()
    #selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
    #selenium_driver.find_element(By.ID,'title2').click()
    #selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').clear()
    #selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').send_keys('text box')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
    time.sleep(3)
    print'Page 2: Created'
    selenium_driver.find_element(By.ID, 'pb').click()   # page breaker 3/3
    selenium_driver.find_element(By.ID, 'sl').click()
    selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
    time.sleep(3)
    selenium_driver.find_element(By.ID, 'foli1').click()
    #selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').clear()
    #selenium_driver.find_element(By.XPATH, './/*[@id=\'fieldTitle\']').send_keys('text field')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
    selenium_driver.find_element(By.ID, 'ml').click()
    print'Page 3: Created'
    selenium_driver.find_element(By.LINK_TEXT,'Field Settings').click()
 
    
 
    selenium_driver.find_element(By.ID,'title2').click()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').clear()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'fieldTitle\']').send_keys('text box')
    selenium_driver.find_element(By.LINK_TEXT, 'Add Field').click() # add field button
  
    time.sleep(3)
    
    selenium_driver.find_element(By.ID, 'saveForm').click() # Save Form >>> Registration
    time.sleep(5)
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'lbContent\']/ol/li[3]/a/b').click() # Confirmation for Save Form >>> Registration
    time.sleep(5)
   
 
 
    print'Form Saved'
   
#def rules():   
    ### Create Rule 1 ###
    print'Create rule 1'
   
    selenium_driver.find_element(By.XPATH, './/*[@id=\'expandThis\']/div/a[7]').click() # click "Rules" icon
    time.sleep(3)
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'wl\']/a').click()   #    select Form Rules tab
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'formRulesWarning\']/a[1]').click()   #    Select "Create a Form Rule"
    
    ###
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_FieldName').click() #    click on "if" field
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'Fields\']/li[4]/a').click()   #    switch to "Email"
    ###
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Filter').click()
    selenium_driver.find_element(By.LINK_TEXT,'contains').click()   #    switch "contains" from "is"
    ###
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Value').clear()
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Value').send_keys('wufoos@gmail.com')
    ###
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Type_SendEmail').click()    #    Selected radio button 'Send Email '
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Setting_SendEmail_Type').click()    #    Click "Send-notification"
    selenium_driver.find_element(By.LINK_TEXT,'confirmation').click()   #    choose "confirmation"
    ###
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Setting_ConfirmationEmail_Name').send_keys('Dark Helmet')   #    FIll out "Your Name" text box
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Setting_ConfirmationEmail_ReplyTo').send_keys('dmitryb@surveymonkey.com')   #    Replay to Email Address
    #selenium_driver.find_element(By.CLASS_NAME,'text value').send_keys('Form Rules Test Done')  #    Subject line
    ###
    selenium_driver.find_element(By.LINK_TEXT,'Save Form Rules').click()    #    click "Save Form Rules" button
   
    ####    Navigate to Forms    ####
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[1]/a').click()             #    Navigate to Forms
   
    #### Open Form ####
    selenium_driver.find_element(By.CLASS_NAME,'entries').click()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'first\']/div[2]/a').click() # Create a New Entry
    #selenium_driver.find_element(By.LINK_TEXT,'Create a New Entry').click()
    print '\nForm is Open\n'
    selenium_driver.find_element(By.ID,'Field3').send_keys('wufoos@gmail.com') # fill out Email text field
   
    selenium_driver.find_element(By.ID,'nextPageButton').click() # click Next
    time.sleep(3)
    selenium_driver.find_element(By.ID,'nextPageButton').click() # click Next
    time.sleep(3)
    selenium_driver.find_element(By.ID,'saveForm').click()  # click Submit
    time.sleep(3)
   
    ####    Navigate to Forms    ####
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[1]/a').click()             #    Navigate to Forms
 
    
    ## delete "Rules -> Form Rules"
    ### Rules ###
    selenium_driver.find_element(By.XPATH, './/*[@id=\'expandThis\']/div/a[7]').click() # click "Rules" icon
    time.sleep(3)
    selenium_driver.find_element(By.LINK_TEXT,'Form Rules').click()   #    select Form RUles tab
   
    selenium_driver.find_element(By.CLASS_NAME,'del').click()
   
    
    
    
    ### Add more rules functionality
    
    ## Redirection to Web Page
    ### Create Rule 2 ###
    print'Create rule 2'
   
    #selenium_driver.find_element(By.XPATH, './/*[@id=\'expandThis\']/div/a[7]').click() # click "Rules" icon
   
    selenium_driver.find_element(By.LINK_TEXT,'Form Rules').click()   #    select Form RUles tab
    time.sleep(3)
    selenium_driver.find_element(By.LINK_TEXT,'Create a Form Rule').click()   #    Select "Create a Form Rule"
    #selenium_driver.find_element(By.CLASS_NAME,'dup').click()   #    press "+"
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_FieldName').click()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'Fields\']/li[2]/a').click() #    select "text field" - text from Page 1
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Filter').click()   #    click "contains"
    selenium_driver.find_element(By.LINK_TEXT,'begins with').click()   #    click "begins with"
    #selenium_driver.find_element(By.XPATH,".//*[@id='Conditions']/li[6]/a").click()    #    choosing "begin with"
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Value').clear()
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Condition_TempCondition1_Value').send_keys("Dark")
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Type_Redirect').click() #    redirect to Web Site
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Setting_Redirect').clear()
    selenium_driver.find_element(By.ID,'FormRules_TempRule1_Setting_Redirect').send_keys("http://images4.wikia.nocookie.net/__cb20060520005228/starwars/images/c/c6/Spaceballs_DVD_cover.jpg")
   
    selenium_driver.find_element(By.LINK_TEXT,'Save Form Rules').click()    #    click "Save Form Rules" button
    print '"Form Rules" saved'
   
    ## Show Message
    #### will be next
   
    ####    Navigate to Forms    ####
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[1]/a').click()             #    Navigate to Forms
   
    #### Open Form ####
    selenium_driver.find_element(By.CLASS_NAME,'entries').click()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'first\']/div[2]/a').click() # Create a New Entry
    #selenium_driver.find_element(By.LINK_TEXT,'Create a New Entry').click()
    print '\nForm is Open\n'
    #selenium_driver.get_screenshot_as_file('Form_test_Open_001.jpg')       
    #print'Screenshot added to to TS folder'
   
    ## first Text field
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'Field1\']').clear()
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'Field1\']').send_keys("Dark Helmet") # sent Dark Helmet to first text field
    print 'Dark Helmet is here!'
    ##
    selenium_driver.find_element(By.ID,'nextPageButton').click()
    time.sleep(3)
    selenium_driver.find_element(By.ID,'nextPageButton').click()
    time.sleep(3)
    selenium_driver.find_element(By.ID,'saveForm').click()
   
    
    ####    Navigate to Forms    ####
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[1]/a').click()             #    Navigate to Forms
   
    
    ## delete "Rules -> Form Rules"
    ### Rules ###
    selenium_driver.find_element(By.XPATH, './/*[@id=\'expandThis\']/div/a[7]').click() # click "Rules" icon
    time.sleep(3)
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'wl\']/a').click()   #    select Form Rules tab
   
    selenium_driver.find_element(By.CLASS_NAME,'del').click()
     
    ## Navigate to Forms(Form Manager) and delete tested Form
    ####    Navigate to Forms    ####
    selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[1]/a').click()             #    Navigate to Forms
    selenium_driver.find_element(By.CLASS_NAME,'del').click()
    selenium_driver.find_element(By.ID,'confirmFormDeletion').click()
    print '\nRule deleted'
   
    
    
#     ## Delete Account
#     selenium_driver.find_element(By.XPATH,'.//*[@id=\'menu\']/li[5]/a').click()
#     print'Navigate to Account URL'
#     time.sleep(5)
#     selenium_driver.find_element(By.LINK_TEXT, 'Delete Account').click()
#     time.sleep(5)
#     print '"Delete Account" button pushed'
#     selenium_driver.find_element(By.XPATH, './/*[@id=\'main\']/form/button').click()
#     time.sleep(5)
#     print 'Confirmation: "Account deleted"'
#     selenium_driver.find_element(By.ID, 'Field17_0').click()    # radio button "Would you use Wufoo again?"
#     selenium_driver.find_element(By.ID, 'Field11').click()
#     selenium_driver.find_element(By.ID, 'Field11').send_keys('just tested')    #    sent "sure" text to text box
#     selenium_driver.find_element(By.ID, 'saveForm').click()             #    Click "Submit" button
   
    
    selenium_driver.quit()
   
    print '\n Done!!!'
 
 
if __name__ == '__main__':
    main()
