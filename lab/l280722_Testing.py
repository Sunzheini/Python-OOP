# Testing


# -------------------------------------------------------------------
# unit tests
# integration tests
# functional tests

# -------------------------------------------------------------------
# Tripple A

# Arrange - podgotvi si neshtata
# Act - testvai
# Assert - oceni

# -------------------------------------------------------------------
# unit testig - testvat individualni komponenti

# nai dobre e da se pravqt v momenta na development
# testcase == test
# test suite == mnojestvo testove

# import unittest
# from unittest import TestCase   # kazva se TestCase no e test suite
#
#
# class FirstTests(TestCase):
#     def test_expect_1_to_equal_1(self):     # testcase
#         self.assertEqual(1, 1)      # proverqva i reportva rezultata
#
#     def test_expect_1_to_equal_2(self):
#         self.assertEqual(1, 2)
#
#
# # test runner - neshtoto koeto startira samite testove
# if __name__ == '__main__':      # mojem da startirame izvyn pycharm
#     unittest.main()

# -------------------------------------------------------------------
# assert

# import unittest
# from unittest import TestCase   # kazva se TestCase no e test suite
#
#
# class FirstTests(TestCase):
#     def test_assertEqual(self):
#         self.assertEqual(1, 1)
#
#     def test_assertTrue(self):
#         self.assertTrue(True)       # checks if true
#
#     def test_assertList(self):
#         self.assertListEqual([1, 2, 3], [2, 3, 3])
#
#
# if __name__ == '__main__':
#     unittest.main()

# -------------------------------------------------------------------
# setUp

# import unittest
# from random import random
# from unittest import TestCase
#
#
# class FirstTests(TestCase):
#     x = None
#
#     def setUp(self) -> None:    #runs before each test
#         self.x = random()
#
#     def test_assertEqual(self):
#         print(self.x)
#         self.assertEqual(1, 1)
#
#
# if __name__ == '__main__':
#     unittest.main()

# -------------------------------------------------------------------

# class Person:   # vyrhu Person dqsno kopche / generate / test / ok
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def fullname(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_info(self):
#         return f"My name is {self.fullname} and I am {self.age}-years old!"

# -------------------------------------------------------------------
# tearDown, setUpClass, tearDownClass

# from unittest import TestCase
#
#
# class TestPerson(TestCase):
#
#     def setUpClass(cls) -> None:    #once per class before all tests
#         pass
#
#     def setUp(self) -> None:
#         pass
#
#     def test_fullname__expect_to_be_correct(self):
#         pass
#
#     def tearDown(self) -> None:     # runs after each test
#         pass
#
#     def tearDownClass(cls) -> None:    # runs once after all tests
#         pass

# -------------------------------------------------------------------
# 1
# import unittest
#
#
# class Worker:
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'
#
#
# '''
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with correct values
#
# '''
#
#
# class WorkerTests(unittest.TestCase):
#     NAME = 'Test Worker'
#     SALARY = 1024
#     ENERGY = 1
#
#     def setUp(self) -> None:
#         self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)
#
#     # act__arrange__assert
#     def test__init__when_valid_props__expect_correct_values(self):
#         self.assertEqual(self.NAME, self.worker.name)
#         self.assertEqual(self.SALARY, self.worker.salary)
#         self.assertEqual(self.ENERGY, self.worker.energy)
#         self.assertEqual(0, self.worker.money)
#
#     def test__rest__expect_energy_to_be_incremented(self):
#         self.worker.rest()
#         self.assertEqual(self.ENERGY + 1, self.worker.energy)
#
#     def test__work__when_energy_is_0_expect_to_raise(self):
#         worker = Worker(self.NAME, self.SALARY, 0)
#
#         with self.assertRaises(Exception) as ex:
#             worker.work()
#
#         self.assertIsNotNone(ex)
#
#     def test__work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
#         self.worker.work()
#         self.worker.work()
#
#         self.assertEqual(2 * self.SALARY, self.worker.money)
#
#     def test__work__when_enough_energy__expect_energy_to_increment(self):
#         self.assertEqual(self.ENERGY - 1, self.worker.energy)
#
#     def test__get_info__expect_correct_results(self):
#         actual_info = self.worker.get_info()
#         expected_info = f"{self.NAME} has saved {0} money."
#
#         self.assertEqual(expected_info, actual_info)

# -------------------------------------------------------------------
# 2
# import unittest
#
#
# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         self.fed = False
#         self.sleepy = False
#         self.size = 0
#
#     def eat(self):
#         if self.fed:
#             raise Exception('Already fed.')
#
#         self.fed = True
#         self.sleepy = True
#         self.size += 1
#
#     def sleep(self):
#         if not self.fed:
#             raise Exception('Cannot sleep while hungry')
#
#         self.sleepy = False
#
#
# class CatTests(unittest.TestCase):
#     NAME = 'Pepelyashka'
#
#     def setUp(self) -> None:
#         self.cat = Cat(self.NAME)
#
#     def test_eat__expect_size_to_increment(self):
#         self.cat.eat()
#         self.assertEqual(1, self.cat.size)
#
#     def test_eat__expect_fed_to_be_true(self):
#         self.cat.eat()
#         self.assertTrue(self.cat.fed)
#
#     def test_eat__when_fed_is_true__expect_to_raise(self):
#         self.cat.eat()
#         with self.assertRaises(Exception) as ex:
#             self.cat.eat()
#
#         self.assertIsNotNone(ex)
#
#     def test_sleep__when_fed_is_false__expect_to_raise(self):
#         self.cat.sleep()
#
#         with self.assertRaises(Exception) as ex:
#             self.cat.sleep()
#
#         self.assertIsNotNone(ex)
#
#     def test_sleep__expect_sleepy_to_be_false(self):
#         self.cat.eat()
#         self.cat.sleep()
#
#         self.assertFalse(self.cat.sleepy)
#
#
# if __name__ == '__main__':
#     unittest.main()

# -------------------------------------------------------------------
# mocking - za konkreten test da pravim neshto drugo

# @patch('file.function')
# def test__name(self, mock_name_validator):
#     mock_name_validator.validate_name =

# -------------------------------------------------------------------

# extended_list

# class IntegerList:
#     def __init__(self, *args):
#         self.__data = []
#         for x in args:
#             if type(x) == int:
#                 self.__data.append(x)
#
#     def get_data(self):
#         return self.__data
#
#     def add(self, element):
#         if not type(element) == int:
#             raise ValueError("Element is not Integer")
#         self.get_data().append(element)
#         return self.get_data()
#
#     def remove_index(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         a = self.get_data()[index]
#         del self.get_data()[index]
#         return a
#
#     def get(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         return self.get_data()[index]
#
#     def insert(self, index, el):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         elif not type(el) == int:
#             raise ValueError("Element is not Integer")
#
#         self.get_data().insert(index, el)
#
#     def get_biggest(self):
#         a = sorted(self.get_data(), reverse=True)
#         return a[0]
#
#     def get_index(self, el):
#         return self.get_data().index(el)

# -------------------------------------------------------------------
# car_manager

class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)
















