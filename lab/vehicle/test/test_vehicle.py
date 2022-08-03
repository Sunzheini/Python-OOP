from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init_sets_correct_parameters(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_not_enough_raise_exception(self):
        with self.assertRaises(Exception):
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_drive_if_fuel_enough_subtract_fuel_needed(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance

        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed
        actual_result = self.vehicle.fuel

        self.assertEqual(expected_result, actual_result)

    def test_drive_if_max_distance_subtract_fuel_needed(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test4(self):    # -1.23.06
        pass

    def test5(self):
        pass

    def test6(self):
        pass


if __name__ == '__main__':
    main()
