def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

number1=int(input("Enter First number:"))
number2=int(input("Enter Second number:"))
print("Sum:",add(number1,number2))
print("Difference:",subtract(number1,number2))
print("Product:",multiply(number1,number2))
print("Quotient:",divide(number1,number2))