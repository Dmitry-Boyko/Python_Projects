# Verify_element_by_text
        element = 'Deployment Usage and Aging Report'
        selenium_driver.find_element(By.CSS_SELECTOR, '#LAB_CONF_USAGE_AGING_panelTitle')
        if element != u'Deployment Usage and Aging Report':
            print "Text verification Failed: element text is not %r" % element
        else:
            print('Deployment Usage and Aging Report - verified')
