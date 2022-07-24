class Trainer:
    ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = Trainer.ID
        Trainer.ID += 1
        return result

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"








