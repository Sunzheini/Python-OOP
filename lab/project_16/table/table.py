from abc import ABC, abstractmethod
from project_16.baked_food.baked_food import BakedFood
from project_16.core.validator import Validator
from project_16.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

# --------------------------------------------------------------------------------------------

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.vali_range(value,
                             self.min_table_number,
                             self.max_table_number,
                             self.table_error_message)
        self.__table_number = value

    @property
    @abstractmethod
    def min_table_number(self):
        return

    @property
    @abstractmethod
    def max_table_number(self):
        return

    @property
    @abstractmethod
    def table_error_message(self):
        return

# --------------------------------------------------------------------------------------------

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.vali_num(value, "Capacity has to be greater than 0!")
        self.__capacity = value

# --------------------------------------------------------------------------------------------

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for f in self.food_orders:
            bill += f.price
        for d in self.drink_orders:
            bill += d.price
        return bill

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n" + \
                     f"Type: {self.__class__.__name__}\n" + \
                     f"Capacity: {self.capacity}"
            return result











