'''==== Строки ==='''
# строки -> неизменяемый тип данных, который представляет из себя последовательность символовб, заключенных в кавычки

# id()-> возвращает номер ячейки памяти

# a = '5'
# b = 5
# print(id(a))
# print(id(int(a)))
# print(id(b))
 
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))

# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)

# string = 'строка с одинарными кавычками'
# string2 = "строка с двойными кавычками"
# # string =' error"
# string4 = "Don't"
# string5 = '"Makers"'
# print(string4)

# string6 = '''
# hkdjhgkjhsj
# jfhgkdfjjkd
# jfngkjdkjgd
# '''
# print(string6)

# len() -> возвращает кол-во символов в строке
# print(len(string6))
# print(len(78745638)) # error

'''======= Экранизация строк ========'''
# '\символ'
'\n' # -> перенос на следующую строку 

# a = 'hello \nworld'
# print(a)

'\t' # -> табуляция
# a = 'hello\tworld'
# print(a) # hello   world

'\\' # -> для отображения '\'
# a = 'hello \\'
# print(a)

'\'' # -> для отображения '
"\"" # -> для отображения "
'\r' # -> возвращает каретки в начало строки
# print('Makers \rLab') # Labers 

'\v' # -> переносит на новую строку со смещением вправо на длину предыдущей 
# print('hello\vworld')

'\a' # -> гудок встроенного в систему динамика
# print('hello\a')

# конкатенация строк -> склеивание строк
# a = 'hello'
# b = 'world'
# print(a + b)

# Дублирование строк
# print(a * 5)

"""====== Форматирование строк (Динамическая строка) ======="""

# 1. % 
# 2. .format()
# 3. f - строки 

# 1
# name = input('Введите имя: ')
# print('Hello, %s' %name)

# 2
# name = input('name: ')
# name2 = input('name2: ')
# print('hello, {}, {}'.format(name, name2))

# 3 интерполяция
# name = input('name: ')
# name2 = input('name2: ')
# print(f'Hello {name}, {name2}')

# print(dir('s'))

"""====== Метроды строк ======"""
# методы -> это функции, к которым мы обращаемся через точку

# Методы на is
# s.isdigit() -> проверяет, состоит ли строки только из чисел (True/False)
# s.isalnum() -> только из букв и чисел 
# s.isalpha() -> только из букв
# s.islower() -> все ли символы в нижнем регистре
# s.isupper() -> все ли символы в верхнем регистре
# s.isspace() -> состоит ли строка из неотображаемых символов (пробел, '\n' ...)

# lower() -> переводит целую строку в нижний регистр
# print('FHDJKHHBHDFB'.lower())
# upper() -> переводит целую строку в верхних регистр
# print('fjkdbzshjzbvd'.upper())

# .swappercase() -> переводит символы в противоположный регистр
# print('FHDJKjgfkj'.swapcase())

# .title() -> переводит первую букву каждого слова в верхний регистр
# print('hello world'.title())

# .capitalize() -> Переводит первый символ в верхний регистр
# print('hello world'.capitalize())

# .strip() -> убирает пробелы в начале и конце строки
# print('        hello world       '.strip())
# .lstrip() -> убирает слева
# .rstrip() -> убирает справа

# .replace(old, new, [count]) -> меняет old на new определенное кол-во раз count
# print('ha ha ha ha'.replace('ha', 'new', 2))

# .split(разделитель) -> делит строку по разделителю, возвращает список (массив

# print('hello py27 kjdfk jkfd'.split())
# a = 'hjdfj jdkj jdfkjn'
# list_ = a.split()
# print(list_)

# разделитель.join(iterable) -> соединяет строку по разделителю
# print(' '.join(list_))

# .startswith(string) -> рповеряет начинается ли строка с string 
# a = 'hello world' 
# print(a.startswith('H'))

#  .endswith(string) -> провер]ет заканчивается ли строка на string
# a = 'hello world' 
# print(a.endswith('H'))

# .count(string) -> считает кол-во вхождений подстроки в строку
# a = 'hello'
# print(a.count('l'))

"""====== Индекс ======="""
# индекс - порядковый номер элемента
'hello'
#01234

a = 'hello world'
# print(a[0])
# print(a[-1]) # последний элемент

'''срезы'''
# print(a[0:1])
# print(a[::2])
# a[start:stop:step] (по индексу) -> нахождение подстроки, начиная от start и заканчивая до stop (stop не включительно), step - через какой элемент записывать

# a = 'hello world'
# print(a[::-1]) # переворачивает строка 

