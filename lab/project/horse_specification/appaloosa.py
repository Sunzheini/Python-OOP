from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    SPEED_INCREASE_WHILE_TRAINED = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def maximum_speed(self):
        return self.MAXIMUM_SPEED

    def train(self):
        self.speed += self.SPEED_INCREASE_WHILE_TRAINED
        if self.speed > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED




