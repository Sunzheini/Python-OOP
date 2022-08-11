#from project.movie import Movie
from unit_tests.movie import Movie
from unittest import TestCase

# class Movie:
#     def __init__(self, name: str, year: int, rating: float):
#         self.name = name
#         self.year = year
#         self.rating = rating
#         self.actors = []


class MovieTest(TestCase):
    NAME = 'Maymuna'
    YEAR = 2010
    RATING = 8
    MIN_YEAR = 1887

    def setUp(self):
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if value == '':
#             raise ValueError("Name cannot be an empty string!")
#         self.__name = value

    def test_name_setter_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self, value):
#         if value < 1887:
#             raise ValueError("Year is not valid!")
#         self.__year = value

    def test_year_setter_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = self.MIN_YEAR - 1
        self.assertEqual("Year is not valid!", str(error.exception))

#     def add_actor(self, name: str):
#         if name not in self.actors:
#             self.actors.append(name)
#         else:
#             return f"{name} is already added in the list of actors!"

    def test_add_actor_appends_name(self):
        first = 'Daniel'
        second = 'Maxi'
        self.movie.add_actor(first)
        self.movie.add_actor(second)
        self.assertEqual([first, second], self.movie.actors)

    def test_add_actors_raises_error(self):
        name = 'Daniel'
        self.movie.actors = [name]

        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added "
                         f"in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

#     def __gt__(self, other):
#         if self.rating > other.rating:
#             return f'"{self.name}" is better than "{other.name}"'
#         else:
#             return f'"{other.name}" is better than "{self.name}"'

    def test_gt_returns_true(self):
        another_movie_name = 'Maiiim'
        another_movie = Movie(another_movie_name, 1999, self.RATING - 1)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie

        self.assertEqual(f'"{self.movie.name}" is better '
                         f'than "{another_movie_name}"', first_result)
        self.assertEqual(f'"{self.movie.name}" is better '
                         f'than "{another_movie_name}"', second_result)

#     def __repr__(self):
#         return f"Name: {self.name}\n" \
#                f"Year of Release: {self.year}\n" \
#                f"Rating: {self.rating:.2f}\n" \
#                f"Cast: {', '.join(self.actors)}"

    def test_repr(self):
        actors = ['Daniel', 'Maxi']
        self.movie.actors = actors
        result = repr(self.movie)
        expected = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {', '.join(actors)}"

        self.assertEqual(expected, result)

