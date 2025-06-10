from products import Product

class Store:
    """
    Represents a store that holds a list of products.
    """

    def __init__(self, products=None):
        self.products = products if products else []

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all active products."""
        return sum(p.get_quantity() for p in self.products if p.is_active())

    def get_all_products(self) -> list:
        """Returns a list of all active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes an order and returns the total price.
        Shopping list is a list of (Product, quantity) tuples.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
