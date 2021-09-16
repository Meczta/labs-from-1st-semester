import math
x = float(input('Введите x:'))
if - math.pi <= x <= math.pi:
    print(math.cos(3 * x))
elif x < - math.pi:
    print(x)
elif x > math.pi:
    print(x)