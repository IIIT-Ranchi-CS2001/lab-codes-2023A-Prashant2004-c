import math

# Function to calculate the roots of a quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Case 1: If discriminant is zero, one repeated real root
    if discriminant == 0:
        root = -b / (2 * a)
        print(f"The equation has one real repeated root: R1 = R2 = {root}")

    # Case 2: If discriminant is positive, two distinct real roots
    elif discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots: R1 = {root1}, R2 = {root2}")

    # Case 3: If discriminant is negative, two complex roots
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has two complex roots: R1 = {real_part} + {imaginary_part}i, R2 = {real_part} - {imaginary_part}i")

# Example usage
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

find_roots(a, b, c)
