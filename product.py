from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class ProductImpl(Product):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def to_dict(self):
        return {
            "name": self.get_name(),
            "description": self.get_description(),
            "price": self.get_price(),
        }
