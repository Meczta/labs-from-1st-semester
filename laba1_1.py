a = float(input('Введите значение a:'))
b = float(input('Введите значение b:'))
znak = input('Введите знак:')
if znak == '+':
  print(a + b)
elif znak == '-':
  print(a - b)
elif znak == '*':
  print(a * b)
elif znak == '/':
  print(a / b)
else: print('Выберете другое значение')