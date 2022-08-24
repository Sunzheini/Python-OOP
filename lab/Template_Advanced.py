# Lists as Stacks and Queues


# in pyhton we use lists as stacks - mylist = []
# push - append()
# pop - pop()
# peek - print(mylist[-1])
# len - len(mylist)

#     elif action == '2' and s:   #ako steka ne e prazen inache greshka
#         s.pop()


# from collections import deque
# q = deque()

# # enqueue
# q.append(2) #append right
# # ili q.appendleft(3)
#
# # dequeue
# q.popleft()
# # ili q.pop() #pop right
#
# # peek
# print(q[0])
#
# # count


# operations = {'+': lambda a, b: a + b,      # !!!
#               '-': lambda a, b: a - b,
#               '*': lambda a, b: a * b,
#               '/': lambda a, b: a // b,
#               }
# for i in input_string:
#     if i in '+-*/':
#         while len(q) > 1:
#             left = q.popleft()
#             right = q.popleft()
#             result = operations[i](left, right)    #!!!
#             q.appendleft(result)


#for, else
#else se izpylnqva sled kraq na for, ako predi tova nqma break


#command.startswith('fff') # proverqva dali zapochva s tova
#command.endswith

#--------------------------------------------------------------------------
# Tuples and Sets


# Tuples: immutable but objects inside are mutable
# definiciq
# t = (1, 2, 3)
# t = 1, 2, 3
# t = (1, ) # s edin element
# print(t)

# methods
# numbers = (1, 2, 3, 4)
# print(numbers.count(1))

# names = ('maimuna', 'maiz', 'morz')
# print(names.index('morz')) # index (1, 0)
# print(names.index('morz', 1)) # index ('morz', 1) tyrsi morz ot 1vi index nadqsno


# unpacking
# tt = (1, 2, 3)
# x, y, z = tt
# print(x, y, z)


# SETS - mutable
# ss = {1, 2, 3, 4, 5}
# sss = set() # samo taka prazen set

# ss.add(8)
# ss.remove(4)
# print(4 in ss)      # check if value is in set
# print(len(ss))

# operations
# print(f'{s1} union {s2} = {s1 | s2}')   #union = {1, 2, 3, 4, 5}
# print(f'{s1} & {s2} = {s1 & s2}')       #intersection = {3}
# print(f'{s2} < {s3} = {s2 < s3}')       #subset = True
# print(f'{s1} - {s2} = {s1 - s2}')       #difference = {1, 2}

# set comprehension
# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print({x ** 2 for x in ll})         #kato list ama s kydravi skobi

#--------------------------------------------------------------------------
# multidimentional lists


# mm = []
# rows = int(input())
# for _ in range(rows):
#     ll = [int(x) for x in input().split(', ')]
#     mm.append(ll)
#
# flattened = [x for row in mm for x in row]
# print(flattened)


# def is_outside(row, col, rows, cols):           # validaciq dali sa vytre
#     return row < 0 or col < 0 or row >= rows or col >= cols


# directions = {
#     'R': lambda r, c: (r, c + 1),
#     'L': lambda r, c: (r, c - 1),
#     'U': lambda r, c: (r - 1, c),
#     'D': lambda r, c: (r + 1, c),
# }


# Comprehension
#matrix = [[0 for j in range(2)] for i in range(3)]
#matrix = [[j for j in range(1, 9)] for i in range(1, 5)]

# Accessing element
# print(mm[1][0])         # 4
# print(mm[-1])           # posledniq red

# Diagonal - matricite sa s raven broi koloni na vseki red
# stoinost e na glavniq diagonal ako:           row_index == column_index
# stoinost e na vtorostepenniq diagonal ako:    row_index = n - column_index - 1
# below main diagonal ako:                      column_index < row_index
# above main ako:                               column_index > row_index


#     for row in matrix:
#         print(*row, sep=' ')            # moje i taka

#--------------------------------------------------------------------------
# Functions Advanced


# packigng and unpacking pregovor + dopylnenie
# ll = [1, 2, 3, 4]
# a, b, c, d = ll     # default
# print(a, b, c, d)

# k, l, *r = ll   #izkarai pyrvite 2 a ostanalite v spisyk r
# print(k, l)
# print(r)

# k, *l, r = ll     #bez pyrviq i posledniq gi sloji v l
# print(k, l, r)

# k, *_, r = ll       # ne ni interesuvat srednite
# print(k, r)


# Packing
# we use *args to arguments into tuple


#kwargs - packing arguments into dictionary
# def f(**kwargs):
#     if 'age' in kwargs:
#         kwargs['age'] = None
#     print(kwargs)
#
# print(f(name='Daniel', age=19))             # {'name': 'Daniel', 'age': 19}
# print(f(x=1, y=-11))                        # {'x': 1, 'y': -11}
# print(f(values=[1, 2, 3, 4], pair=(7, 6)))  # {'values': [1, 2, 3, 4], 'pair': (7, 6)}


#packing again
# ll1 = [1, 2, 3, 4]
#
# k, l, *r = ll1
# print(k, l, r)          # 1 2 [3, 4]
#
# ll2 = [1, ll1, -2]
# ll3 = [1, *ll1, -2]     # unpack this list in the middle
# print(ll2)              # [1, [1, 2, 3, 4], -2]
# print(ll3)              # [1, 1, 2, 3, 4, -2]
#
# dd1 = {
#     'x': 1,
#     'y': 2
# }
#
# dd2 = {
#     'z': 3,
#     **dd1,          #** - unpack as a dictionary
# }
#
# print(dd2)          # {'z': 3, 'x': 1, 'y': 2}


# def f(*args, **kwargs):
#     print(f"{args}, {kwargs}")
#
# def shame_maimuna(Daniel, **kwargs):
#     print(f"Daniel has {Daniel}. He is superman.")
#
# numbers = [1, 2, 3, 4, 5]
# grades = {
#     'Doncho': 3,
#     'Ivan': 4,
#     'Daniel': 6,
#     'Pesho': 4.5,
# }
# # !!!!!!!!!
# shame_maimuna(**grades)     # Daniel has 6. He is superman.
# # syshtotoe  kato:
# shame_maimuna(Doncho=3, Ivan=4, Daniel=6, Pesho=4.5)
#
# f(numbers)              # ([1, 2, 3, 4, 5],), {}
# f(*numbers)             # (1, 2, 3, 4, 5), {}
# f(grades)               # ({'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5},), {}
# f(**grades)             # (), {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}
# f(numbers, grades)      # ([1, 2, 3, 4, 5], {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}), {}
# f(*numbers, **grades)   # (1, 2, 3, 4, 5), {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}


# sortirane dict
# my_dict = {'Maymuna': 26, 'Daniel': 44, 'Maxi': 55}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
# sorted_dict2 = sorted(my_dict.items(), key=lambda x: x[1])
# print(sorted_dict)      # [('Daniel', 44), ('Maxi', 55), ('Maymuna', 26)]
# print(sorted_dict2)     # [('Maymuna', 26), ('Daniel', 44), ('Maxi', 55)]
# print(my_dict.items())

#     sorted_dict = sorted(kwargs.items(),
#                          key=lambda x: (-x[1], -len(x[0]), x[0]))   # !!!


# return functions, which are used as normal functions
# def math_operation_factory(operation):
#
#     def add(*args):
#         return sum(args)
#
#     def subtract(*args):
#         return sum(-x for x in args)
#
#     def multiply(*args):
#         result = 1
#         for x in args:
#             result *= x
#         return result
#
#     if operation == '+':
#         return add
#     elif operation == '-':
#         return subtract
#     elif operation == '*':
#         return multiply
#     else:
#         return None
#
# add = math_operation_factory('+')
# subtract = math_operation_factory('-')
# print(add(1, 2, 3))
# print(add(1, 2, -4))
# print(subtract(1, 2, -4))
# print(subtract(1, 2, -4))


# closure -
# vryshtame vytreshnata funkciq, koqto
# close-va vynshnata stoinost x

# def f1(x):
#     def inner_f1(y):
#         return x + y
#
#     return inner_f1
#
# func1 = f1(5)
# print(func1(6))         # 11
# print(func1(5))         # 10


# trqbva da imame neshto koeto da spre rekursiqta
# def reverse_loop(n):
#     if n < 0:               # exit case
#         return
#     print(n)
#     reverse_loop(n - 1)     # recursive call


# parity = 0 if filter == 'even' else 1       # !!!

#--------------------------------------------------------------------------
# Error Handling


# syntax errors - nevaliden python kod
# exception - obekti pazqt info za konkretnata greshka


# def try_raise_exception():
#     chance = 0.3
#     value = random.random()
#     if value < chance:     # ot 0 do 1
#         raise ValueError('Invalid Value!')
#     elif value < 0.7:
#         raise TypeError('Invalid Type!')


# s custom ime
# class ValueTooSmallException(Exception):
#     pass
# value = int(input())
# if value < 10:
#     raise ValueTooSmallException(f'{value} less than 10')


# for i in range(10):
#     try:
#         try_raise_exception()
#         print(f'Try {i} - No Exception!')
#     except ValueError:
#         print(f'Try {i} - Value Error Raised!')
#     finally:
#         print('noob')

#--------------------------------------------------------------------------
# File Handling


# relativen pyt, based on the location of the current file,
# ./ e tekushta direktoriq
#give_contents('./demo.txt')

# ../ e parent direktoriq
#give_contents('../another_demo.txt')


#absolute - based on os file location
#give_contents('D:\Study\Projects\PycharmProjects\Python-Advanced\lab\demo.txt')


# / - windows
# \ - unix, python
# zatova:
# import os
# file_path = os.path.join(path, "directory_name", "file.txt")


# file modes - default e rt

# kakvo shte pravim
# r - read only
# w - create or overwrite file
# a - create or append

# pod kakva forma
# t - text mode
# b - binary mode

# print(open('demo.txt', 'rt').read())
# # normalno - kato text
#
# print(open('demo.txt', 'rb').read()) # chete kartinki v baitove
# # b'I am Daniel\r\nYou are Maimuna\r\nAnd you are Maxi'


# file_path = './demo.txt'
# file = open(file_path, 'r')
# print(file.read(9))     # number of symbols
# print(file.read(8))     # next 8 symbols, ako svyrshi pochva prazni da chete
#                         # noviq red e simvol
# print(file.read())      # whole file
# ako go chetem navednyj celiq text se zarejda v RAM


# file = open(file_path, 'r')
# print(file.readline(3)) # ako moje da prochete 3 simvola
# # ot tozi red gi vryshta, ako ne kolkoto ima


# file = open(file_path, 'r')
# print(file.readlines()) # vsichki redove kato spisyk


# from os import linesep
# file = open('./demo2.txt', 'w')
# file.write('It worksz!')
# file.write(linesep)
# file.write(str(time.time()))


# file1.close()             # s close


# chetem ot ediniq celiq fail i pishem v drugiq
# for i in range(3):
#     with open('./demo.txt', 'r') as file:
#         text = file.read()
#     with open('./demo2.txt', 'a') as file:
#         file.write(text)


# deleting file
# import os
# from os.path import exists
# if exists('./todel.txt'):
#     os.remove('./todel.txt')


# directories
#from os import mkdir, rmdir
#directory_path = './'
#mkdir('./dir_to_del')   # create
#rmdir('./dir_to_del')   # delete
#print(listdir(directory_path))   # ls, samo imenata
# + direktoriite
# files_and_dirs_names = listdir(directory_path)
# files_and_dirs = [join(directory_path, f) for f in files_and_dirs_names]








