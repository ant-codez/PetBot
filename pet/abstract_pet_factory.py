from attributes import Species, Size, AbilityType, Color, Rarity
from abstract_pet import AbstractPet
import random

class AbstractPetFactory:
    def __init__(self):
        self.pet: AbstractPet

    def create_pet(self, name):
        self.pet = AbstractPet(name, random.choice(list(Species)), random.choice(list(Size)), random.choice(list(AbilityType)), random.choice(list(AbilityType)), random.choice(list(Color)), random.choice(list(Rarity)))
        print("-Pet Created: ", self.pet.name, random.choice(list(Species)), random.choice(list(Size)), random.choice(list(AbilityType)), random.choice(list(AbilityType)), random.choice(list(Color)), random.choice(list(Rarity)))
        return self.pet


