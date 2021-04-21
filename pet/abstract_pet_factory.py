from pet.attributes import Species, Size, AbilityType, Color, Rarity
from pet.abstract_pet import AbstractPet
import random

class AbstractPetFactory:
    def __init__(self):
        self.pet: AbstractPet

    # creates and returns a pet with randomly generated attributes
    def create_pet(self, name):
        self.pet = AbstractPet(name, random.choice(list(Species)), random.choice(list(Size)), random.choice(list(AbilityType)), random.choice(list(AbilityType)), random.choice(list(Color)), random.choice(list(Rarity)))
        print("-Pet Created: ", self.pet.name, self.pet.species, self.pet.size, self.pet.ability_type, self.pet.subtype, self.pet.color, self.pet.rarity)
        return self.pet
