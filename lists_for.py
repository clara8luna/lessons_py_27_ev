'''Списки, Методы списков. Цикл for. Кортеж'''

# список - изменяемый, индексируемый, упорядоченный, итерируемый. 
# [] -> литералы (выражения, которые создают объекты определенного типа данных)

# list_ = [1, 2, 3, 'hello', [1, 2, 3, 4], {1:'a'}]
# print(list_[4][0])
# print(list_[5][1])

# names = input('Ведите имена через пробел: ').lower().split()
# guest = input('Ведите имена через пробел: ').lower()
# if guest in names: 
#     print('вы приглашены')
# else:
#     print('иди спать')

'''Создание списков'''
# 1. list(iterable) 
# a = 'hello'
# print(list(a))
# 1.2 range() -> возвращает последоватедьность элементов
# print(list(range(1,10,2))) 
# 2. [] -> литералы
# print(type(list))
# list_ = [1] * 6
# print(list_)

# range -> возвращаем послед-ть чисел, по умолчанию начинает с 0, последовательность каждый раз увеличивается на 1 и останавливается перед заданным числом (stop)

''' Методы списков '''
# del -> удаление элемента
# list_ = [1, 2, 3, 4]
# del list_[0]
# print(list_)

# .append() -> отвечает за добавление элемента в конец списка
# list_ = [1, 2, 3, 4]
# list_.append(5)
# print(list_)

# .extend(element[iterable]) -> расширение списка добавлением в конец
# list_ = [1, 2, 3, 4]
# list_.extend([1,2,3])
# list_.append([1,2,3])
# print(list_)

# .insert(index, element) -> добавляет элемент по индексу
# list_ = [1, 2, 3, 4]
# list_.insert(0, 9)
# print(list_)

# .index(element, [start], [end]) -> возвращает индекс элемента
# list_ = [1, 2, 3, 4]
# print(list_.index(4))

# .clear() -> очищает список 
# list_ = [1, 2, 3, 4]
# list_.clear()
# print(list_)

# .count(element) -> возвращает кол-во вхождений элемента в список
# list_ = [1, 2, 3, 4, 3, 3]
# print(list_.count(4))

# print(len(list_)) -> кол-во эдементов в списке или длина списка

# .pop(index) -> удаляет  и возвращает элемент по index, если индекс не указан то удалит с конца
# list_ = [1, 2, 3, 4, 3, 3]
# list_.pop()
# list_.pop(0)
# print(list_)

# .remove(element) -> удаляет первый элемент в списке
# list_ = [1, 2, 3, 4, 3, 3]
# list_.remove(3)
# print(list_)

# .reverse() -> переворачивает список
# [::-1]
# list_ = [1, 2, 3, 4, 3, 3]
# list_.reverse()
# print(list_)

# .sort() -> сортирует список (reverse=True)
# list_ = [1, 2, 3, 4, 3, 3]
# list_ = ['hello', 'makers', 'bootcamp']
# list_ = ['&', '*', '%']
# list_.sort()
# print(list_)

# .copy() -> поверхностное копирование
# list_ = [1, 2, 3, 4, 3, 3]
# new_list = list_.copy()
# new_list.append(1)
# print(list_)
# print(new_list)

''' Цикл for '''
# цикл - это блок кода, который повторяется несколько раз

# for -> работает с итерируемыми объектами, заканчивается тогда когда доходит до конца 

# list_ = [1, 2, 3, 4, 5]
# for element in list_:
#     print(element)

# for i in 'hello':
#     print(i)

# ls = []
# for i in range(11):
#     ls.append(i)
# print(ls)

# for i in range(11):
#     if i == 3:
#         print(i)
#     else:
#         print('hello')

# names = input('Ведите имена через пробел: ').lower().split()
# guests = input('Ведите имена через пробел: ').lower()

# for guest in guests:
#     if guest in names: 
#         print(f'вы приглашены {guest}')
# else:
#     print('иди спать {guest}') 

''' Tuple (Кортеж) '''
# tuple_ = (1, 2, 3)
# print(tuple('hello'))
# print(dir(tuple))

# (,) -> литералы tuple

''' Методы tuple'''
# .count(element) -> 
# tuple_ = (1, 2, 3, 4, 5, 6, 1, 4, 1, 1, 1)
# print(tuple_.count(1))

# .index(element) -> возвращает индекс элемента

# print(tuple_.index(1))

# count = 0
# for i in tuple_:
#     if i == 1:
#         print(count)
#     count = count + 1





