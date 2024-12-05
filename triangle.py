
import math

def calculate_angle(a, b, c):
    
    angle_rad = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    # Convert the angle to degrees
    angle_deg = math.degrees(angle_rad)
    return angle_deg


def find_triangle_angles(a, b, c):
    angle_A = calculate_angle(a, b, c)
    angle_B = calculate_angle(b, a, c)
    angle_C = calculate_angle(c, a, b)
    # return angle_A, angle_B, angle_C
    print("angles are : " , angle_A , angle_B , angle_C)

a = float(input('enter the value of a : '))
b = float(input('enter the value of b : '))
c = float(input('enter the value of c : '))

peri = (a+b+c)
print("perimeter of triangle is : " , peri)

s = (peri)/2
are1 = s*(s-a)*(s-b)*(s-c)
fareac = pow(are1 , 0.5)

find_triangle_angles(a,b,c);

print("area of triangle is : " , fareac)


# print(a1)

