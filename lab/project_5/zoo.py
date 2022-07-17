from project_5.caretaker import Caretaker
from project_5.keeper import Keeper
from project_5.lion import Lion
from project_5.tiger import Tiger
from project_5.cheetah import Cheetah
from project_5.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if worker_name == i.name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = 0
        for i in self.workers:
            sum_of_salaries += i.salary

        if sum_of_salaries <= self.__budget:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_money_for_care = 0
        for i in self.animals:
            sum_of_money_for_care += i.money_for_care

        if sum_of_money_for_care <= self.__budget:
            self.__budget -= sum_of_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]  # !!!
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]

        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs) + '\n'

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]  # !!!
        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]

        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets) + '\n'

        return result.strip()





















