import math

def square(side):
    return math.ceil(side * side)

side = 4.3
result = square(side)
print(f'Площадь квадрата со стороной {side}: {result}')
