import math 

def find_lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

lcm=find_lcm(num1,num2)
print(f"LCM of {num1} and {num2} is {lcm}")