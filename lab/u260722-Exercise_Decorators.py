# Exercise: Decorators

# 1
# def logged(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         my_string = f"you called {func_ref.__name__}{args}\n"
#         my_string += f"it returned {result}"
#         return my_string
#     return wrapper
#
#
# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))


# 2
# def even_parameters(func_ref):
#     def wrapper(*args):
#
#         for i in args:
#             if not isinstance(i, int) or i % 2 != 0:
#                 return "Please use only even numbers!"
#
#         result = func_ref(*args)
#         return result
#
#     return wrapper
#
#
# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))


# 3
# def make_bold(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return '<b>' + result + '</b>'
#     return wrapper
#
#
# def make_italic(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return '<i>' + result + '</i>'
#     return wrapper
#
#
# def make_underline(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return '<u>' + result + '</u>'
#     return wrapper
#
#
# @make_bold
# @make_italic
# @make_underline           # pyrvo se izpylnqva dolniq
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))


#           priemane na parametri !!!
# 4
# def type_check(params):             # !!! razlika ot predhodnite
#
#     def decorator(func_ref):
#         def wrapper(argument):
#             if not isinstance(argument, params):
#                 return "Bad Type"
#             result = func_ref(argument)
#             return result
#         return wrapper
#
#     return decorator                # !!! razlika ot predhodnite
#
#
# @type_check(int)
# def times2(num):
#     return num*2
#
#
# print(times2(2))
# print(times2('Not A Number'))
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))


# 5         # cache + funkciq s atribut

# def cache(func_ref):
#
#     memo = {}               # !!!
#
#     def wrapper(n):
#         if n in memo:
#             return memo[n]
#         result = func_ref(n)
#         memo[n] = result
#         return result
#
#     wrapper.log = memo      # !!!
#
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# fibonacci(3)
# print(fibonacci.log)        # !!!


# 6
# def tags(param):
#
#     def decorator(func_ref):
#         def wrapper(*args):
#             result = func_ref(*args)
#             a_string = f"<{param}>{result}</{param}>"
#             return a_string
#         return wrapper
#
#     return decorator
#
#
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
#
#
# print(join_strings("Hello", " you!"))


# 7
# def store_results(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         with open('./results.txt', 'a') as file:
#             file.write(f"Function '{func_ref.__name__}' was called. Result: {result}")
#             file.write('\n')
#             return result
#     return wrapper
#
#
# @store_results
# def add(a, b):
#     return a + b
#
#
# @store_results
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)


# 8
import time


def exec_time(func_ref):
    def wrapper(*args):
        start = time.time()
        func_ref(*args)
        end = time.time()
        result = end - start
        return result
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())

























