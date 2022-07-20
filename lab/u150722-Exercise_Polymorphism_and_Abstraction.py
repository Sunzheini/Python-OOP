# Exercise: Polymorphism and Abstraction

# 1
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
#
# class Car(Vehicle):
#     AIR_CONDITIONER = 0.9
#
#     def drive(self, distance):
#         if self.fuel_quantity >= distance * (self.fuel_consumption + self.AIR_CONDITIONER):
#             self.fuel_quantity -= distance * (self.fuel_consumption + self.AIR_CONDITIONER)
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle):
#     AIR_CONDITIONER = 1.6
#
#     def drive(self, distance):
#         if self.fuel_quantity >= distance * (self.fuel_consumption + self.AIR_CONDITIONER):
#             self.fuel_quantity -= distance * (self.fuel_consumption + self.AIR_CONDITIONER)
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel * 0.95
#
#
# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)


# 2
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
#
#
# class Group:
#     def __init__(self, name, people):
#         self.name = name
#         self.people = people
#
#     def __len__(self):
#         return len(self.people)
#
#     def __add__(self, other):
#         new_name = f"{self.name} {other.name}"
#         new_list = self.people + other.people
#         return Group(new_name, new_list)
#
#     def __str__(self):
#         people_str = ', '.join([str(x) for x in self.people])
#         return f"Group {self.name} with members " \
#                f"{people_str}"
#
#     def __getitem__(self, index):                 # !!!
#         return f"Person {index}: {str(self.people[index])}"
#
#
# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# print(third_group[0])
#
# for person in third_group:
#     print(person)


# 3
# class Account:
#     def __init__(self, owner, amount=0):
#         self.owner = owner
#         self.amount = amount
#         self._transactions = []
#
#     def add_transaction(self, amount):
#         if not isinstance(amount, int):
#             raise ValueError("please use int for amount")
#         self._transactions.append(amount)
#
#     @property
#     def balance(self):
#         return self.amount + sum(self._transactions)
#
#     @staticmethod
#     def validate_transaction(account, amount_to_add):
#         if account.balance + amount_to_add < 0:
#             raise ValueError("sorry cannot go in debt!")
#
#         account.add_transaction(amount_to_add)
#         return f"New balance: {account.balance}"
#
#     def __str__(self):
#         return f"Account of {self.owner} with starting " \
#                f"amount: {self.amount}"
#
#     def __repr__(self):
#         return f"Account({self.owner}, {self.amount})"
#
#     def __len__(self):
#         return len(self._transactions)
#
#     def __getitem__(self, index):
#         return self._transactions[index]        # !!!
#
#     def __reversed__(self):         # !!!
#         return reversed(self._transactions)
#
#     def __gt__(self, other):
#         return self.amount > other.amount
#
#     def __ge__(self, other):
#         return self.amount >= other.amount
#
#     def __eq__(self, other):
#         return self.amount == other.amount
#
#     def __add__(self, other):
#         name = self.owner + '&' + other.owner
#         starting_amount = self.amount + other.amount
#         new_acc = Account(name, starting_amount)        # !!!
#
#         new_acc._transactions = self._transactions + other._transactions
#
#         return new_acc
#
#
# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)


# 4
# from project_13.animals.birds import Owl
# from project_13.food import Meat, Vegetable
#
# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)


# 5
from project_12.dog import Dog
from project_12.tomcat import Tomcat

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)

















