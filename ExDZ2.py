# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import math


def sum_Fraction(number_frac_1, number_frac_2):
    sum_frac = [int(number_frac_1[0]) * int(number_frac_2[1]) \
                       + int(number_frac_2[0]) * int(number_frac_1[1]),
                int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(sum_frac[0], sum_frac[1])
    sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]
    print('Cумма дробей = ', sum_frac[0], '/', sum_frac[1])


def mult_Fraction(number_frac_1, number_frac_2):
    mult_frac = [int(number_frac_1[0]) * int(number_frac_2[0]),
                 int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(mult_frac[0], mult_frac[1])
    mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]
    print('Произведение дробей = ', mult_frac[0], '/', mult_frac[1])


def Main():
    number_frac_1 = str(input('Введите первое число вида a/b - ')).split('/')
    number_frac_2 = str(input('Введите второе число вида a/b - ')).split('/')
    sum_Fraction(number_frac_1, number_frac_2)
    mult_Fraction(number_frac_1, number_frac_2)


Main()

import fractions
str1 = str(input('Введите дробь вида 3/4 : '))
str2 = str(input('Еще одну : '))
first = str1.split('/')
second = str2.split('/')
summa = str(int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])) + '/' + str(int(second[1]) * int(first[1]))
mult = str(int(first[0]) * int(second[0])) + '/' + str(int(first[1]) * int(second[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')
