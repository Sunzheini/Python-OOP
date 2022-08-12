from unittest import TestCase, main
from project_14.mammal import Mammal


class TestMammal(TestCase):
    NAME = 'Daniel'
    MAMMAL_TYPE = 'gorilla'
    SOUND = 'boo'
    KINGDOM = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test_mammal_init_should_create_proper_obj(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_result(self):
        expected_result = f"{self.NAME} makes {self.SOUND}"
        actual_result = self.mammal.make_sound()

        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_returns_animals(self):
        expected_result = self.KINGDOM
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(expected_result, actual_result)

    def test_get_info_returns_proper_result(self):
        expected_result = f"{self.NAME} is of type {self.MAMMAL_TYPE}"
        actual_result = self.mammal.info()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
