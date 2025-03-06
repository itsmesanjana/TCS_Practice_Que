#FULL PYRAMID USING STAR AND NUMBERS

rows = int(input("Enter the number of rows: "))

for i in range(rows,0,-1):
    print(" " * (rows - i) + "* " * i)

#Using numbers..

for i in range(rows,0,-1):

    spaces=" "*(rows-i)
    numbers=" ".join(str(j) for j in range(1,i+1))
    print(spaces+numbers)