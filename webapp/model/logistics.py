import math

MAX_WIDTH = 500
MAX_HEIGHT = 500
MAX_DISTANCE = int(math.sqrt((MAX_WIDTH * MAX_WIDTH) + (MAX_HEIGHT * MAX_HEIGHT)))
MAX_MERCENARIES = 1
MAX_SOLAR_SYSTEMS = 3
SOLAR_SYSTEM_NAMES = ["Sombrero", "Cygnus", "Andromeda"]
MAX_CAPACITIES = {"Gnat" : [1, 1, 15, 80]}
PLANET_NAMES = ["Acamar", "Adahn",
        "Aldea", "Andevian", "Antedi", "Balosnee", "Baratas", "Brax",
        "Bretel",
        "Calondia", "Campor", "Capelle",
        "Carzon", "Castor",
        "Cestus", "Cheron", "Daled", "Damast", "Davlos", "Deneb", "Deneva", "Devidia",
        "Draylon", "Drema", "Endor", "Esmee",

        "Exo", "Ferris",
        "Festen",        # A great Scandinavian movie
        "Fourmi",        # An ant, in French
        "Frolix",        # A solar system in one of Philip K. Dick's novels
        "Gemulon", "Guinifer",        # One way of writing the name of king Arthur's wife
        "Hades",        # The underworld
        "Hamlet",        # From Shakespeare
        "Helena",        # Of Troy
        "Hulst",        # A Dutch plant
        "Iodine",        # An element
        "Iralius", "Janus",        # A seldom encountered Dutch boy's name
        "Japori", "Jarada", "Jason",        # A Greek hero
        "Kaylon", "Khefka", "Kira",            # My dog's name
        "Klaatu",        # From a classic SF movie
        "Klaestron", "Korma",        # An Indian sauce
        "Kravat",        # Interesting spelling of the French word for "tie"
            "Krios", "Laertes",        # A king in a Greek tragedy
        "Largo", "Lave",            # The starting system in Elite
        "Ligon", "Lowry",        # The name of the "hero" in Terry Gilliam's "Brazil"
        "Magrat",        # The second of the witches in Pratchett's Discworld
        "Malcoria", "Melina", "Mentar",        # The Psilon home system in Master of Orion
        "Merik", "Mintaka", "Montor",        # A city in Ultima III and Ultima VII part 2
        "Mordan", "Myrthe",        # The name of my daughter
        "Nelvana", "Nix",
        # An interesting spelling of a word meaning "nothing" in Dutch
        "Nyle",            # An interesting spelling of the great river
        "Odet", "Og",            # The last of the witches in Pratchett's Discworld
        "Omega",        # The end of it all
        "Omphalos",        # Greek for navel
            "Orias", "Othello",        # From Shakespeare
        "Parade",        # This word means the same in Dutch and in English
        "Penthara", "Picard",        # The enigmatic captain from ST:TNG
        "Pollux",        # Brother of Castor
        "Quator", "Rakhar", "Ran",            # A film by Akira Kurosawa
        "Regulas", "Relva", "Rhymus", "Rochani", "Rubicum",
        # The river Ceasar crossed to get into Rome
        "Rutia", "Sarpeidon", "Sefalla", "Seltrice", "Sigma", "Sol",
        # That's our own solar system
        "Somari", "Stakoron", "Styris", "Talani", "Tamus", "Tantalos",
        # A king from a Greek tragedy
        "Tanuga", "Tarchannen", "Terosa", "Thera",
        # A seldom encountered Dutch girl's name
        "Titan",        # The largest moon of Jupiter
        "Torin",        # A hero from Master of Magic
        "Triacus", "Turkana", "Tyrus", "Umberlee",
        # A god from AD&D, which has a prominent role in Baldur's Gate
        "Utopia",        # The ultimate goal
        "Vadera", "Vagra", "Vandor", "Ventax", "Xenon", "Xerxes",        # A Greek hero
        "Yew",            # A city which is in almost all of the Ultima games
        "Yojimbo",        # A film by Akira Kurosawa
        "Zalkon", "Zuul"]


def map_values(original, omin, omax, nmin, nmax):
    return nmin + ((nmax - nmin) * ((original - omin) / (omax - omin)))

