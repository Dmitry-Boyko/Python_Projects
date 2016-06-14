#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def diff():
    m = int(raw_input('Input first number: '))
    n = int(raw_input('Input seond number: '))

    if m > n:
        print (m - n)
    else:
        print(n - m)
    return m, n

a, b = diff()
c, d = diff()
e, f = diff()

"""
Практическая работа
1. Напишите функцию, которая вычисляет сумму трех чисел и
   возвращает результат в основную ветку программы.
   
2. Придумайте программу, в которой из одной функции
   вызывается вторая.
   При этом ни одна из них ничего не возвращает в основную
   ветку программы, обе должны выводить результаты своей
   работы с помощью функции print().
"""
# Task 1
def my_sum():
    a = int(raw_input('Insert 1st number: '))
    b = int(raw_input('Insert 2st number: '))
    c = int(raw_input('Insert 3rd number: '))

    d = a + b + c
    print d
    return a, b, c

i, f, g = my_sum()
k, h, j = my_sum()

