from project_10.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
