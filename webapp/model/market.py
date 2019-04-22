from model import inventory, good
import random

class Market:
    def adjustTotalStock(self, stock):
        self.marketInventory.totalStock = stock;

    def validate_good(self, toValidate, planet):
        tl = planet.techLevel
        return toValidate.MTLP <= tl.ordinal

    def compute_vf(self, gd):
        flip = 1 if random.randint(0, 1) else - 1
        return gd.BASE_PRICE * flip * (random.randint(0, gd.varianceFactor) / 100.0)

    def price_model(self, gd, planet):
        if self.validate_good(gd, planet):
            tl = planet.techLevel
            return gd.BASE_PRICE + (abs(gd.IPL * (tl.ordinal - gd.MTLP)) + self.compute_vf(gd))
        return 0

    def random_stock(self, gd, planet, bound):
        if self.validate_good(gd, planet):
            return random.randint(0, bound)
        return 0

    def create_inventory(self, planet):
        inv = inventory.Inventory()
        for currentGood in good.values:
            randStock = self.random_stock(currentGood, planet, 50)
            computedPrice = self.price_model(currentGood, planet)
            if computedPrice < 0:
                computedPrice = self.price_model(currentGood, planet)

            inv.setStock(currentGood.name, randStock)
            inv.setPrice(currentGood.name, computedPrice)
            inv.totalStock += randStock

        return inv

    def __init__(self, planet):
        self.marketInventory = self.create_inventory(planet)
