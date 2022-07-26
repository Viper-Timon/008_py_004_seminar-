# 35. (Доп). Даны два файла, в каждом из которых
# находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

path1 = 'Task_HW_05_01.txt'
path2 = 'Task_HW_05_02.txt'


def open_and_modify(path):
    with open(path, 'r') as data:
        for line in data:
            s = line.replace(' ', '').replace(
                '+', ' + ').replace('-', ' - ').replace('=', ' = ').strip().lower()
            # приведение к стандартному виду для выделения в список
            lst = s.split(' ')
    return lst


def find_max_deg(lst):
    max_j = 0
    for i in range(0, len(lst)):
        if len(lst[i]) >= 3:  # проверка на длинну элемента, где есть степень X
            str_x = str(lst[i])
            for j in range(2, 10):  # исправить до 1000
                if f'x^{j}' == str_x[-3:] and max_j < j:
                    max_j = j
    return max_j


lst1 = open_and_modify(path1)
lst2 = open_and_modify(path2)
print(lst1)
print(lst2)

#condition_if_true if condition else condition_if_false
#попробовал тернарный оператор
max_deg = find_max_deg(lst1) if find_max_deg(lst1) > find_max_deg(lst2) else find_max_deg(lst2)


lst_res = []
for i in range(max_deg, -1, -1):
    coef1=0
    coef2=0

    if i == 0 \
        and (lst1[len(lst1)-3]!=0) \
        and (str(lst1[len(lst1)-3])[-1])!='x':
            coef1=int(str(lst1[len(lst1)-4])+str(lst1[len(lst1)-3]))
            print(coef1)

    
    for j in range(len(lst1)-2):    # -2 т.к. "=" и "0" не будут участвовать в вычислениях
        
        s1=str(lst1[j])
        if f'x^{i}' == s1[-3:]:
            coef1=int(s1[0:-3])

    for j in range(len(lst2)-2):
        s2=str(lst2[j])
        if f'x^{i}' == s2[-3:]:
            coef2=int(s2[0:-3])
    print(f'{i} -> {coef1+coef2}')
    



# for i in range(len(lst1),0,-1):

# if f'x^{i}'==':
#     print(i)

# if lst1[i].find('-')==0:
#     print(f'! {i}')
