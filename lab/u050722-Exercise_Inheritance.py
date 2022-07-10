# Exercise: Inheritance

# --------------------------------------------
# class Child(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

# ==

# class Child(Person):
#   pass
# --------------------------------------------

# 1
# from project.child import Child
# from project.person import Person
#
# person = Person("Peter", 25)
# child = Child("Peter Junior", 5)
# print(person.name)
# print(person.age)
# print(child.__class__.__bases__[0].__name__)

# --------------------------------------------

# 2
# from project.lizard import Lizard
# from project.mammal import Mammal
#
# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)

# --------------------------------------------

# 3
# from project.elf import Elf
# from project.hero import Hero
#
# hero = Hero("H", 4)
# print(hero.username)
# print(hero.level)
# print(str(hero))
# elf = Elf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)

# --------------------------------------------
# overwrite __str__ in superclass
# and use in child classes:

# def __str__(self):
#     return f"{self.username} of type " \
#            f"{self.__class__.__name__} " \
#            f"has level {self.level}"
# --------------------------------------------

# 4
# from project.family_car import FamilyCar
# from project.vehicle import Vehicle
#
#
# vehicle = Vehicle(50, 150)
# print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
# print(vehicle.fuel)
# print(vehicle.horse_power)
# print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)
# family_car = FamilyCar(150, 150)
# family_car.drive(50)
# print(family_car.fuel)
# family_car.drive(50)
# print(family_car.fuel)
# print(family_car.__class__.__bases__[0].__name__)

# --------------------------------------------

# 5
from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)






