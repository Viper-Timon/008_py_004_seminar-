# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Задайте степень многочлена -> '))
lst = []
for i in range(0, k+1):
    coef = random.randint(-100, 100)     # для правдоподобности примеров
    if coef != 0:
        if i == 0:
            lst.insert(0, coef)
        elif i == 1:
            lst.insert(0, f'{coef}x')
        else:
            lst.insert(0, f'{coef}x^{i}')

for i in range(0, len(lst)):
    str_f = str(lst[i]).replace('-', '- ')  # для читабельности  
    if i == 0:
        print(f'{str_f}', end=' ')

    else:
        if str_f.find('-') == 0:
            
            print(f'{str_f}', end=' ')
        else:
            print(f'+ {str_f}', end=' ')
print(f'= 0\n')
