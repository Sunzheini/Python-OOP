from project_12.animal import Animal


class Cat(Animal):
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} " \
               f"year old {self.gender} {self.__class__.__name__}" # !!!

    def make_sound(self):
        return "Meow meow!"
