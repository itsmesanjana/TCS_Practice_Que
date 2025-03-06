# Pascal's Triangle is a triangular arrangement of numbers where:

# The first row always starts with 1.
# Each number inside the triangle is the sum of the two numbers directly above it.
# The edges of the triangle always have 1.
# The third row has 1 2 1 because:
# 2 is the sum of 1 + 1 from the row above.
# The fourth row has 1 3 3 1 because:
# 3 is the sum of 1 + 2 from above.
# The next 3 is the sum of 2 + 1.

# def pascal_triangle(n):
#     for i in range(n):
#         print(" "*(n-i),end=" ")
#         num=1
#         for j in range(i+1):
#             print(num,end=" ")
#             num=num*(i-j)//(j+1) 
#         print() 
def pascal_triangle(n):
    for i in range(n):
        print(" "*(n-i),end=" ")
        num=1
        for j in range(i+1):
            print(num,end=" ")
            num=num*(i-j)//(j+1)
        print()
rows=int(input("Enter the number of rows: "))
pascal_triangle(rows)
