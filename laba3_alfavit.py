sort = str.lower(input('Введите строку:'))
print('Выберите действие: \n 1:сортировать слова \n 2:показать количество букв')
vibor = input(':::')
splsort = sort.split()
a = set(splsort)
e = ''
d = {}
for i in sorted(a):
    if len(i) > 3:
        e += ' ' + i
    else:
        continue
if vibor == '1':
    print(e)
elif vibor == '2':
    for char in set(e):
        if char != ' ':
            d[char] = e.count(char)
        else:
            continue
    print(d)
else:
    print('Вы ввели недопустимое значение')
