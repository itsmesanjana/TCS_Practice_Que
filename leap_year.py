# Check Leap Year
yr=int(input("Enter a yr:"))
if (yr%400==0) and (yr%100==0):
    print("{0} is a leap yr".format(yr))
elif (yr%4==0) and (yr%100!=0):
    print("{0} is a leap yr".format(yr))
else:
    print("{0} is not a leap yr".format(yr))