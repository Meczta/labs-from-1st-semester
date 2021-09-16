a = float(input('give me a'))
b = float(input('give me b'))
c = float(input('give me c'))
bl = float(b ** 2 - 4 * a * c)
if bl > 0:
    result_1 = float(-b + bl ** 0.5 // (2 * a))
    result_2 = float(-b - bl ** 0.5 // (2 * a))
    print('x1 =', result_1)
    print('x2 =', result_2)
elif bl == 0:
    result_3 = - b / 2 * a
    print('x1=', result_3)
else: print('discriminant menshe 0, rozwiazkiv net')