from unittest import TestCase, main
#from project_16.pet_shop import PetShop
from unit_tests_3.pet_shop import PetShop


# class PetShop:
#     def __init__(self, name: str):
#         self.name = name
#         self.food = {}
#         self.pets = []

class PetShopTests(TestCase):
    SHOP_NAME = 'Maimunski_Shop'

    def setUp(self) -> None:
        self.shop = PetShop(self.SHOP_NAME)

    def test_init(self):
        self.assertEqual(self.SHOP_NAME, self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

# -------------------------------------------------------------------------------------------

#     def add_food(self, name: str, quantity: float):
#         if quantity <= 0:
#             raise ValueError('Quantity cannot be equal to or less than 0')
#
#         if name not in self.food:
#             self.food[name] = 0

#         self.food[name] += quantity

#         return f"Successfully added {quantity:.2f} grams of {name}."

    def test_add_food_error(self):
        with self.assertRaises(ValueError) as error:
            self.shop.add_food('Daniel', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_name_not_in_self_food(self):
        food_name = 'test_food'
        food_quantity = 100

        result = self.shop.add_food(food_name, food_quantity)

        self.assertEqual(f"Successfully added {food_quantity:.2f} grams of {food_name}.", result)
        self.assertTrue(food_name in self.shop.food)
        self.assertEqual(food_quantity, self.shop.food[food_name])

    def test_add_food_adds_to_existing_food(self):
        food_name = 'test_food'
        old_quantity = 10
        new_quantity = 15

        self.shop.food[food_name] = old_quantity
        result = self.shop.add_food(food_name, new_quantity)

        self.assertEqual(f"Successfully added {new_quantity:.2f} grams of {food_name}.", result)
        self.assertTrue(food_name in self.shop.food)
        self.assertEqual(old_quantity+new_quantity, self.shop.food[food_name])

# -------------------------------------------------------------------------------------------

#     def add_pet(self, name: str):
#         if name not in self.pets:
#             self.pets.append(name)
#             return f"Successfully added {name}."
#         raise Exception("Cannot add a pet with the same name")

    def test_add_pet_not_in(self):
        pet_name = 'Maymuna'

        result = self.shop.add_pet(pet_name)

        self.assertEqual(f"Successfully added {pet_name}.", result)
        self.assertTrue(pet_name in self.shop.pets)

    def test_add_pet_in(self):
        pet_name = 'Maymuna'
        self.shop.pets.append(pet_name)

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet(pet_name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

# -------------------------------------------------------------------------------------------

#     def feed_pet(self, food_name: str, pet_name: str):
#         if pet_name not in self.pets:
#             raise Exception(f"Please insert a valid pet name")
#
#         if food_name not in self.food:
#             return f'You do not have {food_name}'
#
#         if self.food[food_name] < 100:
#             self.add_food(food_name, 1000.00)
#             return "Adding food..."
#
#         self.food[food_name] -= 100
#         return f"{pet_name} was successfully fed"

    def test_feed_pet_error(self):
        pet_name = 'Maymuna'
        food_name = 'Chocolate'

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet(food_name, pet_name)
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_name_not_in_self_food(self):
        pet_name = 'Maymuna'
        food_name = 'Chocolate'

        self.shop.pets.append(pet_name)
        result = self.shop.feed_pet(food_name, pet_name)

        self.assertEqual(f'You do not have {food_name}', result)

    def test_add_food_less_than_100(self):
        pet_name = 'Maymuna'
        food_name = 'Chocolate'
        food_quantity = 99
        self.shop.pets.append(pet_name)
        self.shop.food[food_name] = food_quantity

        result = self.shop.feed_pet(food_name, pet_name)

        self.assertEqual("Adding food...", result)
        self.assertEqual(1000.00 + food_quantity, self.shop.food[food_name])

    def test_add_food_more_than_100(self):
        pet_name = 'Maymuna'
        food_name = 'Chocolate'
        food_quantity = 101
        self.shop.pets.append(pet_name)
        self.shop.food[food_name] = food_quantity

        result = self.shop.feed_pet(food_name, pet_name)

        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(food_quantity - 100, self.shop.food[food_name])

# -------------------------------------------------------------------------------------------

#     def __repr__(self):
#         return f'Shop {self.name}:\n' \
#                f'Pets: {", ".join(self.pets)}'

    def test_repr(self):
        self.shop.pets.append('pet1')
        self.shop.pets.append('pet2')

        expected = f'Shop {self.shop.name}:\n' + f'Pets: {", ".join(self.shop.pets)}'
        actual = repr(self.shop)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
