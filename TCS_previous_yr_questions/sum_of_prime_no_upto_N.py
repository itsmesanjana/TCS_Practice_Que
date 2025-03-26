def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sum_of_primes(N):
    return sum(n for n in range(2,n+1) if is_prime(n))

n=int(input("Enter a number: "))
print("Sum of prime numbers up to ",n,"is:",sum_of_primes(n)) 