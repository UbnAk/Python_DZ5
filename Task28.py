# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4


def sum_int(a,b):
    if b == 0:
        return a
    return sum_int(a+1, b-1)
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
print(sum_int(number_1, number_2))