selenium_driver.find_element(By.XPATH, "<XPATH>").click() # "Manual" icon selected
file = open("Path to file.txt",'r')
for line in file:
  selenium_driver.find_element(By.XPATH, "<XPATH>").send_keys(line)
file.close()

'''
tb_blah = selenium_driver.find_element(By.XPATH, "<XPATH>")
file = open("C:\Dmitry\Docum\Test_csv's\manual.txt",'r')
for line in file:
tb_blah.sendkeys(line)
'''
