# Decorators

# -----------------------------------------------------------------
# closure

# def f(x):
#     def f_internal(y):
#         return x + y          # f_internal makes closure with x
#
#     return f_internal
#
#
# f1 = f(2)
# print(f1)       # <function f.<locals>.f_internal at 0x000002934E560E50>
#
# print(f1(3))    # 3 + 2 = 5
# print(f1(4))    # 4 + 2 = 6
# print(f1(5))    # 5 + 2 = 7

# -----------------------------------------------------------------
# 1     # !!!

# def number_increment(numbers):
#
#     def increase():
#         return [x+1 for x in numbers]    # numbers is part of closure
#                                          # promenliva ot roditelski scope
#     return increase()
#
#
# print(number_increment([1, 2, 3]))

# -----------------------------------------------------------------
# decorators

# promenqme neshto kak raboti bez da go promenqme
# funckii koito vzemat kato parametyr funkcii


# def uppercase_basic(func_to_be_decorated):
#     result = func_to_be_decorated()
#     return result.upper()
#
#
# def uppercase(func_to_be_decorated):    # the decorator
#     def func_wrapper():
#         result = func_to_be_decorated()
#         return result.upper()
#
#     return func_wrapper
#
#
# def get_shopping_list():
#     return 'eggs, milk, sugar'
#
#
# def get_name():
#     return 'Daniel Zorov'
#
#
# get_name = uppercase(get_name)      # decorated of get_name
# print(get_name)
#
# # print(uppercase_basic(get_shopping_list))
# # print(uppercase_basic(get_name))
#
# # print(f"I am {get_name()}")
# # print(f"I have to buy {get_shopping_list()}")

# -----------------------------------------------------------------
# @

# def uppercase(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#
#     return wrapper
#
#
# @uppercase      # == get_shopping_list = uppercase(get_shopping_list)
# def get_shopping_list():
#     return 'eggs, milk, sugar'
#
#
# @uppercase
# def get_name():
#     return 'Daniel Zorov'
#
#
# print(f"I am {get_name()}")
# print(f"I have to buy {get_shopping_list()}")

# -----------------------------------------------------------------
# @wraps
# from functools import wraps
#
#
# def uppercase(func):
#     @wraps(func)        # posle mojem da imame pravilnite meta danni na dekoriranata funkciq
#     def wrapper():
#         result = func()
#         return result.upper()
#
#     return wrapper
#
#
# @uppercase      # == get_shopping_list = uppercase(get_shopping_list)
# def get_shopping_list():
#     return 'eggs, milk, sugar'
#
#
# @uppercase
# def get_name():
#     return 'Daniel Zorov'
#
#
# print(f"I am {get_name()}")
# print(f"I have to buy {get_shopping_list()}")

# -----------------------------------------------------------------

# 2
# from functools import wraps
#
#
# def vowel_filter(func):
#     vowels = 'eyuioa'
#
#     @wraps(func)
#     def wrapper():
#         result = func()
#         return [x for x in result if x.lower() in vowels]
#
#     return wrapper
#
#
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())

# -----------------------------------------------------------------
# accepting arguments - 98% ot dekoratorite se pishat s *args i **kwargs
# from functools import wraps
#
#
# def measure_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
#
# @measure_time
# def sum_two(x, y):
#     return x + y
#
#
# @measure_time
# def sum_three(x, y, z):
#     return x + y + z
#
#
# print(sum_two(1, 2))
# print(sum_three(1, 2, 3))
# print(sum_three(1, 2, z=3))

# -----------------------------------------------------------------

# 3
# from functools import wraps
#
#
# def even_numbers(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return [x for x in result if x % 2 == 0]
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))

# -----------------------------------------------------------------
# passing arguments

# def dec(func):
#
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# # decorator factory - funckiq koqto ni vryshta dekorator, koito moje da vzima parametri
# def dec_with_params(params):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return dec
#
#
# @dec
# def x():
#     pass
#
#
# @dec_with_params(params='asd')      # !!!
# def y():
#     pass

# -----------------------------------------------------------------

import sys
from functools import wraps


def log(filepath):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            stdout_original = sys.stdout
            with open(filepath, 'a') as file:
                sys.stdout = file
                result = func(*args, **kwargs)
            sys.stdout = stdout_original
            return result

        return wrapper
    return decorator


@log(filepath='./log.txt')
def say_hello(name):
    print(f"Hello {name}")


say_hello("Daniel")

# -----------------------------------------------------------------
#decorating methods in classes - po syshtiq nachin

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @cache
#     @measure_time
#     def get_age_after_years(self, years):
#         return self.age + years
#
#
# p = Person('Daniel', 40)
# print(p.get_age_after_years(10))

# -----------------------------------------------------------------
# decorators as classes





























