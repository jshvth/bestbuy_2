from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the promotion logic to a given product and quantity.
        Must return the total price after discount.
        """
        pass


class PercentDiscount(Promotion):
    """
    Applies a percentage discount to the total price.
    """

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """
    Every second product is half price.
    """

    def apply_promotion(self, product, quantity):
        full_price_count = quantity // 2
        half_price_count = quantity - full_price_count
        return full_price_count * product.price + half_price_count * product.price * 0.5


class ThirdOneFree(Promotion):
    """
    Every third item is free.
    """

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        payable_quantity = quantity - free_items
        return payable_quantity * product.price
