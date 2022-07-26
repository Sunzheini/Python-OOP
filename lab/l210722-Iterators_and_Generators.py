# Iterators and Generators


# iterator - obekt koito moje da hodi po state-a na nashite obekti
# for, comprehension, unpacking

# ------------------------------------------------------------------
# __iter__() - internal dunder method in class
# iter() - external for clss that calls __iter__


# print('---for loop---')
# ll = [1, 2, 3, 4, 5]
# for x in ll:
#     print(x)
#
# print('---Manual---')
# ll_iter = iter(ll)  # creates an iterator object for ll
#
# print(ll_iter)
# print(next(ll_iter))    # get next value
# print(next(ll_iter))    # get next value, etc
#
# print('---while---')
# ll_iter = iter(ll)
# while 1:
#     value = next(ll_iter)
#     print(value)

# ------------------------------------------------------------------
# 2 iteratora

# ll = [1, 2, 3, 4, 5]
#
# ll_iter1 = iter(ll)
# ll_iter2 = iter(ll)     # iteratorite sa nezavisimi

# ------------------------------------------------------------------
# StopIteration exception

# ll = [1, 2, 3, 4, 5]
#
# ll_iter = iter(ll)
# while 1:
#     try:
#         value = next(ll_iter)
#         print(value)
#     except StopIteration:
#         print('Stopped')
#         break

# ------------------------------------------------------------------

# 1
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.next_value = start
#
#     def __iter__(self):
#         return self         #samiq klas stava interator
#
#     def __next__(self):
#         if self.next_value > self.end:
#             raise StopIteration         # no more values to iterate
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

# ------------------------------------------------------------------
# class custom_range_iterator:
#     def __init__(self, cr):
#         self.cr = cr
#         self.next_value = self.cr.start
#
#     def __next__(self):
#         if self.next_value > self.cr.end:
#             raise StopIteration
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
#
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return custom_range_iterator(self)
#
#
# cr = custom_range(1, 10)
# ll = [1, 2, 3, 4, 5]
#
# cr_iter = iter(cr)
# ll_iter = iter(ll)
#
# print(cr_iter)
# print(ll_iter)

# ------------------------------------------------------------------

# 2
# class reverse_iter:
#     def __init__(self, values):
#         self.values = values
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < -len(self.values):   # !!!
#             raise StopIteration
#         value_to_return = self.values[self.index]
#         self.index -= 1
#         return value_to_return
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)

# ------------------------------------------------------------------
# generator - syntactic sugar vyrhu iteratori
# funkciq koqto izpolzva yield

# class custom_range:
#     def __init__(self, n):
#         self.n = n
#         self.next_value = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.next_value == self.n:
#             raise StopIteration
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
#
# def first_n(n):         # generator, zamenq gornoto
#     value = 1
#     while value < n:
#         yield value     # pri sledvashta iteraciq prodyljava ot yield-a
#         value += 1
#
#
# for x in custom_range(10):
#     print(x)
#
# for x in first_n(10):
#     print(x)

# ------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __iter__(self):
#         yield ('name', self.name)
#         yield ('age', self.age)
#
#
# daniel = Person('Daniel', 19)
#
# for x in daniel:
#     print(x)

# ------------------------------------------------------------------
# diff return and yield

# def gen_func(n):
#     for x in range(n):
#         yield x
#
#
# def norm_func(n):
#     for x in range(n):
#         return x
#
#
# print(norm_func(5))         # 0
# print(gen_func(5))          # <generator object gen_func at 0x000002B6C07C5D90>
# print(next(gen_func(5)))    # 0

# ------------------------------------------------------------------
# generator expressions
# chrez comprehension pravim generator funkciq

# [ -> literal for list comprehension
# { -> literal for set or dict comprehension
# ( -> literal for generator expression


# def print_values(values_iter):
#     for value in values_iter:
#         print(value)
#
# def gen_func(n):
#     for x in range(n):
#         yield x

## syshtoto kato:

# def print_values(values_iter):
#     for value in values_iter:
#         print(value)
#
# print_values(
#     (x for x in range(5))       # gen expression
# )

# ------------------------------------------------------------------
# def custom_range_1(n):
#     value = 1
#     while value < n:
#         yield value
#         value += 1
#
#
# def custom_range_2(n):
#     values = list(range(1, n))  # create a list of n elements
#     for value in values:
#         yield value
#
#
# for x in custom_range_1(5):
#     print(x)
#
# for x in custom_range_2(5):
#     print(x)

# ------------------------------------------------------------------
# 3
# class vowels:
#     vowel_chars = 'eyuioa'
#
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.text):
#             if self.text[self.index].lower() not in self.vowel_chars:
#                 self.index += 1
#                 continue
#
#             value_to_return = self.text[self.index]
#             self.index += 1
#             return value_to_return
#
#         raise StopIteration
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


# 4
# def squares(n):
#     value = 1
#     while value < n + 1:
#         yield value * value
#         value += 1
#
#
# print(*squares(5))      # !!!


# 5
# def genrange(start, end):
#     value = start
#
#     while value < end + 1:
#         yield value
#         value += 1
#
#
# print(list(genrange(1, 10)))


# 6
def reverse_text(text):
    index = len(text) - 1

    while index > -1:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')




















