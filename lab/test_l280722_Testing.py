from unittest import TestCase
from l280722_Testing import Person


class TestPerson(TestCase):
    # act__arrange__assert for test naming
    def test_fullname__expect_to_be_correct(self):
        # Arrange
        person = Person("Daniel", "Zorov", 40)

        # Act
        actual_fullname = person.fullname

        # Assert
        expected_fullname = "Daniel Zorov"
        self.assertEqual(expected_fullname, actual_fullname)

