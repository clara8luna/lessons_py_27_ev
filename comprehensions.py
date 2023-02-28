'''Comprehension'''
# синтаксический сахар -  упращение кода

# генерация последовательности  в одну строку используя цикл (синтаксический сахар)

# list, set, dict
'''Синтаксис'''
# result for element in iterable_object
# result for element in iterable_object if filter 

'''====== LIst comprehension ======'''
''' Упрощенный подход к созданию списка,  задействует цикл for и if-else.  Работает быстрее чем обычный'''
# 

''' for '''
# list_=[]
# for i in range(11):
#     list_.append(i)
# print(list_)

# a=list((i for i in range(11)))
# print(a)

# list_=[i for i in range(11)]
# print(list_)
# '''#
'''засекаем время'''
# import time
# start_time= time.time()

# list_=[]
# for i in range(100000):
#     list_.append(i)
# time1= time.time()- start_time

# start_time = time.time()
# list_2=[i for i in range(11)]
# time2= time.time()- start_time
# print( time1, time2)

''' if '''
# 
# list_=[]
# for i in range(11):
#     if i%2==0:
#         list_.append(i)
# print(list_)

# list_2=[i for i in range(11) if i%2==0]
# print(list_2)
# 

# list_2=[i for i in range(0,11,2)]
# print(list_2)

# list_2=[i for i in range(11) if not i%2]
# print(list_2)


# a=['hello'for i in range(10)]
# print(a)    #['hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']

# print([input() for i in range(2)])     на каждой итерации запрашивает ввод(input)

''' if- else . Если в условии нужен else, то все условие пишется перед for'''
# list_2=[i if not i%2 else 'hello' for i in range(11) ]
# print(list_2)    #[0, 'hello', 2, 'hello', 4, 'hello', 6, 'hello', 8, 'hello', 10]
'''задача '''
# list_1 =[1,'hello', 3, 'a', 4.0, 6, 8, 'hw']
# l=['четное' if i%2==0  else 'нечетное' for i in list_1 if type(i)==int or type(i)== float]
# print(l)   #['нечетное', 'нечетное', 'четное', 'четное', 'четное']



''' set comprehension'''
#  почти тоже самое как и представление списков(list comprehension)
#  Используются {} скобки, не содержит дубликатов,  не гарнтирует сохранность элементов в порядке

# list_=[1,2,3,4,5,4,5,3,2]
# set_={i for i in list_}
# print(set_)    #{1, 2, 3, 4, 5}

# set_= set()
# for i in list_:
#     set_.add(i)
# print(set_)

''' dict comprehension'''
# необходимо дополнительно определить ключ

# dict_={i: i for i in range(10)}
# print(dict_)   #{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

# dic={}
# for i in range(10):
#     dic.update({i: i**2})
# print(dic)  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# l=[1,1,2,3,2,2,3,4,5]
# li={i: l.count(i) for i in l}
# print(li)   #{1: 2, 2: 3, 3: 2, 4: 1, 5: 1}

# d={'a':2, 'b':3}
# l={k: 'четное' if v%2==0 else 'нечетное' for k,v in d.items() }
# print(l)  #{'a': 'четное', 'b': 'нечетное'}
'''создать словарь, где ключи- это числа от 1 до 10, а значения эти же числа в виде строки'''
# d={i: str(i) for i in range(1,11)}
# print(d)

''''''
# l1=[1,2,3,4,5]
# l2=['a','b','c','d','e']
# d={ l1[i]: l2[i] for i in range(len(l1))}
# print(d)   #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


''' вложенные comprehension'''
# d={i: list(range(1,i+1)) for i in range(1,6)}
# print(d)

# d={i: [j for j in range(1,i+1)] for i in range(1,6)}  # вложенность
# print(d)

''''''
# l=[['hello world' for i in range(5)] for j in range(10)]
# print(l)

employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
    }}
# for info in employees.values():
#     for k,v in info.items():
#         if k=='age':
#             info[k] = float(v)
# print(employees)

# print({id_: {k: float(v) if k=='age' else v for k,v in info.items()} for id_, info in employees.items()})
# # info == {k: float(v) if k=='age' else v for k,v in info.items()}