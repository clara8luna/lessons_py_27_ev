'''======= Тип данных словари dict() ======='''
# {key: value} 
# позволяет хранить объекты, для доступа к которым используется ключ (key)

# изменяемый, итерируемый, не индексируемый, упорядоченный тип данных

# {} -> литералы
# dict_ = {}
# print(type(dict_))

# dict_ = {'a': 'hello', 'b': 'world', 'c': 3}
# print(dict_['c'])

# ключи должны быть неизменяемыми типами данных
# ключи должны быть уникальными
# значениями словаря могут быть любые типы данных 

# dict_ = {[1, 2]: 'hello'} TypeError: unhashable type: 'list'

# dict_ = {1: {'a': 'one'}, 'hello': [1,2,3]}

# dict_ = {'a': 1, 'a': 2, 'a': 3}
# dict_{['a']} = 100

'''====== Cоздание словарей ======'''
# 1. {key: value}
# 2. dict()
# print(dict('hello')) # Error
# print(dict([('key1', 'value1'), ('key2', 'value2')]))

# print(dict(['ad', 'bc', 'hj']))

# key1, value1 = 'ab'
# print(key1, value1)

# print(dict(a='hello', b='world'))

''''======= Методы словарей ======='''
# .clear() -> очищает словарь -> {}
# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}
# dict_.clear()
# print(dict_)

# .copy -> 
# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}
# dict2 = dict_.copy()

# dict2['hobby'][0] = 'hi'
# print(dict_)

# from copy import deepcopy 
# dict2 = deepcopy(dict_)
# dict2['hobby'][0] = 'hi'
# print(dict2)

# .fromkeys(seq, [value]) -> создает словарь с ключами из seq и значением value (для всех одинаковый, по умолчанию None)

# list_ = ['name', 'age', 'hobby']
# dict_ = dict.fromkeys(list_, 'wow')
# print(dict_)

# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}

# Получение элементов из словаря
# .get(key, [value]) -> возвращает значение по ключу, а если такого ключа нет, не бросает ошибку (исключение), а возвращает value или None

# Изменение элементов словаря 
# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}
# dict_['name'] = 'Same' 
# dict_['address'] = 'Kiyevskaya 25' # создание новой пары
# dict_['hobby'].append(1)
# print(dict_)

# .update(new_dict) -> добавляет new_dict в наш словарь
# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}
# new_dict = {'adress': 23}
# dict_.update(new_dict)
# print(dict_)

# .setdfault(key, [default_value]) -> работает точно так же как метрод get(), но если нет такого ключа он создасть новую пару key: default_value
# dict_ = {'name': 'John', 'age': 25, 'hobby': ['football', 'poker', 'sing']}

# 1. 
# print(dict_.setdefault('name', Sam))

# 2. 
# print(dict_.setdefault('address', '34.....'))
# print(dict_)

# .keys() -> выводит все ключи в словаре
# print(dict_.keys())

# .values()
# print(dict_.values())

# .items() -> возращает все пары из словаря 
# print(dict_.items())

# Удаление элементов в словаре

# pop(key, [message]) -> удаляет пару ключ и значение, и возвращает значение. Если ключа нет, по умолчанию возвращает message (по умолчанию бросает исключение (ошибку))
# print(dict_.pop('name2', 'Noooooo'))
# print(dict_)

# .popitem() -> удаляет и возвращает пару  ключ и значение. Удаляет последнюю добавленную пару
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem())
# print(dict_.popitem()) # Error
# print(dict_)