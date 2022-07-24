# Solid

#------------------------------------------------------------------
# I. Single Responsibility

# each class is responsible for only 1 thing, taka stava reusable

# def my_sum(numbers):    # nqma single responsibility, pravi 2 neshta
#     the_sum = sum(numbers)
#     print(the_sum)

#------------------------------------------------------------------
# II. Open/Closed

# open for extension but closed for modification
# by use Abstraction, Min-ins, Monkey-patching...

# da mojem pri nujda da promenim bevavior-a na 1 klas bez da mojem
# da promenqme samiq klas


# class NumbersValidator:
#     min_value = 0
#     max_value = 1024
#
#     def validate(self, value):
#         if value < self.min_value or self.max_value < value:
#             raise ValueError("Error")
#
#
# class NegativeNumbersValidator(NumbersValidator):
#     min_value = -1024
#     max_value = 0

#------------------------------------------------------------------
# III. Liskov substitution

# vseki naslednik da se dyrji kato roditel
# napr. ako roditelq raise-va exception i naslednika trqbva

#------------------------------------------------------------------
# IV. Interface segregation

# edin klas ne trqbva da ima metodi koito ne izpolzva
# po dobre mnogo klasove s po 1 metod, otklokoto 1 klas s mnogo metodi

#------------------------------------------------------------------
# V. Dependency inversion

# ne trqbva da razchitame na konkretiki a na abstrakcii

#------------------------------------------------------------------

# 1
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page

#------------------------------------------------------------------

# 2
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# # animals = [Animal('cat'), Animal('dog'), Animal('chicken')]

#------------------------------------------------------------------

# 3
# from abc import abstractmethod, ABC
#
#
# class Duck(ABC):
#     @staticmethod
#     def quack():
#         pass
#
#     @staticmethod
#     def walk():
#         pass
#
#     @staticmethod
#     def fly():
#         pass
#
#
# class RubberDuck(Duck):
#     @staticmethod
#     def quack():
#         return "Squeek"
#
#     @staticmethod
#     def walk():
#         """Rubber duck can walk only if you move it"""
#         raise Exception('I cannot walk by myself')
#
#     @staticmethod
#     def fly():
#         """Rubber duck can fly only if you throw it"""
#         raise Exception('I cannot fly by myself')
#
#
# class RobotDuck(Duck):
#     HEIGHT = 50
#
#     def __init__(self):
#         self.height = 0
#
#     @staticmethod
#     def quack():
#         return 'Robotic quacking'
#
#     @staticmethod
#     def walk():
#         return 'Robotic walking'
#
#     def fly(self):
#         """can only fly to specific height but
#         when it reaches it starts landing automatically"""
#         if self.height == RobotDuck.HEIGHT:
#             self.land()
#         else:
#             self.height += 1
#
#     def land(self):
#         self.height = 0

#------------------------------------------------------------------

# 4
# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class DVDPlayer(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)

#------------------------------------------------------------------

# 5
class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book




























