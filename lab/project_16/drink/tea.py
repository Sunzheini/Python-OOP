from project_16.drink.drink import Drink


class Tea(Drink):
    TEA_PRICE = 2.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.TEA_PRICE, brand)




