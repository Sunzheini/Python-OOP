

# Exercise: First Steps in OOP

# 1
# class Shop:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items
#
#     def get_items_count(self):
#         return len(self.items)
#
#
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())


# 2
# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def defend(self, damage):
#         self.health -= damage
#         if self.health <= 0:
#             self.health = 0
#             return f"{self.name} was defeated"
#
#     def heal(self, amount):
#         self.health += amount
#
#
# hero = Hero("Peter", 100)
# print(hero.defend(50))
# hero.heal(50)
# print(hero.defend(99))
# print(hero.defend(1))


# 3
# class Employee:
#     def __init__(self, id, first_name, last_name, salary):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_annual_salary(self):
#         return 12 * self.salary
#
#     def raise_salary(self, amount):
#         self.salary += amount
#         return self.salary
#
#
# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())


# 4
# class Cup:
#     def __init__(self, size: int, quantity: int):
#         self.size = size
#         self.quantity = quantity
#
#     def fill(self, milliliters):
#         if self.status() >= milliliters:   # izpolzvane na method vytre
#             self.quantity += milliliters
#
#     def status(self):
#         return self.size - self.quantity
#
#
# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())


# 5
class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

# ---------------------------------------------------------------
# -1:23:10