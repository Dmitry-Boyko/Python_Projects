def main():

    #selenium_driver = driver()

    #d = driver()

    try:
        main_event_ilt_online.main()
    except Exception, err:
        sys.stderr.write('ERROR: %sn' % str(err))
        
    try:
        main_tms__template.main()
    except Exception, err:
        sys.stderr.write('ERROR: %sn' % str(err))
        

if __name__ == "__main__":
    main()
