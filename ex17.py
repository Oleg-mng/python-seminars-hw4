# Задача 17
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = int(input('задайте натуральное число N: '))
c=n
mnozh = [2, 3, 5, 7]
res=[]
while n != 1:
    for i in range(len(mnozh)):
        if (n % mnozh[i]) == 0:
            n = n/mnozh[i]
            # print(mnozh[i])
            res.append(mnozh[i])
print('список простых множителей для числа', c, ':', res)

# for i in range(len(deliteli)):
#     if (n % deliteli[i]) == 0:
#         res.append(i)
#         n = n/deliteli[i]
#         print(deliteli[i])
# print('список простых множителей для числа', n, ':', res)
