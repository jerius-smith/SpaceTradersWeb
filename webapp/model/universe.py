from model import logistics, techlevel, resource, market
import random

usedPlanets = set()

class Universe:
    def __init__(self):
        self.solarSystems = []
        for i in range(0, 3):
            self.solarSystems.append(SolarSystem(logistics.SOLAR_SYSTEM_NAMES[i]))



class SolarSystem:
    NUM_PLANETS = int(random.uniform(0.0, 1.0) * 7) + 10

    def __init__(self, name):
        self.name = name
        self.planets = []
        for i in range(0, SolarSystem.NUM_PLANETS):
            rand_int = random.randint(0, len(logistics.PLANET_NAMES) - 1)

            while rand_int in usedPlanets:
                rand_int = random.randint(0, len(logistics.PLANET_NAMES) - 1)

            planet = Planet(logistics.PLANET_NAMES[rand_int])
            planet.setSolarSystemCurrentlyIn(name)
            self.planets.append(planet)

        self.xLoc = random.randint(0, logistics.MAX_WIDTH)
        self.yLoc = random.randint(0, logistics.MAX_HEIGHT)


class Planet:
    def __init__(self, name):
        self.name = name
        self.xLoc = random.randint(0, logistics.MAX_WIDTH)
        self.yLoc = random.randint(0, logistics.MAX_HEIGHT)
        self.techLevel = techlevel.values[random.randint(0, len(techlevel.values) - 1)]
        self.resource = resource.values[random.randint(0, len(resource.values) - 1)]
        self.market = market.Market(self)

    def setSolarSystemCurrentlyIn(self, solar_name):
        self.solarSystemCurrentlyIn = solar_name


def getPlanetMarket(planetName, uni):
    for i in range(0, 3):
        for planet in uni.solarSystems[i].planets:
            if planet.name == planetName:
                return planet.market


def getRandLocation(uni):
    for i in range(0, 3):
        if random.randint(0, 4) == 0:
            for planet in uni.solarSystems[i].planets:
                if random.randint(0, 4) == 0:
                    return planet

    return uni.solarSystems[random.randint(0, 3)].planets[random.randint(0, 3)]
