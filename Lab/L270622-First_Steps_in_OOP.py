

# First Steps in OOP

# functions enable extensibility (change of requirements fot teh function)
# def get_name(number):
#     if number == 1:
#         return 'One'
#     elif number == 2:
#         return 'Two'
#     else:
#         return number
#
#
# def print_list(z):
#     for x in z:
#         if x is None:
#             continue
#         else:
#             print(get_name(x))
#
#
# ll = [1, 2, 3, 4]
# ll2 = [5, 6, 7, 8]
#
# print_list(ll)
# print_list(ll2)

# ------------------------------------------------------------------

# 1 - Rhombus of stars

# def get_line(i, n):
#     spaces_count = n - 1 - i
#     stars_count = i + 1
#
#     return ' ' * spaces_count + ('* ' * stars_count).strip()
#
#
# def create_rhombus(n):
#     for i in range(0, n, 1):
#         print(get_line(i, n))
#     for i in range(n-2, -1, -1):
#         print(get_line(i, n))
#
#
# n = int(input())
# create_rhombus(n)

# ------------------------------------------------------------------

# Scope and namespace

# # global namespace - pi and sum1 - (global for this module)
# from math import pi
#
#
# def sum1(ll):
#     # result and x - in local namespace (local for func body and class)
#     result = 1
#     for x in ll:
#         result += x
#     return result
#
#
# print(sum1([1, 2, 3, 4]))
#
# # built-in namespace
# print(sum([1, 2, 3, 4]))
#
#
# # can overwrite
# # local > global > built-in

# ------------------------------------------------------------------

# Scope
# a region of the program where a namespace is directly accessible

# global scope - for the module
# function scope
# class scope (from function scope)


text = 'Daniel'


def print_greeting():
    text = 'Maxi'
    print(text)


print_greeting()        # printira Maxi
print(text)             # printira Daniel


# pyrvo se proverqva nai-blizkiq scope

# ------------------------------------------------------------------

# 19.45h // -28:48










