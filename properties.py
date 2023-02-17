class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter  # if a setter does not exist when setting the value --> AttributeError: can't set attribute 'price'
    def price(self, price):
        if price < 0:
            raise ValueError("Price can not be negative")
        self.__price = price

    # price = property(get_price, set_price) --> #could use this with the annotations
    # and prefix methods with __, but it is less clean


product = Product(1)
product.price = 5
