#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Практическая работа
1. Создайте словарь, связав его с переменной school, 
   и наполните его данными, которые бы отражали количество 
   учащихся в десяти разных классах 
   (например, 1а, 1б, 2б, 6а, 7в и т.д.).
2. Узнайте сколько человек в каком-нибудь классе.
3. Представьте, что в школе произошли изменения, внесите их в словарь: 
   ◦ в трех классах изменилось количество учащихся; 
   ◦ в школе появилось два новых класса;
   ◦ в школе расформировали один из классов.
4. Выведите содержимое словаря на экран.

"""

# School class 1A
a1 = {'1a_st_01': 'ivanov',
      '1a_st_02': 'petrov',
      '1a_st_03': 'sidorov'}
# School class 1B
b1 = {'1b_st_01': 'sidorova',
      '1b_st_02': 'kuskina',
      '1b_st_03': 'sinicina'}
# School class @a
a2 = {'2a_st_01': 'dilda',
      '2a_st_02': 'senechkin'}

school = a1, b1, a2

# Count number of students in all classes
AllStudents = len(a1) + len(b1) + len(a2)
print "1. \n   All number of students in school: %d" % AllStudents
"""
Result:
1. 
   All number of students in school: 8
"""
# Count number of students by school>class
print '2.'
print "   Number of Students in 1a klass: %d" % len(a1)
print "   Number of Students in 1b class: %d" % len(b1)
print "   Number of Students in 2a class: %d" % len(a2)
"""
Result:
2.
   Number of Students in 1a klass: 3
   Number of Students in 1b class: 3
   Number of Students in 2a class: 2
"""
print '\n'

# Print last name of students from "1b" class
keys = b1.keys()
values = b1.values()
print "\nLast Names students from \"1B\" class: ", values
for k, v in b1.iteritems():
    b1[k] = v.split()
    print v
"""
Result:
Last Names students from "1B" class:  ['sidorova', 'kuskina', 'sinicina']
sidorova
kuskina
sinicina
"""

# Add student to 2A class
print "\nAdd new student to 2A class"
a2['2a_st_03'] = 'soloviova'
print "Number of Students in 2A class now: %d" % len(a2)

print "\nClass 1B contain next last names of students"

# Loop and display tuple items.
for k, v in b1.items():
    #print(k, ' ==> ', v)
    print v
"""
Result:
Class 1B contain next last names of students
['sidorova']
['kuskina']
['sinicina']
"""
# Merge two school classes 1a + 1b true "dict" method
a1b1 = dict(a1.items() + b1.items())
print "\nMerged \"1A\" and \"1B\" classes:\n", a1b1

print "\nName of All students in new/merged class: "
for k, v in a1b1.items():
    print "Last Name; ", v
print '\n'
"""
Result:
\nLast Name;  ['sidorova']
Last Name;  ['kuskina']
Last Name;  ['sinicina']
Last Name;  sidorov
Last Name;  petrov
Last Name;  ivanov
"""

# Merge two school classes 1a + 1b true "update" method
a1.update(a2)
for k, v in a1.items():
    print "1A, Last Name; ", v
"""
Result:
1A, Last Name;  sidorov
1A, Last Name;  petrov
1A, Last Name;  ivanov
1A, Last Name;  senechkin
1A, Last Name;  soloviova
1A, Last Name;  dilda
"""

print '\n4.', '\n  ', "All info: ", school
