"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """


def power(base, exponent):
    if (exponent == 1):
        return base
    if (exponent != 1):
        return (base * power(base, exponent - 1))


base = int(input("Введите основание: "))
exponent = int(input("Введите показатель степени: "))
print("Возведение в степень равно: ", power(base, exponent))
