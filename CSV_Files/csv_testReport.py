### csv_generator.py
import csv
import sys

def csv_File():
    with open('test_report.csv', 'w') as csvfile:
        test_writer = csv.DictWriter(csvfile, delimiter = ',')
        test_writer.writerow(['Test Case'] + ['Result'])

### File "test_engine"
from csv_generator import csv_File

class address_book():
    def addressBook(self, selenium_driver):
        csvFile = csv_File()
        try:
            selenium_driver.find_element(By.ID, "userAcctTab_MainMenu").click()
            selenium_driver.find_element(By.LINK_TEXT, "Contacts").click()
            print('AddressBook URL selected')
            test_writer = csv.writer(csvFile, delimiter=',',  quoting=csv.QUOTE_MINIMAL) #quotechar='|',
            test_writer.writerow(['\nNavigate to AddressBook'] + ['Pass'])

        except:
            traceback.print_exc()
            test_writer = csv.writer(csvFile, delimiter=',',  quoting=csv.QUOTE_MINIMAL) #quotechar='|',
            test_writer.writerow(['\nNavigate to AddressBook'] + ['Fail'])
