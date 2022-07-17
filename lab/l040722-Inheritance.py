# Inheritance

# Inheritance - nasledqvame kod ot klas
# Encapsulation - skrivane na internal state i promeni samo prez publichen interfeis
# Abstraction -
# Polymorphism -

# ----------------------------------------------------------------

# class Person:               # Person is extended by Teacher
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Teacher(Person):      # Teacher extends Person
#     pass
#
#
# t = Teacher("Daniel", 39)
# print(t.name)
# print(t.age)

# ----------------------------------------------------------------
# dobavqne na fukniconalnost

# class Person:               # Person is extended by Teacher
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Teacher(Person):      # Teacher extends Person
#     def teach(self):
#         print(f"Mr {self.name} is teaching")
#
#
# t = Teacher("Daniel", 39)
# print(t.name)
# print(t.age)

# ----------------------------------------------------------------
# super - means this instance as the parent class

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} - {self.age}"
#
#
# class Teacher(Person):
#
#     def __init__(self, name, age, subject, title):
#         super().__init__(name, age)
#         self.subject = subject
#         self.title = title
#
#     def teach(self):
#         print(f"Mr {self.name} is teaching")
#
#     def __str__(self):
#
#         # samo ako dopylvame naslednicheski metod, koito go ima i v roditelq
#         return f"{super().__str__()}; subject: Python"
#
#
# t1 = Teacher("Daniel", 39, "Python OOP", "mr")
# t2 = Teacher("Maxi", 9, "C#", "maimuna")
# print(t1)
# print(t2)

# ----------------------------------------------------------------

# 1 -folder

# lab: mark as resources root
#       food: mark as sources root
#               project_3:
#                       food.py
#                       fruit.py

# ----------------------------------------------------------------

# 2 - folder
# from project_3.dog import Dog
#
# dog = Dog()
# print(dog.eat())
# print(dog.bark())

# ----------------------------------------------------------------
# miltiple inheritance

# class X:
#     def fx(self):
#         print("I am X")
#
#
# class Y:
#     def fy(self):
#         print("I am Y")
#
#
# class XY(X, Y):
#     pass
#
#
# xy = XY()
# xy.fx()
# xy.fy()

# ----------------------------------------------------------------

# 3 - folder

# ----------------------------------------------------------------

# multilevel inheritance

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def increase_age(self):
#         self.age += 1
#
#     def __str__(self):
#         return ';'.join(f'{key}={value}'        # !!!
#                         for key, value in self.__dict__.items())
#
#
# class Employee(Person):     # Employee can use everything from Person
#     def __init__(self, name, age, field):
#         self.field = field
#         super().__init__(name, age)
#
#     def work(self):         # can use everything from Empl and Person
#         print(f"{self.name} is working in {self.field}")
#
#
# class Teacher(Employee):
#     def __init__(self, name, age, field, subject):
#         super().__init__(name, age, field)
#         self.subject = subject
#
#     def teach(self):
#         print(f"Mr. {self.name} is teaching {self.subject}")
#
#
# t = Teacher("Daniel", 39, "Education", "Python OOP")
# print(t)
# t.teach()
# t.work()
# t.increase_age()
# print(t)

# ----------------------------------------------------------------

# 4 - folder

# ----------------------------------------------------------------

# 5 - no

# ----------------------------------------------------------------
# MRO - method resolution order

# ----------------------------------------------------------------
# Mixins - mixin-a e popylvash klas, ne trqbva da imat state
# class StrMixin:
#     def __str__(self):
#         return ';'.join(f"{key}={value}"
#                         for key, value in self.__dict__.items())
#
#
# class Person(StrMixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Building(StrMixin):
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
# print(Person("Daniel", 39))
# print(Building("Softuni", "adress 17"))

# ----------------------------------------------------------------

# 6

class StringStack:
    def __init__(self):
        self.data = []

    def push(self, value):
        if isinstance(value, str):      # !!!
            raise TypeError('Only strings can be '
                            'appended to StringStack')
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)


















