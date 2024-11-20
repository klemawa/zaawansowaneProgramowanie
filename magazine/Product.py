from magazine import utils

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self, quantity):
        return utils.calculate_total_price(self.price, quantity)
