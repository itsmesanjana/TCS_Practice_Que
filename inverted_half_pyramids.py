#Using * 
rows=int(input("Enter no of rows :"))

for i in range(rows,0,-1):
    print("*"*i)
# Using  numbers
 
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    