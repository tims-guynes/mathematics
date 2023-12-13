from math import pi
from basic_operations import *

def circle(radius):
    area = multiply(exponent(radius, 2), pi)
    return area

def triangle(height, base):
    #area is equal to the base times the height divided by 2
    denominator = multiply(height, base)
    area = divide(denominator, 2)
    return area

print(triangle(4, 5))
print(circle(8))