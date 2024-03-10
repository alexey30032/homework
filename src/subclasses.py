from classes import Product
from mixin import MixinLog


class Phone(Product):
    performance: float
    memory: int

    def __init__(self, name, description, amount, quantity_in_stock,
                 performance, model, memory, color):
        super().__init__(name, description, amount, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product):

    def __init__(self, name, description, amount, quantity_in_stock,
                 prod_country, germ_prd, color):
        super().__init__(name, description, amount, quantity_in_stock)
        self.prod_country = prod_country
        self.germ_prd = germ_prd
        self.color = color
