# Задача 18
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной
# последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

mylist = [1, 1, 2, 3, 4, 5, 5]

# for i in range(len(mylist)):
#     for j in range(len(mylist)):
#         if mylist[i] == mylist[j]:
#             mylist.remove(mylist[i])
#             mylist.remove(mylist[j])
# print(mylist)

helplist=mylist
for i in mylist:
    for j in mylist:
        if i == j:
            helplist.remove(j)
            helplist.remove(j)
print(helplist)


