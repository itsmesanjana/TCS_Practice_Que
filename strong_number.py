import math  # Importing math module for factorial calculation

# Function to check if a number is Strong
def is_strong_number(num):
    temp = num
    sum_of_factorials = 0
    
    while temp > 0:
        digit = temp % 10  # Extract last digit
        sum_of_factorials += math.factorial(digit)  # Add factorial of digit
        temp //= 10  # Remove last digit
    
    return sum_of_factorials == num  # Check if sum equals the number

# Taking input from user
number = int(input("Enter a number: "))

# Checking and printing result
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is NOT a Strong Number.")
