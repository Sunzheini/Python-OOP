# Exercise: SOLID

# 1
# from abc import ABC, abstractmethod
#
#
# class BaseWorker(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class Worker(BaseWorker):
#     def work(self):
#         print("I'm working!!")
#
#
# class SuperWorker(BaseWorker):
#     def work(self):
#         print("I work very hard!!!")
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, BaseWorker), f'`worker` must be of type {BaseWorker}'
#           # proverka dali e worker inache hvyrlq error
#           # ako ne e True - raise AssertionError s dadeniq message (syntactic sugar)
#         self.worker = worker
#
#     def manage(self):
#         if self.worker is not None:
#             self.worker.work()
#
#
# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
#
# super_worker = SuperWorker()
# try:
#     manager.set_worker(super_worker)
#     manager.manage()
# except AssertionError:
#     print("manager fails to support super_worker....")

#------------------------------------------------------------------


# 2
# from abc import abstractmethod, ABC
# import time
#
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class Eatable(ABC):
#     def eat(self):
#         pass
#
#
# class Worker(Workable, Eatable):
#
#     def work(self):
#         print("I'm normal worker. I'm working.")
#
#     def eat(self):
#         print("Lunch break....(5 secs)")
#         time.sleep(5)
#
#
# class SuperWorker(Workable, Eatable):
#
#     def work(self):
#         print("I'm super worker. I work very hard!")
#
#     def eat(self):
#         print("Lunch break....(3 secs)")
#         time.sleep(3)
#
#
# class Robot(Workable):
#
#     def work(self):
#         print("I'm a robot. I'm working....")
#
#
# class Manager(ABC):
#     def __init__(self):
#         self.worker = None
#
#     @abstractmethod
#     def set_worker(self, worker):
#         pass
#
#
# class WorkManager(Manager):
#     def set_worker(self, worker):
#         assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)
#         self.worker = worker
#
#     def manage(self):
#         self.worker.work()
#
#
# class BreakManager(Manager):
#     def set_worker(self, worker):
#         assert isinstance(worker, Eatable), "`worker` must be of type {}".format(Eatable)
#         self.worker = worker
#
#     def lunch_break(self):
#         self.worker.eat()
#
#
# work_manager = WorkManager()
# break_manager = BreakManager()
#
# work_manager.set_worker(Worker())
# break_manager.set_worker(Worker())
#
# work_manager.manage()
# break_manager.lunch_break()
#
# work_manager.set_worker(SuperWorker())
# break_manager.set_worker(SuperWorker())
#
# work_manager.manage()
# break_manager.lunch_break()
#
# work_manager.set_worker(Robot())
# work_manager.manage()
#
# try:
#     break_manager.set_worker(Robot())
#     break_manager.lunch_break()
#
# except Exception as error:
#     print(error)


# 3
from copy import copy


# class Person:
#     def __init__(self, position):
#         self.position = position
#
#
# class FreePerson(Person):
#     def walk_north(self, dist):
#         self.position[1] += dist
#
#     def walk_east(self, dist):
#         self.position[0] += dist
#
#
# class Prisoner(Person):
#     PRISON_LOCATION = [3, 3]
#
#     def __init__(self):
#         super(Prisoner, self).__init__(copy(self.PRISON_LOCATION))
#
#
# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
#
# except Exception as error:
#     print(error)
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")

#------------------------------------------------------------------
# copy

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# print(b)    # taka a i b sa ednakvi


# from copy import copy
# a = [1, 2, 3]
# b = copy(a)     # b e na drugo mqsto v pametta
# b.append(4)
# print(a)
# print(b)    # taka a i b sa razlichni

#------------------------------------------------------------------

# 4
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def calc_area(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def calc_area(self):
#         return self.side * self.side
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calc_area(self):
#         return self.width * self.height
#
#
# class AreaCalculator:
#     def __init__(self, shapes):
#         assert isinstance(shapes, list), "`shapes` should be of type `list`."
#         self.shapes = shapes
#
#     @property
#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.calc_area()
#         return total
#
#
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)


# 5
from abc import ABCMeta, abstractmethod, ABC


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def __init__(self, text):
        super().__init__(text)

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HtmlContent(IContent):
    def __init__(self, text):
        super().__init__(text)

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class IEmail(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content:IContent):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender,
                               receiver=self.__receiver,
                               content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)



















