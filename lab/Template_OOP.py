# First Steps in OOP


# vsichko v python e obekt
# vseki obekt ima stoinost (state) i publichen interface (behaviour)


# prints_count = 0
# def print_list(ll):
#     global prints_count         # access v globalniq scope
#     prints_count += 1


# def f1():
#     count = 0
#     def f1_inner():
#         nonlocal count      # access v parent funkciite otvytre navyn
#         count += 1


# print(str(book))            # calls __str__
#       ili print(book)


# ----------------------------------------------------------------------
# Classes and Objects


# __init__ - zadava pyrvonachalniq state na nashata instanciq
# self - refernciq kym instanciqta v samata instanciq


# print(Glass.__name__)       # printira imeto
# print(Glass.__doc__)        # printira zapisanoto v """ """ pod imeto na klasa ili metoda v klasa
# print(Glass().__dict__)     # vryshta dict s vsichki instance atributi


# ----------------------------------------------------------------------
# Inheritance


# Inheritance - nasledqvame kod ot klas


# super - means this instance as the parent class
# class Teacher(Person):
#     def __init__(self, name, age, subject, title):
#         super().__init__(name, age)
#         self.subject = subject
#         self.title = title


# Mixins - mixin-a e popylvash klas, ne trqbva da imat state
# class StrMixin:
#     def __str__(self):
#         return ';'.join(f"{key}={value}"
#                         for key, value in self.__dict__.items())


# ----------------------------------------------------------------------
# Encapsulation


# predpazvane i validaciq
# everything written in python is public by default
# other is private and protected and in python is only syntax


# class Student:
#     def __init__(self, number, id_number):     # init ne e private, a dunder
#         self.number = number
#         self.__id_number = id_number           # private
#         self._grades = [5, 6]                  # protected


# print(student._Student__id_number)      # taka dostigame private
# print(student._grades)                  # mojem da dostypim protected


# getter and setter pythonic way - shortcut: props
# class Person:
#     def __init__(self, age=0):
#         self.age = age      # ima ravno i izvikva settera
#                             # v sluchaq age e bez __ !!!
#     @property               # getter (property e dekorator)
#     def age(self):
#         return self.__age
#
#     @age.setter             # setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age
#
#     @property
#     def test(self):
#         return "Hello"
#
# p = Person(16)
# p.age = 15                  # izvikva se bez skobi
# print(p.age)
# print(p.test)


# any
# print(any([]))         # False
# print(any([1, 2, 3]))  # True

# all - obratnoto


# ----------------------------------------------------------------------
# Static and Class Methods


# Static - mogat da syshtestvuvat kato funkciq i izvyn klasa
# no e vytre zaradi nqkakva obshta logika


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
# print(Person.is_adult(5))  # po-pravilno e da se vika taka
# girl = Person("Amy")
# print(girl.is_adult(20))   # no moje da se vika i taka


# Class methods
# class Student:
#     kind = "human"
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def change_kind(cls):       # kato self no kym klasa
#         cls.kind = "asd"        # promenq klas atribut


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     @classmethod
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])

# second_pizza = Pizza.quattro_formaggi()


# ----------------------------------------------------------------------
# Polymorphism and Abstraction


# # izbqgvane na if-ove
# i.e. overwriting methods of parent class


# Overloading built-in methods
#print(da_vinci + chef_robot) == print(da_vinci.add__(chef_robot))
# mojem da prenapishem matematicheskite operatori i op za sravnenie
# == sravnqva po id-to v pametta, t.e. ako sa razlichni lokaciite e !=
# ako imame prenapisan __gt__, nqma nujda za __lt__
# ako imame prenapisan __ge__, nqma nujda za __le__
# ako imame prenapisan __eq__, nqma nujda za __ne__

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#     def __add__(self, other):
#         return Person(self.name, other.surname)     # !!!


# duck typing - type system used in dynamic languages
# we don't care about object type but whether they have the methods we need


# Abstraction - nasilvame na polimorhisma
# ne moje da se pravi instanciq ot abstracten
# trqbva da ima tozi import i (ABC) i pone 1 abstracten method

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     # kogato imash naslednik na Animal
#     # toi zadyljitelno trqbva da prenapishe make_sound v nego
#     def make_sound(self):
#         pass


# ----------------------------------------------------------------------
# Iterators and Generators


# iterator - obekt koito moje da hodi po state-a na nashite obekti
# for, comprehension, unpacking

# __iter__() - internal dunder method in class
# iter() - external for clss that calls __iter__


# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.next_value = start
#
#     def __iter__(self):
#         return self         #samiq klas stava interator

#           v __next__ e logikata za 1 iteraciq + logikata za prikluchvane
#     def __next__(self):
#         if self.next_value > self.end:
#             raise StopIteration         # no more values to iterate
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)


# generator - syntactic sugar vyrhu iteratori
# if a function has at least 1 yield statement is is a generator
# yield e kato return no samo che ne terminira funkciqta a prodyljava napred
# yield pauses the function, saving its states and later continues from there


# def first_n(n):         # generator, zamenq gornoto
#     value = 1
#     while value < n:
#         yield value     # pri sledvashta iteraciq prodyljava ot yield-a
#         value += 1
#
# for x in first_n(10):
#     print(x)


# diff return and yield

# def gen_func(n):
#     for x in range(n):
#         yield x
#
# def norm_func(n):
#     for x in range(n):
#         return x
#
# print(norm_func(5))         # 0
# print(gen_func(5))          # <generator object gen_func at 0x000002B6C07C5D90>
# print(next(gen_func(5)))    # 0


# [ -> literal for list comprehension
# { -> literal for set or dict comprehension
# ( -> literal for generator expression


# generator expressions
# chrez comprehension pravim generator funkciq

# def print_values(values_iter):
#     for value in values_iter:
#         print(value)
#
# print_values(
#     (x for x in range(5))       # gen expression
# )


# ----------------------------------------------------------------------
# Decorators


# closure
# def number_increment(numbers):
#
#     def increase():
#         return [x+1 for x in numbers]    # numbers is part of closure
#                                          # promenliva ot roditelski scope
#     return increase()
#
# print(number_increment([1, 2, 3]))


# promenqme neshto kak raboti bez da go promenqme
# funckii koito vzemat kato parametyr funkcii

# def uppercase(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper
#
# @uppercase      # == get_shopping_list = uppercase(get_shopping_list)
# def get_shopping_list():
#     return 'eggs, milk, sugar'


# @wraps
# from functools import wraps
#
# def uppercase(func):
#     @wraps(func)        # posle mojem da imame pravilnite meta danni na dekoriranata funkciq
#     def wrapper():
#         result = func()
#         return result.upper()
#
#     return wrapper
#
# @uppercase      # == get_shopping_list = uppercase(get_shopping_list)
# def get_shopping_list():
#     return 'eggs, milk, sugar'
#
# @uppercase
# def get_name():
#     return 'Daniel Zorov'
#
# print(f"I am {get_name()}")
# print(f"I have to buy {get_shopping_list()}")


# accepting arguments - 98% ot dekoratorite se pishat s *args i **kwargs
# from functools import wraps

# def measure_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @measure_time
# def sum_two(x, y):
#     return x + y
#
# @measure_time
# def sum_three(x, y, z):
#     return x + y + z
#
# print(sum_two(1, 2))
# print(sum_three(1, 2, 3))
# print(sum_three(1, 2, z=3))


# passing arguments

# def dec(func):
#
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# # decorator factory - funckiq koqto ni vryshta dekorator, koito moje da vzima parametri
# def dec_with_params(params):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return dec
#
# @dec
# def x():
#     pass
#
# @dec_with_params(params='asd')      # !!!
# def y():
#     pass


# @make_bold
# @make_italic
# @make_underline           # pyrvo se izpylnqva dolniq
# def greet(name):
#     return f"Hello, {name}"


# ----------------------------------------------------------------------
# Testing


# Tripple A
# Arrange - podgotvi si neshtata
# Act - testvai
# Assert - oceni


# import unittest
# from random import random
# from unittest import TestCase
#
# class FirstTests(TestCase):
#     x = None
#
#     def setUp(self) -> None:    #runs before each test
#         self.x = random()
#
#     def test_assertEqual(self):
#         print(self.x)
#         self.assertEqual(1, 1)
#
# if __name__ == '__main__':
#     unittest.main()


# tearDown, setUpClass, tearDownClass

# from unittest import TestCase
#
# class TestPerson(TestCase):
#
#     def setUpClass(cls) -> None:    #once per class before all tests
#         pass
#
#     def setUp(self) -> None:
#         pass
#
#     def test_fullname__expect_to_be_correct(self):
#         pass
#
#     def tearDown(self) -> None:     # runs after each test
#         pass
#
#     def tearDownClass(cls) -> None:    # runs once after all tests
#         pass


# mocking - za konkreten test da pravim neshto drugo
# @patch('file.function')
# def test__name(self, mock_name_validator):
#     mock_name_validator.validate_name =

























