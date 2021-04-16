import discord
import random
import asyncio
import os
from discord.ext import commands

speciesList = ['Dog', 'Cat', 'Turtle']
colorList = ['Red', 'Brown', 'Black', 'Yellow', 'Gold']

class Player:
    
    def __init__(self, username, id):
        self.name = username
        self.id = id
        self.eggs = 1
        self.pets = {}
    
    def giveEgg(self):
        self.eggs += 1
        return True
    
    def hatchEgg(self, petName):
        if self.eggs > 0:
            self.pets[petName] = Pet(random.choice(speciesList), random.choice(colorList), petName)
            print(self.pets[petName].getStats(), petName)
            return True
        else:
            return False
        
        


class Pet:
    
    def __init__(self, species, color, name):
        self.species = species
        self.color = color
        self.name = name
        self.closeNess = 0
    
    def pet(self):
        closeNess += random.randint(0,7)
    
    def getStats(self):
        return f"{self.name} is a {self.species}. It is {self.color} and has a closness of {self.closeNess} to you."