def monkeys_left_on_tree(n,m,p,k,j):
    monkeys_fed=0
    while n>0 and (m>=k or p>=j or (m>0 and p>0)):
        if m>=k:
            m-=k
        elif p>=j:
            p-=j
        elif m>0 and p>0:
            m,p=0,0
        else:
            break
        monkeys_fed+=1
        n-=1
    return n

# Input values from user
n = int(input("Enter total number of monkeys: "))
m = int(input("Enter total number of bananas: "))
p = int(input("Enter total number of peanuts: "))
k = int(input("Enter number of bananas a monkey can eat: "))
j = int(input("Enter number of peanuts a monkey can eat: "))

print("Monkeys left on the tree:", monkeys_left_on_tree(n, m, p, k, j))