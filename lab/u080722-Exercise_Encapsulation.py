# Exercise: Encapsulation

# 1
# from project_5.caretaker import Caretaker
# from project_5.cheetah import Cheetah
# from project_5.keeper import Keeper
# from project_5.lion import Lion
# from project_5.tiger import Tiger
# from project_5.vet import Vet
# from project_5.zoo import Zoo
#
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())


# 2
# from project_6.dough import Dough
# from project_6.pizza import Pizza
# from project_6.topping import Topping
#
#
# try:        # !!!
#     tomato_topping = Topping("Tomato", 60)
#     print(tomato_topping.topping_type)
#     print(tomato_topping.weight)
#
#     mushrooms_topping = Topping("Mushroom", 75)
#     print(mushrooms_topping.topping_type)
#     print(mushrooms_topping.weight)
#
#     mozzarella_topping = Topping("Mozzarella", 80)
#     print(mozzarella_topping.topping_type)
#     print(mozzarella_topping.weight)
#
#     cheddar_topping = Topping("Cheddar", 150)
#
#     pepperoni_topping = Topping("Pepperoni", 120)
#
#     white_flour_dough = Dough("White Flour", "Mixing", 200)
#     print(white_flour_dough.flour_type)
#     print(white_flour_dough.weight)
#     print(white_flour_dough.baking_technique)
#
#     whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
#     print(whole_wheat_dough.weight)
#     print(whole_wheat_dough.flour_type)
#     print(whole_wheat_dough.baking_technique)
#
#     p = Pizza("Margherita", whole_wheat_dough, 2)
#
#     p.add_topping(tomato_topping)
#     print(p.calculate_total_weight())
#
#     p.add_topping(mozzarella_topping)
#     print(p.calculate_total_weight())
#
#     p.add_topping(mozzarella_topping)
# except ValueError as error:
#     print(error)


# 3
# from project_7.player import Player
# from project_7.team import Team
#
#
# p = Player("Pall", 1, 3, 5, 7)
#
# print("Player name:", p.name)
# print("Points sprint:", p._Player__sprint)
# print("Points dribble:", p._Player__dribble)
# print("Points passing:", p._Player__passing)
# print("Points shooting:", p._Player__shooting)
#
# print("\ncalling the __str__ method")
# print(p)
#
# print("\nAbout the team")
# t = Team("Best", 10)
# print("Team name:", t._Team__name)
# print("Teams points:", t._Team__rating)
# print("Teams players:", len(t._Team__players))
# print(t.add_player(p))
# print(t.add_player(p))
# print("Teams players:", len(t._Team__players))
# print(t.remove_player("Pall"))
# print(t.remove_player("Pall"))


# 4
from project_8.beverage.beverage import Beverage
from project_8.food.soup import Soup
from project_8.product import Product

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)



















