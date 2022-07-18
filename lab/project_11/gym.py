from project_11.customer import Customer
from project_11.equipment import Equipment
from project_11.exercise_plan import ExercisePlan
from project_11.subscription import Subscription
from project_11.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        exercise = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, exercise.equipment_id)

        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(exercise)

    def __find_by_id(self, collection, obj_id):
        for obj in collection:
            if obj.id == obj_id:
                return obj



























