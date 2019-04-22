values = []


class TechLevel:
    def __init__(self, name):
        self.name = name
        self.ordinal = len(values)
        print(self.ordinal)
        values.append(self)


PRE_AGRICULTURE = TechLevel("Pre-Agriculture")
CULTURE = TechLevel("Agriculture")
MEDIEVAL = TechLevel("Medieval")
RENAISSANCE = TechLevel("Renaissance")
EARLY_INDUSTRIAL = TechLevel("Early Industrial")
INDUSTRIAL = TechLevel("Industrial")
POST_INDUSTRIAL = TechLevel("Post-Industrial")
HI_TECH = TechLevel("Hi-Tech")
