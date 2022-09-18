# Задача 20
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# from solution import Polynomial

with open('file20.txt', 'w') as data:
    data.write('3*x^2+7*x+9')
with open('file20.1.txt', 'w') as data:
    data.write('5*x^2+3*x+7')

with open('file20.txt', 'r') as f:
    poly_1 = f.read()
    print(poly_1)

with open('file20.1.txt', 'r') as f:
    poly_2 = f.read()
    print(poly_2)

print(poly_1.split('+'))
print(poly_2.split('+'))

# sentence = 'Extract 100 , 100.45 and 10000 from this string'
# s = [int(s) for s in str.split(poly_1) if s.isdigit()]
# print(s)

import nums_from_string

sentence = 'Extract 100 , 100.45 and 10000 from this string'
print(nums_from_string.get_nums(sentence))

# import re

# res = re.split('\W+', poly_2) 
# print(res)


# sum_poly = poly_1+poly_2
# print(sum_poly)
# poly=Polynomial([11, 2, 2])
