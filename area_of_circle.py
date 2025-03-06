import math  # Importing math module for π (pi)

def circle_area(radius):
    return math.pi * radius ** 2

r = float(input("Enter the radius of the circle: "))

area = circle_area(r)
print(f"Area of the circle with radius {r} is {area:.2f}")
