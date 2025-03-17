# Given a number N. Find its unique prime factors in increasing order.
 

# Example 1:

# Input: N = 100
# Output: 2 5
# Explanation: 2 and 5 are the unique prime
# factors of 100.
# Example 2:

# Input: N = 35
# Output: 5 7
# Explanation: 5 and 7 are the unique prime
# factors of 35.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_prime_factors(n):
    factors=[]
    for i in range(2,n+1):
        if n%i==0 and is_prime(i):
            factors.append(i)
    return factors

n=int(input("Enter number: "))
print("The prime factors of given number are ",all_prime_factors(n))