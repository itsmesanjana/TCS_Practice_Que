#  Print the Fibonacci sequence
nterms=int(input("How many terms?"))

n1,n2=0,1
count=0

if nterms<0:
    print("Plz valid no")
elif nterms==1:
    print("Fibonacci seq upto",nterms,":")
    print(n1)
else:
    print("Fibonacci seq :")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        
        