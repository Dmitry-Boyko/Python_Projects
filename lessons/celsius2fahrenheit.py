def c2f(cels):
    tf = tc * 1.8 + 32
    return tf
    
tc = input("Please add Temperature in Celsius: ")

print(c2f(tc))