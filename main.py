from product import Product
from cart import Cart
from exception import MoneyError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == "__main__":
    try:
        pr_1 = Product("Phone", 1)
        pr_2 = Product("Laptop", 500)
        pr_3 = Product("Tablet", 300)

        cart = Cart()
        cart.add_product(pr_1, 3)
        cart.add_product(pr_2, 1)
        cart.add_product(pr_3, 3)

        print(cart)
    except Exception as e:
        logger.exception("Exception occurred")