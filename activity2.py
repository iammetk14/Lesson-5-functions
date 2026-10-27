def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("Write a number and get its factorial!"))
if num<0:
    print("Sorry, Factorials are not available for negative numbers.")
elif num==0:
    print("The factorial of both 0 and 1 is 1 only!!")
else:
    print("The factorial of",num,"is", recur_factorial(num))
        
