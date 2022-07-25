# 1. Задайте строку из набора чисел.
# Напишите программу, которая покажет
# большее и меньшее число.
# В качестве символа-разделителя
# используйте пробел.

# str1 = '234 65 256'
# srt2 = ''
# for i in str1:
#     if i.isdigit == 1:
#         str2 += str(i)
# print(str2)


str1 = '234 54 654'
list_1= str1.split()
max = int(list_1[0])
min = int(list_1[0])

for i in list_1:
    if int(i)>max:
        max= int(i)
    if int(i)<min:
        min = int(i)
print(f'max = {max}')
print(f'min = {min}')


