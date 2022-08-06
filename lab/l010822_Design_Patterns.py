# Design Patterns


# design patterns - shabloni za dizain
# reshavat problemi i davat abstrakciq vyrhu samoto reshenie
# creational, structural, behavioral

# -------------------------------------------------------------------
# Creational - abstrakciq pri syzdavane na obekti
import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_noise(self):
        pass


class Cat(Animal):
    def __init__(self, name, age):
        pass


class Dog(Animal):
    def __init__(self, name):
        pass

# 2:28:43


# -------------------------------------------------------------------
# Structural - abstrakciq vyrhu strukturata, kak razlichnite komponenti mogat da se strukturirat taka che namalin tqhnoto strukturno vzaimodeistvie


# -------------------------------------------------------------------
# Behavioral - kak si vzaimodeistvat komponentite, komunikaciqta mejdu tqh










