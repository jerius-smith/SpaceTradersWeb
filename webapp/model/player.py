from model import good, logistics, inventory


class Player:
    def __init__(self, name, prefdifficulty, skillpoints, location):
        self.name = name
        self.prefdifficulty = prefdifficulty
        self.skillpoints = skillpoints
        self.credits = 1000
        self.location = location
        self.ship = Ship("Gnat")
        self.credits = 1000
        self.inventory = inventory.Inventory()


class Ship:
    def __init__(self, name):
        self.name = name
        self.cargoCapacity = logistics.MAX_CAPACITIES[name][2]
        self.gadgetCapacity = logistics.MAX_CAPACITIES[name][1]
        self.fuelCapacity = logistics.MAX_CAPACITIES[name][3]
        self.fuelTooLow = False

