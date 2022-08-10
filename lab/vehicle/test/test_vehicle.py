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
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

        self.assertEqual("Not enough fuel", str(ex.exception))

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

    def test_refuel_if_exceed_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel_in_tank(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_str_returns_correct_string(self):
        self.assertEqual(f"The vehicle has {self.HORSE_POWER}"
                         f" horse power with {self.FUEL} fuel"
                         f" left and {self.DEFAULT_FUEL_CONSUMPTION} fuel "
                         f"consumption", str(self.vehicle))


if __name__ == '__main__':
    main()
