from product import Product

class Cart:

    def __init__(self) -> None:
        self.__quantity = []
        self.__products = []

    def add_product(self, product: Product, quantity=1) -> None:
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product object.")
        if not isinstance(quantity, int | float):
            raise TypeError("Quantity must be a number.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.__products.append(product)
        self.__quantity.append(quantity)

    def __str__(self) -> str:
        return f"Cart with {sum(self.__quantity)} items."