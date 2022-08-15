from project_16.core.drinks_factory import DrinksFactory
from project_16.core.food_factory import FoodFactory
from project_16.core.tables_factory import TablesFactory
from project_16.core.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drinks_factory = DrinksFactory()
        self.tables_factory = TablesFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.vali_string(value, "Name cannot be empty string or white space!")
        self.__name = value

# -------------------------------------------------------------------------------------------

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return F"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.drinks_factory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = self.tables_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

# -------------------------------------------------------------------------------------------

    def reserve_table(self, number_of_people: int):
        for t in self.tables_repository:
            if t.is_reserved:
                continue
            if t.capacity >= number_of_people:
                t.reserve(number_of_people)
                return f"Table {t.table_number} " \
                       f"has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

# -------------------------------------------------------------------------------------------

    def order_food(self, table_number: int, *food_names):
        table = self.find_object_by_number(table_number, self.tables_repository)
        if table is None:
            return f"Could not find table {table_number}"
        result1 = f"Table {table_number} ordered:\n"
        result2 = f"{self.name} does not have in the menu:\n"
        for food_name in food_names:
            food = self.find_object_by_name(food_name, self.food_menu)
            if food is None:
                result2 += food_name + '\n'
            else:
                result1 += str(food) + '\n'
                table.order_food(food)
        return result1 + result2.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = self.find_object_by_number(table_number, self.tables_repository)
        if table is None:
            return f"Could not find table {table_number}"
        result1 = f"Table {table_number} ordered:\n"
        result2 = f"{self.name} does not have in the menu:\n"
        for drink_name in drink_names:
            drink = self.find_object_by_name(drink_name, self.drinks_menu)
            if drink is None:
                result2 += drink_name + '\n'
            else:
                result1 += str(drink) + '\n'
                table.order_drink(drink)
        return result1 + result2.strip()

# -------------------------------------------------------------------------------------------

    def leave_table(self, table_number: int):
        table = self.find_object_by_number(table_number, self.tables_repository)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        result = f"Table: {table_number}\n" + f"Bill: {table_bill:.2f}"
        return result

    def get_free_tables_info(self):
        result = ''
        for t in self.tables_repository:
            if not t.is_reserved:
                result += t.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

# -------------------------------------------------------------------------------------------

    @staticmethod
    def find_object_by_name(name, collection):
        for i in collection:
            if i.name == name:
                return i
        return None

    @staticmethod
    def find_object_by_number(number, collection):
        for i in collection:
            if i.table_number == number:
                return i
        return None
