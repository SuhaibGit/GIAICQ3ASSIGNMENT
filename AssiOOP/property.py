class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
print("Price:")
print(p.price)
p.price = 150
print("Price changed using setter..")
print(p.price)
del p.price
