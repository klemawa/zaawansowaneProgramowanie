from magazine.Product import Product
from magazine.Order import Order

if __name__ == "__main__":
    product = Product(name="Laptop", price=1500)
    order = Order(product=product, quantity=3)

    total = order.total_price()
    print(f"Total price for {order.quantity} {product.name}(s): ${total}")
