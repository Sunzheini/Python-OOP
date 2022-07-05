class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for i in self.tasks:
            if i.name == task_name:
                i.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for i in self.tasks:
            if i.completed:
                self.tasks.remove(i)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = ''

        result += f"Section {self.name}:\n"
        for i in self.tasks:
            result += f"{i.details()}\n"

        return result.strip()


