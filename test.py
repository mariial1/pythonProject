# 1)Дан лист:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - найти min число в листе
# - удалить все одинаковые значения
# - заменить каждое четвертое значение на "Х"
# - вывести элемент листа, значение которого ближе всего
# к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] = > 5
# [-1, -2, 3, 4, 555] = > 4
# [5, 5, 5, 5] = > 5
# [-10, 5, 5] = > 5


# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# print(min(list))
# print(max(list))

# s1 = set(list)
# print(s1)

# list2 = list[::4]
# print(list2)
#
# for i in range(0, len(list), 4):
#     list[i] = 'X'
# print(list)
#
#
# list.sort()
# sum = 0
# for i in list:
#     sum += i
# avg = sum / len(list)
#
# candidates = []
#
# for i in range(len(list)):
#     if list[i] > avg:
#         candidates.append(list[i])
#         candidates.append(list[i - 1])
#         break
# print("Avg =", avg)
#
# if not len(candidates):
#     print('result:', avg)
# else:
#     print('result = ', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])
#
######################################
# решение:
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# while True:
#     print('1. найти min число в листе')
#     print('2. удалить все одинаковые значения')
#     print('3. заменить каждое четвертое значение на "Х"')
#     print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех елементов в листе')
#     print('5. выход')
#
#     choice = input('Сделайте свой выбор: ')
#     if choice not in '1234567':
#         continue
#
#     elif choice == '1':
#         min_num = l[0]
#         for item in l:
#             if min_num > item:
#                 min_num = item
#         print(l)
#         print('min_num: ', min_num)
#
#     elif choice == '2':
#         l2 = l.copy()
#         for i in range(len(l2) - 1, -1, -1):
#             if l2.count(l2[i]) > 1:
#                 del l2[i]
#
#         print(l)
#         print(l2)
#
#     elif choice == '3':
#         l2 = l.copy()
#         for i in range(3, len(l2), 4):
#             l2[i] = 'X'
#         print(l2)
#
#     elif choice == '4':
#         print('List =', l)
#         l.sort()
#         sum = 0
#         for i in l:
#             sum += i
#         avg = sum / len(l)
#
#         candidates = []
#
#         for i in range(len(l)):
#             if l[i] > avg:
#                 candidates.append(l[i])
#                 candidates.append(l[i - 1])
#                 break
#         print("Avg =", avg)
#
#         if not len(candidates):
#             print('result:', avg)
#         else:
#             print('result = ', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])
#
#     elif choice == '5':
#         break

######################################

# 2)вывести на экран пустой квадрат из "*" сторона
# которого указана в переменой:
# a = 7
# i = a
# while i >= 1:
#     if i == a or i == 1:
#         j = a
#         while j > 0:
#             print('*', end='')
#             j -= 1
#         print()
#     else:
#         j = a - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1

# 3) переделать первое задание под меню с помощью цикла


# 4) вывести табличку умножения с помощью цикла while
# i = 1
# size = 10
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res, end='  ')
#         else:
#             print(res, end='   ')
#         j += 1
#     print()
#     i += 1
