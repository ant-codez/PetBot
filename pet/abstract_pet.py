from pet.attributes import Species, Size, AbilityType, Color, Rarity

# this are the attributes that a pet has
class AbstractPet:
    def __init__(self, name:str, species: Species, size: Size, ability_type: AbilityType, subtype: AbilityType, color: Color, rarity: Rarity):
        self.name: str = name
        self.species: Species = species
        self.size: Size = size
        self.ability_type: AbilityType = ability_type
        self.subtype: AbilityType = subtype
        self.color: Color = color
        self.rarity: Rarity = rarity
        self.closeness= 0
        self.hunger= 100
        #Pet stats used for races and games
        self.swim=          0
        self.fly=          0
        self.run=           0
        self.power=         0
        self.stamina=       0
        #Hidden stats
        self.luck=          0
        self.intelligence=  0