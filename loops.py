''' ======= Циклы ======='''
# while -> цикл, который работает пока условие верно True

# while True:
#     print('hello')

'''опасность в создании бесконечного цикла'''

# counter = 0
# while counter < 11:
#      print(counter) # neverending circle
#      counter = counter + 1
#      print(counter)

# while False: #никогда не заработает
    # print('hello')

# counter = 10
# while counter > 1:
#     #  print(counter) # neverending circle
#      counter = counter - 1
#      print(counter)

# a = o # bool(0) -> False doesn't work
# while a:
#     print('hello')

# a = 7368538579384579
# summa = 0
# for i in str(a):
#     summa = summa + int(i)
# print(summa)

# a = '2jhb234jhbjh423345nb'
# summa = 0
# for i in a:
#     if i.isdigit():
#         summa = summa + int(i)
# print(summa)

# i = 0
# summa = 0
# a = str(937983749873)
# while i < len(str(a)):
#     # print(str(a)[i])
#     summa = summa + int(a[i])
#     i = i + 1
# print(summa)

# при итерации словаря -> получаем только ключи
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for i in dict_:
#     print(i)

# dict_.keys() -> прохождение по ключам
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for i in dict_.keys():
#     print(i)

# dict_.values() -> прохождение по значениям
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for i in dict_.values():
#     print(i)

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for i in dict_:
#     print(dict_[i])

'''получает tuple из ключа и значения'''
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for i in dict_.items():
#     print(i)

# распаковываем tuple на две переменныe
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# for k, v in dict_.items():
#     print(k)
#     print(v)

# for a, b, c in [(1, 2, 3), [4, 5, 6]]:
#     print(a, b, c)


'''====== Ключевые слова в циклах ======'''
# break -> полностью выйти из циклаю. досрочно прерывает цикл
# continue -> переход к следующей итерации
# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла

# for i in range(11):
#     if i == 4:
#         continue
#     print(i)

# for i in range(11):
#     print (i)
#     if i == 4:
#         continue

# for i in range(11):
#     print(i)
#     if i == 4:
#         break

# for i in range(11):
#     if i == 4: break
#     print(i)

# i = 0
# while i < 10:
#     # i = i + 1
#     i += 1
#     if i == 3:
#         continue
#     elif i == 7:
#         break
#     print(i)

'''===== else ====='''
# слово else, применяется в циклах for и while -> проверяет, был ли произведен выход из цикла без оператора break (естественным образом) Код внутри отработает если не сработал break

# i = 0
# while i < 10:
#     if i == 5: pass
#     print(i)
#     i += 1
# else:
#     print('hello')

'''===== Оператор pass ====='''
'''ничего не делает. Фактически заглушка для объектов pass == ...'''

# for i in range(11):
#     if i == 4: pass
#     print(i)