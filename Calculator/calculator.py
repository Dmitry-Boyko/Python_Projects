
class calculator():
    
    def add(self, x, y):
        return x + y
        
    def substract(self, x, y):
        return x - y
        
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

    print('Calculator operation')
    print('1. Addition')
    print('2. Substract')
    print('3. Multiplay')
    print('4. Divide')
    print('0. Exit')
    
    choice = int(raw_input('Please enter expecting operation: '))
    
    num1 = float(raw_input('Please inout First number: >  '))
    num2 = float(raw_input('Please input Second number: > '))

    
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
        
    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1, num2))
        
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
        
    elif choice == '4':
        print(num1, ":", num2, "=", divide(num1, num2))
    
    elif choice == '0':
        exit()
        
    else:
        print("Invalid input")


calculator()
