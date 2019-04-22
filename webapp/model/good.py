class Good:
    def __init__(self, name, price, MTLP, IPL, varianceFactor):
        self.name = name
        self.BASE_PRICE = price
        self.MTLP = MTLP
        self.IPL = IPL
        self.varianceFactor = varianceFactor


WATER = Good("WATER", 30, 0, 3, 4)
FUR = Good("FUR", 250, 0, 10, 10)
FOOD = Good("FOOD", 100, 1, 5, 5)
ORE = Good("ORE", 350, 2, 20, 10)
GAMES = Good("GAMES", 250, 3, -10, 5)
FIREARMS = Good("FIREARMS", 1250, 3, -75, 100)
MEDICINE = Good("MEDICINE", 650, 4, -20, 10)
MACHINES = Good("MACHINES", 900, 4, -30, 5)
NARCOTICS = Good("NARCOTICS", 3500, 5, -125, 150)
ROBOTS = Good("NARCOTICS", 5000, 6, -150, 100)

values = [WATER, FUR, FOOD, ORE, GAMES, FIREARMS, MEDICINE, MACHINES, NARCOTICS, ROBOTS]
