# Задача 19
# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите натуральную степень k: '))
mylist = []
for i in range(k+1):
    a = random.randint(0, 100)
    b = a, 'x^', i
    b = ''.join(map(str, b))
    # print(b)
    mylist.append(b)
mylist.reverse()
# print(mylist)
print('+'.join(map(str, mylist)))
g = '+'.join(map(str, mylist))
with open('file19.txt', 'w') as data:
    data.write(g)
