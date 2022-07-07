# Inheritance

# Inheritance - nasledqvame kod ot klas
# Encapsulation - skrivane na internal state i promeni samo prez publichen interfeis
# Abstraction -
# Polymorphism -

# ----------------------------------------------------------------

# class Person:               # Person is extended by Teacher
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Teacher(Person):      # Teacher extends Person
#     pass
#
#
# t = Teacher("Daniel", 39)
# print(t.name)
# print(t.age)

# ----------------------------------------------------------------
# dobavqne na fukniconalnost

# class Person:               # Person is extended by Teacher
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Teacher(Person):      # Teacher extends Person
#     def teach(self):
#         print(f"Mr {self.name} is teaching")
#
#
# t = Teacher("Daniel", 39)
# print(t.name)
# print(t.age)

# ----------------------------------------------------------------
# super

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"


class Teacher(Person):
    def teach(self):
        print(f"Mr {self.name} is teaching")

    def __str__(self):
        return f"{super().__str__()}; subject: Python"
# dostypvame direktno state i behavious na super klasa
# samo ako pishem v naslednicheski metod, koito go ima i v roditelq


t1 = Teacher("Daniel", 39, "Python OOP", "mr")
t2 = Teacher("Maxi", 9, "C#", "maimuna")

# -2:11:45







