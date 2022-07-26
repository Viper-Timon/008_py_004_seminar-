# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Задайте степень многочлена -> '))
lst=[]
for i in range(0, k+1):
    coef=random.randint(0,100)      #гораздо нагляднее randint(0,5)
    if coef !=0:
        if i == 0:
            lst.insert(0, coef)
        elif i == 1:
            lst.insert(0, f'{coef}x')
        else:    
            lst.insert(0,f'{coef}x^{i}')

for i in range(0,len(lst)):
    
    if i==len(lst)-1:
        print(f'{lst[i]} = 0\n')
    else: print(f'{lst[i]} + ', end='')

