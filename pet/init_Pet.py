import emoji
import random

#this class is used to init pets from the database
class DBPet:
    def __init__(self, name, species, color, closeness, size, ability_type, rarity, stats):
        self.name = name
        self.species = species
        self.size = size
        self.ability_type = ability_type
        self.color = color
        self.rarity = rarity
        self.closeness = closeness
        #Pet stats used for races and games
        self.swim =          stats[0]
        self.fly =           stats[1]
        self.run =           stats[2]
        self.power =         stats[3]
        self.stamina =       stats[4]
        #Hidden stats
        self.luck =          stats[5]
        self.intelligence =  stats[6]
        
    #print out pet stats
    def printStats(self):
        output = "{} is a {} And looks like {}. They are a {} sized pet. They are the color {} and have a closeeness of {}. Your pet is {}. Swim: {}. fly: {}. Run: {}, Power: {}, Stamina: {}"
        return output.format(self.name, self.species, emoji.emojize(':' + self.species.lower() +':', use_aliases=True), self.size, self.color, self.closeness, self.rarity, self.swim, self.fly, self.run, self.power, self.stamina)
    
    #returns pet stats into a list for easy db entry
    def getStats(self):
        return [self.swim, self.fly, self.run, self.power, self.stamina, self.luck, self.intelligence]
    
    #feed pet class returns amount of power upgraded
    def feed(self, key):
        p = random.randint(2, 9)
        
        if (key == 'Swim'):
            self.swim += p
        elif (key == 'Fly'):
            self.fly += p
        elif (key == 'Run'):
            self.run += p
        elif (key == 'Power'):
            self.power += p
        elif (key == 'Stamina'):
            self.stamina += p
        
        return p