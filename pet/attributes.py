from enum import Enum, auto

# these are the values that the pet attributes can contain

class Species(Enum):
    DOG = auto()
    CAT = auto()
    MOUSE = auto()
    FOX = auto()
    BEAR = auto()
    PANDA = auto()
    KOALA = auto()
    HAMSTER = auto()
    TIGER = auto()
    LION = auto()
    COW = auto()
    PIG = auto()
    FROG = auto()
    CHICKEN = auto()
    PENGUIN = auto()
    EAGLE = auto()
    OWL = auto()
    BAT = auto()
    WOLF = auto()
    HOG = auto()
    HORSE = auto()
    UNICORN = auto()
    BEE = auto()
    

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
    BROWN = auto()
    BLACK = auto()
    WHITE = auto()
    ORANGE = auto()

class Rarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()
    ULTRA_LEGENDARY = auto()
