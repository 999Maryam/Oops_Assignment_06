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

if __name__ == "__main__":
    p = Product(200)
    print(p.price)  # prints: 200
    p.price = 300
    print(p.price)  # prints: 300
    del p.price
    print(p.price)