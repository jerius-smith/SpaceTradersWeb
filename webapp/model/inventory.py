from model import good


class GoodAttribute:
    def __init__(self):
        self.stock = 0
        self.price = 0


class Inventory:
    def __init__(self):
        self.totalStock = 0
        self.inventory = {}
        for currgood in good.values:
            self.inventory[currgood.name] = GoodAttribute()

    def setStock(self, toChange, stock):
        self.inventory[toChange].stock = stock

    def setPrice(self,toChange, price):
        self.inventory[toChange].price = price

