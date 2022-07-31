# Exercise: Iterators and Generators

# 1
# v __next__ e logikata za 1 iteraciq + logikata za prikluchvane

# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#         self.iterations = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.iterations == self.count:
#             raise StopIteration
#
#         result = self.iterations * self.step
#         self.iterations += 1
#         return result
#
#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)


# 2
# class dictionary_iter:
#     def __init__(self, data):
#         self.items = list(data.items())     # !!!
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.items):
#             raise StopIteration
#
#         result = self.items[self.index]
#         self.index += 1
#         return result
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


# 3
# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < 0:
#             raise StopIteration
#
#         result = self.count
#         self.count -= 1
#         return result
#
#
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")


# 4
# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == self.number:
#             raise StopIteration
#
#         result = self.sequence[self.index % len(self.sequence)] # !!!
#         self.index += 1
#         return result
#
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')


# 5
# def solution():
#
#     def integers():
#         num = 1
#         while 1:
#             yield num
#             num += 1
#
#     def halves():
#         for i in integers():
#             yield i / 2
#
#     def take(n, seq):
#         return [next(seq) for i in range(n)]
#
#     return (take, halves, integers)
#
#
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))


# 6
# def fibonacci():
#     first = 0
#     second = 1
#
#     yield first
#     yield second
#
#     while 1:
#         result = first + second
#         first = second
#         second = result
#         yield result
#
#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))


# 7
# def read_next(*args):
#     for n in args:
#         for el in n:
#             yield el
#
#
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')
# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)


# 8
# def is_prime(i):
#     if i <= 1:
#         return False
#
#     is_prime = True
#
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#
#     return is_prime
#
#
# def get_primes(list_of_ints):
#     for i in list_of_ints:
#         if is_prime(i):
#             yield i
#
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))


# 9
from itertools import permutations


def possible_permutations(numbers):
    for result in permutations(numbers):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
