

# First Steps in OOP

# functions enable extensibility (change of requirements fot teh function)
# def get_name(number):
#     if number == 1:
#         return 'One'
#     elif number == 2:
#         return 'Two'
#     else:
#         return number
#
#
# def print_list(z):
#     for x in z:
#         if x is None:
#             continue
#         else:
#             print(get_name(x))
#
#
# ll = [1, 2, 3, 4]
# ll2 = [5, 6, 7, 8]
#
# print_list(ll)
# print_list(ll2)

# ------------------------------------------------------------------

# 1 - Rhombus of stars

# def get_line(i, n):
#     spaces_count = n - 1 - i
#     stars_count = i + 1
#
#     return ' ' * spaces_count + ('* ' * stars_count).strip()
#
#
# def create_rhombus(n):
#     for i in range(0, n, 1):
#         print(get_line(i, n))
#     for i in range(n-2, -1, -1):
#         print(get_line(i, n))
#
#
# n = int(input())
# create_rhombus(n)

# ------------------------------------------------------------------

# Scope and namespace

# # global namespace - pi and sum1 - (global for this module)
# from math import pi
#
#
# def sum1(ll):
#     # result and x - in local namespace (local for func body and class)
#     result = 1
#     for x in ll:
#         result += x
#     return result
#
#
# print(sum1([1, 2, 3, 4]))
#
# # built-in namespace
# print(sum([1, 2, 3, 4]))
#
#
# # can overwrite
# # local > global > built-in

# ------------------------------------------------------------------

# Scope
# a region of the program where a namespace is directly accessible

# global scope - for the module
# function scope
# class scope (from function scope)


# text = 'Daniel'
#
# def print_greeting():
#     text = 'Maxi'
#     print(text)
#
# print_greeting()        # printira Maxi
# print(text)             # printira Daniel


# pyrvo se proverqva nai-blizkiq scope, sled tova i ostanalite, dokato proverim i globalniq


# def f1_rec():
#     def f1_rec():
#         def f1_rec():
#             print("f1_rec 3")
#
#         print("f1_rec 2")
#         f1_rec()
#
#     print("f1_rec 1")
#     f1_rec()    # pyrvo proverqva ima li f1_rec() v lokalniq scope
#                 # ako go nqma se gleda v roditelskiq ... globalniq i built-in
#
# f1_rec()        # f1_rec 1  \n  f1_rec 2  \n  f1_rec 3

# ------------------------------------------------------------------

# prints_count = 0
#
# def print_list(ll):             # za neferentni tipove:
#     print(prints_count)         # moga da izpolzvam promenlivata
#     #prints_count += 1          # no ne i da q promenq
#     print(ll)
#
# ll = list(range(5))
#
# print_list(ll)
# print(prints_count)


# za da q promenq - global
# prints_count = 0
#
# def print_list(ll):
#
#     global prints_count         # access v globalniq scope
#     prints_count += 1
#
#     print(ll)
#
# ll = list(range(5))
#
# print_list(ll)
# print(prints_count)


# nonlocal
# def f1():
#     count = 0
#     def f1_inner():
#         nonlocal count      # access v parent funkciite otvytre navyn
#         count += 1
#
#     for _ in range(5):
#         f1_inner()
#         print(count)
#
# f1()

# ------------------------------------------------------------------

# 2. Scope mess - another file

# ------------------------------------------------------------------

# OOP
# v python funkciite i klasovete sa first class obekti

# vsichko v python e obekt
# vseki obekt ima stoinost (state) i publichen interface (behaviour)


# class Person:
#     # constructor
#     def __init__(self, name, age):      # dostypvam sebe si
#         self.name = name
#         self.age = age
#
#
# daniel = Person("Daniel", 39)
# maxi = Person("Maxi", 10)
#
# print(daniel.age)
# print(maxi.age)

# ------------------------------------------------------------------

# 3. Class book

# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#
# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)

# ------------------------------------------------------------------

# __str__
# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):      # string kak bihme iskali da izglejda
#         return f"{self.name}, {self.author}, {self.pages}"
#
#
# book = Book("My Book", "Me", 200)
# print(str(book))            # calls __str__

# ------------------------------------------------------------------

# methods can change the state
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def increase_age(self):
#         self.age += 1
#
#
# daniel = Person("Daniel", 39)
# maxi = Person("Maxi", 9)
#
# print(daniel.age)
# print(maxi.age)
#
# daniel.increase_age()
# maxi.increase_age()
#
# print(daniel.age)
# print(maxi.age)

# ------------------------------------------------------------------

# 4. Car

# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model
#         self.engine = engine
#
#     def get_info(self):
#         return f"This is {self.name} {self.model} with engine {self.engine}"
#
#
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())

# ------------------------------------------------------------------

# 5. Music

class Music:
    def __init__(self, title, artist, lyrics):
        self.lyrics = lyrics
        self.artist = artist
        self.title = title

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())

# ------------------------------------------------------------------
























