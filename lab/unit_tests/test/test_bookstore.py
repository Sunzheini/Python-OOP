#from project.bookstore import Bookstore
from unit_tests.bookstore import Bookstore
from unittest import TestCase, main
from typing import Dict


# class Bookstore:
#     def __init__(self, books_limit: int):
#         self.books_limit = books_limit
#         self.availability_in_store_by_book_titles: Dict[str, int] = {}
#         self.__total_sold_books: int = 0

class TestBookstore(TestCase):
    BOOKS_LIMIT = 10

    def setUp(self) -> None:
        self.shop = Bookstore(self.BOOKS_LIMIT)

    def test_init(self):
        self.assertEqual(self.BOOKS_LIMIT, self.shop.books_limit)
        self.assertEqual({}, self.shop.availability_in_store_by_book_titles)
        self.assertEqual(0, self.shop.total_sold_books)

#     @property
#     def total_sold_books(self):
#         return self.__total_sold_books
#
#     @property
#     def books_limit(self):
#         return self.__books_limit
#
#     @books_limit.setter
#     def books_limit(self, value: int):
#         # the books limit cannot be equal or below zero
#         if value <= 0:
#             raise ValueError(f"Books limit of {value} is not valid")
#         self.__books_limit = value

    def test_books_limit_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.shop.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid", str(error.exception))

    def test_books_limit_raises_error2(self):
        with self.assertRaises(ValueError) as error:
            self.shop.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(error.exception))

#     # count the total number of books (copies) in the bookstore
#     def __len__(self):
#         count_books = 0
#         for number_of_books in self.availability_in_store_by_book_titles.values():
#             count_books += number_of_books
#         return count_books

    def test_len_counts_books(self):
        self.shop.availability_in_store_by_book_titles['book1'] = 2
        self.shop.availability_in_store_by_book_titles['book2'] = 3

        result = len(self.shop)

        self.assertEqual(5, result)

#     def receive_book(self, book_title: str, number_of_books: int):
#         # if there is not enough space in the bookstore
#         if len(self) + number_of_books > self.books_limit:
#             raise Exception("Books limit is reached. Cannot receive more books!")

    def test_receive_book_not_enough_space(self):
        book_title = 'book1'

        with self.assertRaises(Exception) as error:
            self.shop.receive_book(book_title, 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertEqual(0, len(self.shop))
        self.assertEqual(0, len(self.shop.availability_in_store_by_book_titles))

#         # if there is enough space in the bookstore
#         if book_title not in self.availability_in_store_by_book_titles:
#             self.availability_in_store_by_book_titles[book_title] = 0
#         self.availability_in_store_by_book_titles[book_title] += number_of_books

    def test_receive_book_enough_space(self):
        book_title = 'book1'
        self.shop.receive_book(book_title, 5)
        self.assertEqual(5, self.shop.availability_in_store_by_book_titles[book_title])
        self.assertEqual(5, len(self.shop))

#         # take the new availability of that book copies and return the result
#         total_number = self.availability_in_store_by_book_titles[book_title]
#         return f"{total_number} copies of {book_title} are available in the bookstore."

    def test_receive_book_string(self):
        book_title = 'book1'
        result = self.shop.receive_book(book_title, 5)
        self.assertEqual(f"5 copies of {book_title} are available in the bookstore.", result)
        self.assertEqual(5, self.shop.availability_in_store_by_book_titles[book_title])
        self.assertEqual(5, len(self.shop))

#     def sell_book(self, book_title: str, number_of_books: int):
#         # if the book is not available in the bookstore
#         if book_title not in self.availability_in_store_by_book_titles:
#             raise Exception(f"Book {book_title} doesn't exist!")

    def test_sell_book(self):
        book_title = 'book1'
        with self.assertRaises(Exception) as error:
            self.shop.sell_book(book_title, 5)
        self.assertEqual(f"Book {book_title} doesn't exist!", str(error.exception))
        self.assertEqual(0, len(self.shop))
        self.assertEqual(0, self.shop.total_sold_books)

#         # if there is not enough copies of that book to sell
#         if number_of_books > self.availability_in_store_by_book_titles[book_title]:
#             books_left = self.availability_in_store_by_book_titles[book_title]
#             raise Exception(f"{book_title} has not enough copies to sell. Left: {books_left}")

    def test_sell_book_not_enough_books(self):
        book_title = 'book1'
        self.shop.receive_book(book_title, 5)

        with self.assertRaises(Exception) as error:
            self.shop.sell_book(book_title, 6)
        self.assertEqual(f"{book_title} has not enough copies to sell. Left: 5", str(error.exception))

        self.assertEqual(5, self.shop.availability_in_store_by_book_titles[book_title])
        self.assertEqual(5, len(self.shop))
        self.assertEqual(0, self.shop.total_sold_books)

#         # if can sell successfully
#         self.availability_in_store_by_book_titles[book_title] -= number_of_books
#         self.__total_sold_books += number_of_books
#         return f"Sold {number_of_books} copies of {book_title}"

    def test_sell_book_successfully(self):
        book_title = 'book1'
        self.shop.receive_book(book_title, 5)
        result = self.shop.sell_book(book_title, 3)

        self.assertEqual(f"Sold 3 copies of {book_title}", result)
        self.assertEqual(2, len(self.shop))
        self.assertEqual(2, self.shop.availability_in_store_by_book_titles[book_title])
        self.assertEqual(3, self.shop.total_sold_books)

#     def __str__(self):
#         result = [f"Total sold books: {self.total_sold_books}"]
#         result.append(f'Current availability: {len(self)}')
#         for book_title, number_of_copies in self.availability_in_store_by_book_titles.items():
#             result.append(f" - {book_title}: {number_of_copies} copies")
#         return '\n'.join(result)

    def test_str(self):
        book_title = 'book1'
        book_title2 = 'book2'
        self.shop.receive_book(book_title, 5)
        self.shop.receive_book(book_title2, 2)
        self.shop.sell_book(book_title, 3)

        actual = str(self.shop)
        expected = "Total sold books: 3\n" \
                   + "Current availability: 4\n" \
                   + " - book1: 2 copies\n" \
                   + " - book2: 2 copies"

        # result = [f"Total sold books: {self.total_sold_books}"]
        # result.append(f'Current availability: {len(self)}')
        # for book_title, number_of_copies in self.availability_in_store_by_book_titles.items():
        #     result.append(f" - {book_title}: {number_of_copies} copies")
        # return '\n'.join(result)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
