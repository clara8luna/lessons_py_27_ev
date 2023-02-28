

# операции на числа

# + -> сложение 
# num1 = 45
# num2 = 12
# result = num1 + num2
# print(result)

#  - -> вычитание
# num1 = 78
# num2 = 45
# print(num1 - num2)

# / -> деление
# num1 = 89
# num2 = 5
# print(num1 / num2)

# // -> целочисленное деление
# num1 = 80
# num2 = 5
# print(num1 // num2)

# * -> умножение
# num1 = 65
# num2 = 9
# print(num1 * num2)

# % -> остаток от деления
# num1 = 7
# num2 = 3
# print(num1 % num2)

# ** -> возведение в степень
# num1 = 5
# num2 = 2
# print(num1 ** num2)

# abs() -> модуль числа (из отрицательного числа сделать положительное)
# print(abs(-19)) # 19
# print(abs(89)) # 89
# print(abs(-2.5) # 2.5

# pow
# 1. возводит число в определенную степень
# 2. возвращает остаток от деления первого результа на 3е число
# print(pow(4, 6))
# print(pow(4, 6, 2)) -> (4 ** 6) % 2

# divmod - принимает два числа и возвращает два числа, первое число - результат целочисленного деления, а второе число остаток от деления
# print(divmod(6, 4))

# round -> округление
# print(round(12.8475678))
# print(round(12.74598364, 3))

# import math
# from math import sqrt
# sqrt -> нахождение квадратного корня числа
# print(dir(math))
# print(math.sqrt(36))

# второй способ нахождения квадратного корня (число ** 0.5)


# a = 9
# b = 10
# c = 11

# Множественное присваивание 
# a, b, c = 9, 10, 11
# print(a, b, c)

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num1 = num3
# print(num1, num2)

# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2

# from math import pi
# r = 6
# p = 2 * pi * r
# s = pi * (r ** 2)
# print(p, s)

b = frozenset('qwerty')
print(b)