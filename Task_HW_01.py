# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141



def pi_near_rounder(x):
    p = float(103993/33102)
    pr = p*(10**x)//1           # можно и int
    pr = float(pr/(10**x))
    return pr

d = int(input('Задайте точность вычисления числа Пи -> '))
print(pi_near_rounder(d))