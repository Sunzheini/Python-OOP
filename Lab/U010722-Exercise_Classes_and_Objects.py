# Exercise: Classes and Objects

# 1

# class Vet:
#
#     animals = []
#     space = 5
#
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if Vet.space > 0:                           # !!!
#
#             self.animals.append(animal_name)
#             Vet.animals.append(animal_name)         # !!!
#
#             Vet.space -= 1
#             return f"{animal_name} registered in the clinic"
#         else:
#             return "Not enough space"
#
#     def unregister_animal(self, animal_name):
#         if animal_name in self.animals:
#             self.animals.remove(animal_name)
#             Vet.animals.remove(animal_name)
#             Vet.space += 1
#             return f"{animal_name} unregistered successfully"
#         else:
#             return f"{animal_name} not in the clinic"
#
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())


# 2
# class Time:
#
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"    # !!!
#
#     def next_second(self):
#
#         self.seconds += 1
#
#         if self.seconds > self.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#
#         if self.minutes > self.max_minutes:
#             self.minutes = 0
#             self.hours += 1
#
#         if self.hours > self.max_hours:
#             self.hours = 0
#
#         return self.get_time()
#
#
# time = Time(9, 30, 59)
# print(time.next_second())


# 3

# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         else:
#             return "Amount exceeded balance"
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"
#
#
# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())


# 4

# class PizzaDelivery:
#     def __init__(self, name, price, ingredients):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
#
#         if not self.ordered:
#
#             if ingredient in self.ingredients.keys():
#                 self.ingredients[ingredient] += quantity
#                 self.price += quantity * price_per_quantity
#             else:
#                 self.ingredients[ingredient] = quantity
#                 self.price += quantity * price_per_quantity
#         else:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
#
#         if not self.ordered:
#
#             if ingredient not in self.ingredients.keys():
#                 return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#             elif ingredient in self.ingredients.keys() and quantity > self.ingredients[ingredient]:
#                 return f"Please check again the desired quantity of {ingredient}!"
#             else:
#                 self.ingredients[ingredient] -= quantity
#                 self.price -= quantity * price_per_quantity
#         else:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#
#     def make_order(self):
#         self.ordered = True
#
#         # !!!
#         result = ', '.join([f"{key}: {value}" for key, value in self.ingredients.items()])
#
#         return f"You've ordered pizza {self.name} prepared " \
#                f"with {result} and the price will be {self.price}lv."
#
#
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))


# 5 + folder

# from project.task import Task
# from project.section import Section
#
#
# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())


# 6 + folder
from project.guild import Guild
from project.player import Player


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


# -1:26:04













