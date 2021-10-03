sort = str.lower(input('Введите строку:'))
splsort = sort.split()
e = ''
for i in sorted(splsort):
    e += ' ' + i
print(e)
d={}
for char in set(sort):
    d[char]=sort.count(char)
print(d)
