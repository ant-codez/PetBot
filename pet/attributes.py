from enum import Enum, auto

class Species(Enum):
    TINDERING = auto()
    FLEETING = auto()
    LIQUIDY = auto()

class AbilityType(Enum):
    GRASS = auto()
    ELECTRIC = auto()
    WATER = auto()
    FIRE = auto()
    FLYING = auto()
    DARK = auto()
    PSYCHIC = auto()
    ROCK = auto()

class Size(Enum):
    TINY = auto()
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    HUGE = auto()

class Color(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    INDIGO = auto()

class Rarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()
    ULTRA_LEGENDARY = auto()
