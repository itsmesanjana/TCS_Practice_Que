# Body Mass Index

def BMI(h,w):
    return round((w/h**2),2)

h=float(input("Enter your height in meters:"))
w=float(input("Enter your weight in kg:"))
print("Welcome to BMI calculator:")

bmi=BMI(h,w)
print("Your BMI is:",bmi)

if bmi<=18.5:
    print("your are underweight.")
elif 18.5 <bmi<=24.9:
    print("your weight is normal")
elif 25< bmi<=29.29:
    print("your are overweight.")
else:
    print("You are obese.")