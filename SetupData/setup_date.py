# Send data to text-box

import datetime

## Data tuday
selenium_driver.find_element(By.ID, "text-box Date").send_keys(time.strftime("%d/%m/%Y")) 

## Data tomorrow
td = datetime.datetime.now() + datetime.timedelta(days=1)
selenium_driver.find_element(By.ID, "text-box Date").send_keys((td.strftime("%m/%d/%Y")))
