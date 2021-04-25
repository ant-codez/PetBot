from pet.abstract_pet_factory import AbstractPetFactory
from pet.abstract_pet import AbstractPet

# temporary because it doesn't make sense for the player to have a factory
factory = AbstractPetFactory()

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.eggs = 1
        self.cash = 100
        self.pets = {}
    
    def giveEgg(self):
        self.eggs += 1
        return True
    
    def hatchEgg(self, name: str):
        if self.eggs > 0:
            self.pets[name] = factory.create_pet(name)
            return self.pets[name]
        else:
            return None
        