'''====== Множества set() ======'''
# изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных
# Предназначен для хранения уникальных значений. Могут хранить в себе только неизменяемый тип данных, если используете tuple, то в них тоже должны храниться неизменяемый типы данных

# set1 = {1, 2, 3, 3}
# print(set1)
# for i in set1: 
#     print(i)

# set2 = {(1, 2, 3, (1, ))}
# print(set2)

# set3 = {1, True, False, 0}
# print(set3) # {1, False}

''' Создание множеств '''
# 1. set()
# a = set([1, 2, 3, 4])
# a = set({'a':1, 'b': 2})
# a = set('hello world')
# print(a)

# 2. {}
# set_ = {1, 2, 3, 'hello', (4, 5), None, True, False}
# print(set_)

'''====== Методы множеств ====='''
# add(element)
# update(sequence)

# set_= {1, 2, 3}
# set_.add(3)
# set_.add('hello')
# set.add([1, 2, 3]) # Error

# update(за раз может добавить несколько элементов, но не повторяет имеющиеся) все итерируемые 
# set_.update('hello')
# set.update([1, 2, 3, 4])
# set_.update({'a': 99, 'b': 97}, 'string')
# print(set_)

'''Удаление элементов'''
# clear() -> очищение всего множества
# remove(element) -> удаляет элемент, если такого элемента нет выдает ошибку
# discard(element) -> если элемента нет, ничего не произойдет
# pop() -> удаляет случайный, по принцину fifo (first in firts out)

# set_ = {1, 2, 3, 4, 5}
# set_clear()
# set_.remove(1)
# set_.discard(9)
# set_.pop()
# print(set_)
# popped = set_.pop()
# print(set_, popped)

# set_a.difference(set_b) -> выводит элементы, которые есть в set_a, но нет в set_b
# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.difference(set_b))
# print(set_a - set_b)

# set_a.symmetric_difference(set_b) -> выводит уникальные элементы в обоих сетах
# set_a^set_b
# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.symmetric_difference(set_b))


# set_a.intersection(set_b) -> выводит похожие элементы для set_a b set_b
# set_a & set_b
# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.intersection(set_b))

# set_a.union(set_b) -> объединяет set_a  и set_b
# set_a | set_b
# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.union(set_b))

# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# set_b = [3, 4, 5, 6] # Error
# res = set_a | set_b
# print(res)

# Homework
# copy()
# difference_update()
# intersection_update()
# symmetric_difference(update)

# isdisjoint()
# issubset()
# issuperset()

# a = [1, 2, 3]
# for i in a:
#     print(i)
#     a.append(i)

# address = '1.1.1.1'
# a = ''
# print(address.replace('.', '[.]'))

# for i in address:
#     if i == '.':
#         i = '[.]'
#     a += i
# print(a)

# command = 'G()()()()()(al)'
# print(command.replace('()', 'o').replace('(al)', 'al'))

