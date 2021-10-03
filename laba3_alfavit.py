sort = str.lower(input('Введите строку:'))
splsort = sort.split()
a = set(splsort)
dr = str(a)
e = ''
for i in sorted(a):
    e += ' ' + i
print(e)
d={}
for char in set(dr):
    d[char]=dr.count(char)
print(d)
