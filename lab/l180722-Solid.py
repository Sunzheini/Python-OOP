# Solid

#------------------------------------------------------------------
# I. Single Responsibility

# each class is responsible for only 1 thing, taka stava reusable

# def my_sum(numbers):    # nqma single responsibility, pravi 2 neshta
#     the_sum = sum(numbers)
#     print(the_sum)

#------------------------------------------------------------------
# II. Open/Closed

# open for extension but closed for modification
# by use Abstraction, Min-ins, Monkey-patching...

# da mojem pri nujda da promenim bevavior-a na 1 klas bez da mojem
# da promenqme samiq klas


class NumbersValidator:
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError("Error")


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0

# -2:02:09