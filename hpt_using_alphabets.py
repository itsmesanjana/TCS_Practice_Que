rows=int(input("Enter the no of rows:"))

for i in range(1,rows+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()