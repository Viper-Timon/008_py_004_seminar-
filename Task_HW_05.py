# 35. (Доп). Даны два файла, в каждом из которых
# находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.



def open_and_modify(path):
    with open(path, 'r') as data:
        for line in data:
            s = line.replace(' ', '').replace(
                '+', ' +').replace('-', ' -').replace('=', ' =').strip().lower()
            # приведение к необходимому виду для выделения в список
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

def polynomial_addition(lst1,lst2,max_deg):
    lst=[]
    for i in range(max_deg, -1, -1):  # подсчет коэф-ов в разрезе степенеи
        coef1 = 0
        coef2 = 0

    # Прогон 1го списка
        for j in range(len(lst1)-1):    # -1 т.к. "=0" не будут участвовать в вычислениях
            s1 = str(lst1[j])

            if i == 0:
                if s1[-1] != 'x'\
                        and s1[-3] != 'x':
                    coef1 = int(s1)
            elif i == 1:
                if s1[-1] == 'x':
                    coef1 = int(s1[0:-1])
            else:
                if s1[-3:] == f'x^{i}':
                    coef1 = int(s1[0:-3])

    # Прогон 2го списка
        for j in range(len(lst2)-1):
            s2 = str(lst2[j])

            if i == 0:
                if s2[-1] != 'x'\
                        and s2[-3] != 'x':
                    coef2 = int(s2)
            elif i == 1:
                if s2[-1] == 'x':
                    coef2 = int(s2[0:-1])
            else:
                if s2[-3:] == f'x^{i}':
                    coef2 = int(s2[0:-3])

        coef = coef1+coef2

    #Наполнение результирующего списка    
        if coef <0:
            if i == 0:
                lst.append(coef)
            elif i == 1:
                lst.append(f'{coef}x')
            else:    
                lst.append(f'{coef}x^{i}')

        if coef >0:
            if i == 0:
                lst.append(f'+{coef}')
            elif i == 1:
                lst.append(f'+{coef}x')
            else:    
                lst.append(f'+{coef}x^{i}')

    lst.append('=0')

    return lst

def clean_look(lst): 
    lst_new=[]
    for i in lst:
        i=str(i).replace('+', ' + ').replace('-', ' - ').replace('=', ' = ').strip()
        lst_new.append(i)
    return lst_new


path1 = 'Task_HW_05_01.txt'
path2 = 'Task_HW_05_02.txt'
l1 = open_and_modify(path1)
l2 = open_and_modify(path2)

#condition_if_true if condition else condition_if_false
# попробовал тернарный оператор
max_deg = find_max_deg(l1) if find_max_deg(l1) > find_max_deg(l2) else find_max_deg(l2)

lst_res = polynomial_addition(l1, l2, max_deg)

print(*(clean_look(l1)))
print(*(clean_look(l2)))
print()
print(*(clean_look(lst_res)))

