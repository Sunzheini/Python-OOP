# Iterators and Generators


# iterator - obekt koito moje da hodi po state-a na nashite obekti
# for, comprehension, unpacking

# ------------------------------------------------------------------
# __iter__() - internal dunder method in class
# iter() - external for clss that calls __iter__


# print('---for loop---')
# ll = [1, 2, 3, 4, 5]
# for x in ll:
#     print(x)
#
# print('---Manual---')
# ll_iter = iter(ll)  # creates an iterator object for ll
#
# print(ll_iter)
# print(next(ll_iter))    # get next value
# print(next(ll_iter))    # get next value, etc
#
# print('---while---')
# ll_iter = iter(ll)
# while 1:
#     value = next(ll_iter)
#     print(value)

# ------------------------------------------------------------------
# 2 iteratora

# ll = [1, 2, 3, 4, 5]
#
# ll_iter1 = iter(ll)
# ll_iter2 = iter(ll)     # iteratorite sa nezavisimi

# ------------------------------------------------------------------
# StopIteration exception

# ll = [1, 2, 3, 4, 5]
#
# ll_iter = iter(ll)
# while 1:
#     try:
#         value = next(ll_iter)
#         print(value)
#     except StopIteration:
#         print('Stopped')
#         break

# ------------------------------------------------------------------

# 1
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.next_value = start
#
#     def __iter__(self):
#         return self         #samiq klas stava interator
#
#     def __next__(self):
#         if self.next_value > self.end:
#             raise StopIteration         # no more values to iterate
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

# ------------------------------------------------------------------
# class custom_range_iterator:
#     def __init__(self, cr):
#         self.cr = cr
#         self.next_value = self.cr.start
#
#     def __next__(self):
#         if self.next_value > self.cr.end:
#             raise StopIteration
#
#         value_to_return = self.next_value
#         self.next_value += 1
#         return value_to_return
#
#
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return custom_range_iterator(self)
#
#
# cr = custom_range(1, 10)
# ll = [1, 2, 3, 4, 5]
#
# cr_iter = iter(cr)
# ll_iter = iter(ll)
#
# print(cr_iter)
# print(ll_iter)

# ------------------------------------------------------------------

# 2
class reverse_iter:
    def __init__(self, values):
        self.values = values
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.values):   # !!!
            raise StopIteration
        value_to_return = self.values[self.index]
        self.index -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# ------------------------------------------------------------------
# generator - syntactic sugar vyrhu iteratori
# funkciq koqto izpolzva yield

# -1:14:35


























