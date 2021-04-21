"""
This is a temporary file to help explain the program flow.
"""

# import pet factory
from abstract_pet_factory import AbstractPetFactory

# creating a pet factory
pet_factory = AbstractPetFactory()

# creating factory objects
joe = pet_factory.create_pet("Joe Biden")
kanye = pet_factory.create_pet("Kanye")

# printing individual attributes
print(f"{joe.name} has a rarity of {joe.rarity}")
print(f"{kanye.name} has a rarity of {kanye.rarity}")
