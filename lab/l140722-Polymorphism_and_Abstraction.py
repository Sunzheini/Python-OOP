# Polymorphism and Abstraction

# ---------------------------------------------------------------
# Polymorhism

# # izbqgvane na if-ove
# i.e. overwriting methods of parent class

# 1
# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def sensors_amount():
#         return 1
#
#
# class MedicalRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 6
#
#
# class ChefRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 4
#
#
# class WarRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 12
#
#
# def number_of_robot_sensors(robot):
#     print(robot.sensors_amount())
#
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
#
# number_of_robot_sensors(basic_robot)
# number_of_robot_sensors(da_vinci)
# number_of_robot_sensors(moley)
# number_of_robot_sensors(griffin)

# ---------------------------------------------------------------
# Overloading built-in methods

#print(da_vinci + chef_robot) == print(da_vinci.add__(chef_robot))

# mojem da prenapishem matematicheskite operatori i op za sravnenie
# == sravnqva po id-to v pametta, t.e. ako sa razlichni lokaciite e !=
# ako imame prenapisan __gt__, nqma nujda za __lt__
# ako imame prenapisan __ge__, nqma nujda za __le__
# ako imame prenapisan __eq__, nqma nujda za __ne__

# 2
# class ImageArea:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def __gt__(self, other):
#         return self.get_area() > other.get_area()
#
#     def __ge__(self, other):
#         return self.get_area() >= other.get_area()
#
#     def __lt__(self, other):
#         return self.get_area() < other.get_area()
#
#     def __le__(self, other):
#         return self.get_area() <= other.get_area()
#
#     def __eq__(self, other):
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):
#         return self.get_area() != other.get_area()
#
#
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)

# ---------------------------------------------------------------
# duck typing - type system used in dynamic languages
# we don't care about object type but whether they have the methods we need

# 3
# def start_playing(obj):
#     return obj.play()
#
#
# class Guitar:
#     def play(self):
#         return "Playing the guitar"
#
#
# guitar = Guitar()
# print(start_playing(guitar))

# ---------------------------------------------------------------
# Abstraction - nasilvame na polimorhisma

# ne moje da se pravi instanciq ot abstracten
# trqbva da ima tozi import i (ABC) i pone 1 abstracten method


# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     # kogato imash naslednik na Animal
#     # toi zadyljitelno trqbva da prenapishe make_sound v nego
#     def make_sound(self):
#         pass
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) < 2:
#             raise ValueError("Cant")
#         self.__name = value
#
#
# class Cat(Animal):
#     def __init__(self, name, laziness):
#         super().__init__(name)
#         self.laziness = laziness
#
#     def make_sound(self):
#         return "meow"

# ---------------------------------------------------------------

# 4
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())































