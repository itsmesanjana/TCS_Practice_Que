#  Find the Factorial of a Number
num=int(input("Enter a number:"))
fact=1
if num<0:
    print("Factorial does not exist for -ve no")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f'The factorial of {num} is {fact}')