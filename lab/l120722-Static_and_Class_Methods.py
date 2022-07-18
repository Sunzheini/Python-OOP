# Static and Class Methods


# method sys "self" e instance method
#------------------------------------------------------------
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
#
# print(Person.is_adult(5))  # po-pravilno e da se izpolzva taka
# girl = Person("Amy")
# print(girl.is_adult(20))   # no moje da se izpolzva i taka

#------------------------------------------------------------

# 1
# from functools import reduce            # !!!
# # izvajda po 2 neshta i reducira spisyka
#
# class Calculator:
#
#     @staticmethod
#     def add(*args):
#         return reduce(lambda x, y: x + y, args)
#
#     @staticmethod
#     def multiply(*args):
#         return reduce(lambda x, y: x * y, args)
#
#     @staticmethod
#     def divide(*args):
#         return reduce(lambda x, y: x / y, args)
#
#     @staticmethod
#     def subtract(*args):
#         return reduce(lambda x, y: x - y, args)
#
#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

#------------------------------------------------------------
# Class methods

# class Student:
#     kind = "human"
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def change_kind(cls):       # kato self no kym klasa
#         cls.kind = "asd"
#
#
# s1 = Student("Test 1'")
# s2 = Student("Test 2'")
# print(s1.kind)
# print(s2.kind)
#
# s1.change_kind()    #kazahme samo prez s1, no promenihme za vsuchki
# print(s1.kind)
# print(s2.kind)


# syzdavane kontrolirano na instancii / shortcut for creating instance objects

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])   # instanciq na Pizza([...])
#
#     @classmethod
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
#
#
# first_pizza = Pizza.pepperoni()
# second_pizza = Pizza.quattro_formaggi()

#--------------------------------------------------------------

# 2
# class Shop:
#
#     def __init__(self, name, type, capacity):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#         self.items = {}
#
#     @classmethod
#     def small_shop(cls, name, type):
#         return cls(name, type, 10)
#
#     def add_item(self, item_name):
#         if self.capacity > sum(self.items.values()):               # dict list!!!
#             if item_name not in self.items:
#                 self.items[item_name] = 0
#             self.items[item_name] += 1
#             return f"{item_name} added to the shop"
#         return "Not enough capacity in the shop"
#
#     def remove_item(self, item_name, amount):
#         if item_name in self.items and self.items[item_name] >= amount:
#             self.items[item_name] -= amount
#             if self.items[item_name] == 0:
#                 del self.items[item_name]                       # !!!
#             return f"{amount} {item_name} removed from the shop"
#         return f"Cannot remove {amount} {item_name}"
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type} with capacity {self.capacity}"
#
#
# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)

#--------------------------------------------------------------

# 3
# class Integer:
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def from_float(cls, float_value):
#         if not isinstance(float_value, float):
#             return "value is not a float"
#         return cls(int(float_value))
#
#     @classmethod
#     def from_roman(cls, value):
#         roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         result = 0
#         for i, c in enumerate(value):
#             if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
#                 result += roman_numerals[c]
#             else:
#                 result -= roman_numerals[c]
#         return cls(result)
#
#     @classmethod
#     def from_string(cls, value):
#         try:
#             if not isinstance(value, str):
#                 raise ValueError
#             return cls(int(value))
#         except ValueError:
#             return "wrong type"
#
#
# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))

#--------------------------------------------------------------
# Overriding using class methods



#--------------------------------------------------------------

# 4
# from project_9.hotel import Hotel
# from project_9.room import Room
#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())






























