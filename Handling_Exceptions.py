import os
import sys
from event_ilt_online               import main_event_ilt_online
from create_new_template            import main_tms__template

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()



def driver():
    selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(30)
    selenium_driver.delete_all_cookies()
    return selenium_driver

def main():
    try:
        main_event_ilt_online.main()
    except Exception, err:
        sys.stderr.write('ERROR: %sn' % str(err))
#### .... ####        
    try:
        main_tms__template.main()
    except Exception, err:
        sys.stderr.write('ERROR: %sn' % str(err))
        
    display.stop()

if __name__ == "__main__":
    main()
