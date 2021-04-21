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
