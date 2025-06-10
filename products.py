from abc import ABC, abstractmethod

# --- Promotions ---

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = product.price * (self.percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        half_price_items = quantity // 2
        full_price_items = quantity - half_price_items
        return full_price_items * product.price + half_price_items * (product.price / 2)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        chargeable_items = quantity - free_items
        return chargeable_items * product.price


# --- Products ---

class Product:
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
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promo_str = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo_str}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Cannot buy inactive product.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.get_quantity():
            raise Exception("Not enough quantity in stock.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.get_quantity() - quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        # quantity is always 0, so ignore any attempts to set
        pass

    def get_quantity(self):
        return 0

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self):
        promo_str = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited{promo_str}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum  # 💡 Hier war vorher der Fehler!

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of this product.")
        return super().buy(quantity)

    def show(self):
        promo_str = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!{promo_str}"
