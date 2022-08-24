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


#
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




















