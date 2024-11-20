from magazine import utils
from magazine.Product import Product

class Order:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return utils.calculate_total_price(self.product.price, self.quantity)
