import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pow(self.radius, 2) * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


try:
    Radius = float(input("Enter the Circle's radius: "))
    Circle = Circle(Radius)

    print(f"Area of the circle: {Circle.area():.2f}")
    print(f"Perimeter of the circle: {Circle.perimeter():.2f}")

except ValueError:
    print("Enter only numbers!")
