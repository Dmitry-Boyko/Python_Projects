#!/usr/bin/env python2

company = 'Platfora='
j = "Front End QA Engineer"
f = 'full time'

def survey():
    print 'Hello, \nwell if you need help, possible I can do it for you, but before go to \
    next step I would like ask one simple questions:'
    for job in company:
        print'Is this', f, 'job for', j,'?'
        answer = str(raw_input('Please type "Y" or "N": '))
        if answer == u'y':
            print 'Excellent!\nPlease email me expected annual salary. \
            \nEmail: 8184160900.cell@gmail.com\nThank you!'
            break
        else:
            print 'Oh-h, that was wrong answer! \nSorry, I can\'t take this job for now.'
            break
             
survey()
