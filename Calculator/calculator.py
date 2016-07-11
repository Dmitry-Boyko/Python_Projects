
class calculator():
    
    def add(x, y):
        return x + y
        
    def substract(x, y):
        return x - y
        
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y

    # input first number
    num1 = float(raw_input('Please inout First number: >  '))

    
    # input second number
    num2 = float(raw_input('Please input Second number: > '))
    
    print('Calculator operation')
    print('1. Addition')
    print('2. Substract')
    print('3. Multiplay')
    print('4. Divide')
    print('0. Exit')
    
    choice = raw_input('Please enter expecting operation: ')
    
    # action
    if choice == '1':
        print num1, "+", num2, "=", add(num1, num2)
        
    elif choice == '2':
        print num1, "-", num2, "=", substract(num1, num2)
        
    elif choice == '3':
        print num1, "*", num2, "=", multiply(num1, num2)
        
    elif choice == '4':
        print num1, ":", num2, "=", divide(num1, num2)
    
    elif choice == '0':
        print('Thank you.')
        quit()
        
    else:
        print("Invalid input")
        
calculator()
