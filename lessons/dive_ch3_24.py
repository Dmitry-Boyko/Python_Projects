"""
mapping list
Example 3.24. Introducing List Comprehesions 

"""
print "\nExample 3.24."

li = [1, 9, 8, 4]
elm = [elem * 2 for elem in li]
print elm
print li

"""
Example 3.25. The keys, values, and items Funtions
"""
print '\nExample 3.25.'

params = {'server': 'mpiligrim', 
          'database': 'master', 
          'uid': 'sa', 
          'pwd': 'secret'}
          
print params.keys()
print params.values()
print params.items()

"""
Example 3.36. List Comprehensions in buildConnectionString, Step by Step
"""
print '\nExample 3.36.'

params = {'server': 'mpiligrim', 'database': 'master', 'uid': 'sa', 'pwd': 'secret'}
k_prnt = [k for k, v in params.items()]
print 'keys in list params: %s' % (k_prnt)

v_prnt = [v for k, v in params.items()]
print 'value in list params: %s' % (v_prnt)

kv_frmt = ["%s = %s" % (k, v) for k, v in params.items()]
print 'keys and values in list param: %s' % (kv_frmt)
