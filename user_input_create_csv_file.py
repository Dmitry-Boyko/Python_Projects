import time

time_now = time.strftime("%Y-%m-%d %H:%M:%S")
'''
while True:
        print("write number between 1 and 4:\n ")
        user_input = str(raw_input())
        print("Input: " + user_input)
        if user_input == u'one':
            print("1")
        elif user_input == u'two':
            print("2")
        elif user_input == u'three':
            print("3")
        elif user_input == u'four':
            print("4")
        else:
            print("wrong input")
'''



# def user__input(elements):
num = {
    'one': "1", '1': "1",
    'two': '2', '2': '2',
    'three': '3', '3': '3',
    'four': '4', '4': '4',
    'one two three four': '1234', '1234': '1234',
    'one23four': '1234', '1234': '1234',
    'four three two one': '4321', '4321': '4321',
    'two three one four': '2314', '2341': '2341',
    'one four two three': '1423', '1423': '1423',
}

f = open('visa_number.csv', 'a')

while True:
    print("Write number between 1 and 4 or xxxx - values:")
    print('For EXIT select "x" key and pres Enter button\n')
    user_input = str(raw_input())

    if user_input in num:
        print 'You\'ve selected', num[user_input]
        #f.write(num[user_input] + ', ')
        f.writelines(str(time_now) + "\n" + num[user_input] + ',')
    elif user_input == u'x':
        break
    else:
        pass

f.close()
