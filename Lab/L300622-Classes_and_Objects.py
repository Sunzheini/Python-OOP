# Classes and Objects


# class Person:
#     min_age = 0       # property / field (data atribute)
#
#     def __init__(self, name, age):        # method / function atribute
#         self.name = name                  # property / fiels (data atribute)
#         self.age = age                    # method / function atribute
#
#     def print_info(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#
#
# p1 = Person('Daniel', 39)
#
# print(p1.name)
# print(p1.age)
# p1.print_info()
# print(Person.min_age)

# --------------------------------------------------------------------------------------------

# __init__ - zadava pyrvonachalniq state na nashata instanciq

# --------------------------------------------------------------------------------------------

# self - refernciq kym instanciqta v samata instanciq

# --------------------------------------------------------------------------------------------

# 1
# class Vehicle:
#     def __init__(self, mileage, max_speed=150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#
#
# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)

# --------------------------------------------------------------------------------------------

# special / dunder methods

# class Fraction:
#     def __init__(self, nominator, denominator):
#         self.nominator = nominator
#         self.denominator = denominator
#
#     def __str__(self):
#         return f"{f1_2.nominator}/{f1_2.denominator}"
#
#     def __add__(self, other):           # fraction 1 + fraction 2
#         nominator = self.nominator * other.denominator + other.nominator * self.denominator
#         denominator = self.denominator * other.denominator
#         return Fraction(nominator, denominator)
#
#
# f1_2 = Fraction(1, 2)
# print(f1_2)
# print(Fraction(3, 4))
# print(Fraction(1, 2) + Fraction(3, 4))

# --------------------------------------------------------------------------------------------

# __str__ - # kak nashiq obekt da se pokazva kato string

# posle:
# print(Person) printira __str__
# ili
# print(str(Person))

# --------------------------------------------------------------------------------------------

# __repr__ - vryshta machine readable representation

# ss = 'Doncho'
# print(str(ss))              # Doncho
# print(repr(ss))             # 'Doncho'
# print(eval(repr(ss)))       # Doncho


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Name: {self.name}; Age: {self.age}"
#
#     def __repr__(self):
#         return f'Person("{self.name}", {self.age})'
#
# p = Person("Daniel", 39)
# print(str(p))
# print(repr(p))

# --------------------------------------------------------------------------------------------

# 2

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"
#
#
# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)

# --------------------------------------------------------------------------------------------

# instance vars and class vars

# class Person:
#
#     min_age = 0
#     max_age = 150
#
#     def __init__(self, name, age):
#         self.name = name            # instance attributes / instance properties
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} -- {self.age} -- {self.max_age}"
#
# print(Person("Daniel", 39))         # Daniel -- 39 -- 150
# Person.max_age = 44                 # not a good practise
# print(Person("Daniel", 39))         # Daniel -- 39 -- 44

# --------------------------------------------------------------------------------------------

# 4

# class Circle:
#
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         return self.pi * self.radius * self.radius
#
#     def get_circumference(self):
#         return self.pi * self.radius * 2
#
#
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())

# --------------------------------------------------------------------------------------------

# 4

# class Glass:
#
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if self.content + ml <= self.capacity:
#             self.content += ml
#             return f"Glass filled with {ml} ml"
#         else:
#             return f"Cannot add {ml} ml"
#
#     def empty(self):
#         self.content = 0
#         return "Glass is now empty"
#
#     def info(self):
#         return f"{self.capacity - self.content} ml left"
#
#
# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())

# --------------------------------------------------------------------------------------------

# special data attributes

# print(Glass.__name__)       # printira imeto
# print(Glass.__doc__)        # printira zapisanoto v """ """ pod imeto na klasa ili metoda v klasa
# print(Glass().__dict__)     # vryshta dict s vsichki instance atributi

# --------------------------------------------------------------------------------------------

# 5

# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         self.is_on = not self.is_on                 # !!!
#
#     def install(self, app, app_memory):
#         if self.is_on and app_memory <= self.memory:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f"Installing {app}"
#         elif not self.is_on and app_memory <= self.memory:
#             return f"Turn on your phone to install {app}"
#         else:
#             return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
#
#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())



