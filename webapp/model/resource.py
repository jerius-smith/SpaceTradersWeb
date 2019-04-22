class Resource:
    def __init__(self, name):
        self.name = name


NOSPECIALRESOURCES = Resource("No special resources")
MINERAL_RICH = Resource("Mineral rich")
MINERAL_POOR = Resource("Mineral poor")
DESERT = Resource("Desert")
LOTS_OF_WATER = Resource("Lots of water")
RICH_SOIL = Resource("Rich soil")
POOR_SOIL = Resource("Poor soil")
RICH_FAUNA = Resource("Rich fauna")
LIFELESS = Resource("Lifeless")
WEIRD_MUSHROOMS = Resource("Weird mushrooms")
LOTS_OF_HERBS = Resource("Lots of herbs")
ARTISTIC = Resource("Artistic")
WARLIKE = Resource("Warlike")

values = [NOSPECIALRESOURCES,
          MINERAL_RICH,
          MINERAL_POOR,
          DESERT,
          LIFELESS,
          LOTS_OF_HERBS,
          LOTS_OF_WATER,
          POOR_SOIL,
          RICH_SOIL,
          RICH_FAUNA,
          WEIRD_MUSHROOMS,
          ARTISTIC,
          WARLIKE]
