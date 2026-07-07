import math
def circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius **2
    return area, circumference

print(circle(2))