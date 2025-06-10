class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Returns the current product quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the product quantity.
        Deactivates the product if quantity becomes 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Raises an exception if the quantity is invalid or insufficient.
        """
        if not self.active:
            raise Exception("Cannot buy inactive product.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.get_quantity():
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.get_quantity() - quantity)
        return total_price
