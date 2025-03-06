#factorial of a number using recursion 

def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=int(input("Enter a number"))

if num<0:
    print("Sorry,factorial does not exisit for -ve number")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("the factorial of",num,"is",recur_factorial(num))