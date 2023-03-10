''' Логические вырожения и опреаторы Python. NoneType, Условные оператооры. Тернарные операторы '''

'''Boolean Type'''
# неизменяемый тип данныхб имеет всего лишь два значения True/False

# print(bool(0)) # False
# print(bool(-9)) # True
# print(bool('')) #False
# print(bool(' ')) #True
# printt(bool(True)) # True

''' Логические вырожения - выражения результатом вычесления, которых является True/False'''

# 4 == 2 # False

''' Логические операторы '''
# == -> сравнение
# 5 == 5 #True
5 == 4 #False
# '5' == 5 #False

# != -> не равно
5 != 5 #True
5 != 4 #False

# > -> Больше
5 > 4 #True
5 > 10 #False

# < -> Меньше
5 < 8 #True
5 < 4 #False

# >= -> больше или равно
5 >= 4 #True
5 >= 6 #False

# >= -> меньше или равно
5 <= 8 #True
5 <= 4 #False

'''======= and or not ========'''
# 1. and -> логическое и
# 2. or -> логическое или
# 3. not -> логическое отрицание

'''
and      операторы используются для 
or       объединения логических выражений
'''

a = 7
b = 5

a == 5 and b == 5 #False (левая часть False, правая True -> false )
a == 7 and b == 5 #True (обе части true -> true)
a == 4 and b == 4 #False (обе части false -> false)

a == 5 or b == 5 #True (важно, чтобы хоть одна часть выражения была true)
a == 7 or b == 5 #True 
a == 4 or b == 4 #False

'''превращает правду в ложь, а ложь в правду'''
# print(not True)
# print(not False)

not a == 7 #False
not b == 7 #True


'''Операторы идентификации'''
# 1. in -> проверяет наличие элемента
# 2. сравнение
    # == -> сравнение по значению
    # is -> сравнение по ячейкам памяти


# a = 'hello'
# if 'e' in a:
#     print(True)

'''None Type'''
# неизменяемый тип данных, имеет только одно значение None
# print(bool(None)) 
# print(bool('None'))


'''======= Условные операторы ========'''
# нужны для того, чторбы при разных входных данных код выполнялся по разному

# 1
# if условие:
#     тело
    # тело будет работать, если условие верно

# 2
# if условие1:
#     тело1
# else:
#     тело2 будет работать, когда условие1 не верно


# 3
# if условие1:
#     тело1
# elif условие2:
#     тело2 будет работать, когда условие1 не верно
# else:
#     тело3 будет работать, когда условие1 и условие2 не верно

# в одной конструкции -> только один if
# в одной конструкции -> сколько угодно elif
# в одной конструкции -> только один else

# age = int(input())
# if age >= 18: 
#     print('yes')
# else: 
#     print('No')

# num = int(input('Введите число: '))
# if num % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# num = int(input('Введите число: '))
# if num == 0:
#     print('равен нулю')
# elif num > 0:
#     print('положительное')
# else:
#     print('отрицательное')

'''====== Тернарные операторы ======'''
# условие в одну строку

'''синтаксис'''
# тело1 if условие else тело2
# a = 6
# print('hello' if a == 5 else 'bye')

# result = 'hello' if a == 5 else 'bye'
# print(result)


'''===== Маржовые операторы ====='''
# позволяет как присвоить, так и вернуть значение в одном вырожении
# := 
# num = 7
print(num:=7)
print(num+7)

# num = int(input('Введите число: '))
# if (num % 5 == 0) and (num % 3 == 0):
#     print('FizzBuzz')
# elif (num % 3 == 0):
#     print('Fizz')
# elif (num % 5 == 0):
#     print('Buzz')
# else:
#     print(num)

