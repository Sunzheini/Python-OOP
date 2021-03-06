# Encapsulation

# predpazvane i validaciq

# everything written in python is public by default
# other is private and protected and in python is only syntax

# ------------------------------------------------------------------

# class Student:
#     def __init__(self, number, id_number):     # init ne e private, a dunder
#         self.number = number
#         self.__id_number = id_number           # private
#         self._grades = [5, 6]                  # protected
#
#     def calculate_age(self):
#         year = self.__id_number[:4]
#         return year
#
#
# student = Student("1234a", "20202020202")
# print(student._Student__id_number)      # taka dostigame private
# print(student._grades)                  # mojem da dostypim protected
# print(student.calculate_age())

# ------------------------------------------------------------------
# getters and setters as functions: getter

# 1
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())

# ------------------------------------------------------------------
# setter + validation

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_name(self, value):
#         if value == "Daniel":
#             self.__name = value
#         else:
#             raise ValueError("Only 'Da'")
#
#
# person = Person("George", 32)
# person.set_name("Daniel")
# print(person.get_name())

# ------------------------------------------------------------------

# 2
# class Mammal:
#     __kingdom = "animals"
#
#     def __init__(self, name, type, sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return self.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"
#
#
# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())

# ------------------------------------------------------------------
# getter and setter pythonic way - shortcut: props

# class Person:
#     def __init__(self, age=0):
#         self.age = age      # ima ravno i izvikva settera
#                             # v sluchaq age e bez __ !!!
#     @property               # getter (property e dekorator)
#     def age(self):
#         return self.__age
#
#     @age.setter             # setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age
#
#     @property
#     def test(self):
#         return "Hello"
#
#
# p = Person(16)
# p.age = 15                  # izvikva se bez skobi
# print(p.age)
# print(p.test)

# ------------------------------------------------------------------

# class Profile:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if not (5 <= len(value) <= 15):
#             raise ValueError("The username must be between 5 and 15 characters.")
#         self.__username = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         is_length_valid = len(value) >= 8
#         is_upper_case_presented = [char for char in value if char.isupper()]
#         is_digit_case_presented = [char for char in value if char.isdigit()]
#
#         if not is_length_valid or not is_upper_case_presented or not is_digit_case_presented:
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         self.__password = value
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
#
#
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

# ------------------------------------------------------------------
# any

# print(any([]))         # False
# print(any([1, 2, 3]))  # True

# all - obratnoto

# ------------------------------------------------------------------
# name mangling of method - (ne syshtestvuvat v naslednicite)

# class Person:
#     def __init__(self):
#         self.first_name = 'Peter'
#         self.last_name = 'Parker'
#
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def info(self):
#         return self.__full_name()
#
#
# p = Person()
# print()

# ------------------------------------------------------------------

# 4
# class EmailValidator:
#     def __init__(self, min_length, mails, domains):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __is_name_valid(self, name):
#         return len(name) >= self.min_length
#
#     def __is_mail_valid(self, mail):
#         return mail in self.mails
#
#     def __is_domain_valid(self, domain):
#         return domain in self.domains
#
#     def validate(self, email):
#         username = email.split('@')[0]
#         mail, domain = email.split('@')[1].split('.')   # !!!
#
#         if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
#             return True
#         else:
#             return False
#
#
# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))

# ------------------------------------------------------------------

# 5
class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

# ------------------------------------------------------------------
# getattr()
# hasattr()
# setattr()
# delattr()
















