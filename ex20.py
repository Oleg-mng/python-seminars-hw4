# Задача 20
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# from solution import Polynomial

def numbers_in_list(list):
    sum_numbers_1 = []
    for i in list:
        if i.isdigit() == True:
            sum_numbers_1.append(i)
    print(sum_numbers_1)
    return sum_numbers_1
    

# def sum_of_lists(list1, list2):
#     sum_of_lists_1 = []
#     for i in list1:
#         sum_of_lists_1=list1+list2


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

numbers_in_list(poly_1)
numbers_in_list(poly_2)

# print(poly_1.split('+'))
# print(poly_2.split('+'))

# print((map(int(poly_1))))

# s = [s for s in str.split(poly_1) if s.isdigit()]
# print(s)
# print((poly_1.split('+'))+ (poly_2.split('+')))


# sentence = 'Extract 100 , 100.45 and 10000 from this string'
# s = [int(s) for s in str.split(poly_1) if s.isdigit()]
# print(s)

# import re

# res = re.split('\W+', poly_2)
# print(res)


# sum_poly = poly_1+poly_2
# print(sum_poly)
# poly=Polynomial([11, 2, 2])
