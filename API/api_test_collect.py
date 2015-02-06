'''
author: dmitry
Created: November 25, 2014

test_collectors.py

Defines Test Operations
'''

import urllib2
import requests
import simplejson as json


def main():
    #collector_get_by_collector_id()
    collectors_create()
    print 'Done!!!'

def collector_get_by_collector_id():
    url = 'http://mt1-pyweb01:7010/v1/collectors/23999929?user_id=57505886'
    data = None # parameter for start
    result_response = get_data(url, data)
    print 'Result for the collector_get:'
    if result_response is not None:
        result = json.dumps(json.loads(result_response.read()), sort_keys=False, indent=4)
        print result
        my_dict = json.loads(result)
        print my_dict["status"]
        print my_dict["weblink"]["url"]
    else:
        print None

def collectors_create():
    url = 'http://mt1-pyweb01:7010/collectors/create'
    # Baratheon\u2665
    data = { "user_id": '<user ID here>',
                 "collector_type": "Email",
                 "recipients":
                     [ { "custom_value1": "94301",
                         "first_name": "Stannis",
                         "last_name": "Baratheon",
                         "email": "dmitryb@surveymonkey.com"},
                       { "custom_value1": "94401",
                         "first_name": "Joffrey",
                         "last_name": "Baratheon",
                         "email": "dmitryb@surveymonkey.com"},
                       {"email": "xxxxx@surveymonkey"} ],
                 "collector_title": "Dmitry's email invite",
                 "eventbrite": True,
                 "configuration_status_id": 4,
                 "survey_id": '<here should be survey ID>'}
    result_response = get_data(url, data)
    print 'Result for the get_user_info:'
    if result_response is not None:
        '''
         # json.dumps take a python object(usualy a dictionary) and serialize \
         # it to JSON.json.loads will take a JSON string and turn it into a python dictionary
        '''
        print json.dumps(json.loads(result_response.read()), sort_keys=False, indent=4)
    else:
        print None

def get_data(url, data):
    response = None
    headers = {'Content-Type':'application/json; charset=UTF-8'}
    print 'url:', url
    if data is not None:
        request = urllib2.Request(url=url, data=json.dumps(data), headers=headers)
    else:
        request = urllib2.Request(url=url, headers=headers)
    try:
        response = urllib2.urlopen(request)            
    except urllib2.HTTPError as e:
        print 'Server couldn\'t fulfill the request.'
        print '   Error code: ', e.code, e.fp.read()
        print '   Request: ', request.get_full_url()
        print '   Headers: ', request.headers
        print '   Data: ', request.data
    except urllib2.URLError as e:
        print 'Failed to reach a server.'
        print '   Reason: ', e.reason
        print '   Request: ', request.get_full_url()
        print '   Headers: ', request.headers
        print '   Data: ', request.data
    return response

if __name__ == "__main__":
    main()
