from project_3.employee import Employee
from project_3.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
