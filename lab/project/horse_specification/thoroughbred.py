from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    SPEED_INCREASE_WHILE_TRAINED = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def maximum_speed(self):
        return self.MAXIMUM_SPEED

    def train(self):
        self.speed += self.SPEED_INCREASE_WHILE_TRAINED
        if self.speed > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
