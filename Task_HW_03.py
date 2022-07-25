# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.




# lst = input('Введите числа через пробел').split(' ') # для пользовательского ввода

import random

def fill_list(size: int, interval: int):
    lst=[]
    for i in range(size):
        lst.append(random.randint(1, interval))
    return lst

def find_unq_elem(lst1):
    lst2=[]
    for i in lst1:
        count=0
        # print(i, end=" ") # для проверки
        for j in lst1:
            if i==j:
                count+=1
        # print(f'- {count} раз') # для проверки 
        if count==1: lst2.append(i)
    return lst2

a = fill_list(15, 10)
b = find_unq_elem(a)
print(a)
print(b)



