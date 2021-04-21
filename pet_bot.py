from discord_api.bot import Bot

from player import Player
from pet.abstract_pet import AbstractPet

#TODO: remove this dependency
import asyncio
import emoji
#TODO: get a database working
from database import Database
db = Database()


class PetBot(Bot):
    def __init__(self, command_prefix: str, token: str):
        super().__init__(command_prefix, token)

        # Define the specific pet bot commands
        self.players = {}

        # give the player an egg
        @self.client.command()
        async def get(ctx):
            self.players[ctx.author.id] = Player(ctx.author.name, ctx.author.id)
            
            # Deal with full inventory
            self.players[ctx.author.id].giveEgg()
            await ctx.send("Congrats you got an egg!")

        #use to test new features
        @self.client.command()
        async def test(ctx):
            db.checkTotalEggs(ctx.author.id)
            await ctx.send("Test complete...")
        # hatch a players egg
        @self.client.command()
        async def hatch(ctx):
            self.players[ctx.author.id] = Player(ctx.author.name, ctx.author.id)
            
            #check if user exists in the DB
            if db.record_from_user_id(ctx.author.id):
                print("User found in db")  
            else:
                print("ID does not exist in database: ", ctx.author.id)
                #add new user to database
                db.create_user(ctx.author.id, ctx.author.name)
            
            
            
            await ctx.send("what is your pets name?")
            
            def check(m):
                return m.author.id == ctx.author.id
            
                name: str = ""
            try:
                message = await self.client.wait_for('message', check = check, timeout=10.0)
                name = message.content
            except asyncio.TimeoutError:
                await ctx.send("Timeout")
            
            #Check to see if pet name is taken, if not create pet        
            if db.checkForPet(ctx.author.id, name) == False:
                pet = self.players[ctx.author.id].hatchEgg(name)
                await ctx.send("Congrats you hatched an egg")
                output = f"{pet.name}, {pet.species.name}, {pet.size.name}, {pet.ability_type.name}, {pet.subtype.name}, {pet.color.name}, {pet.rarity.name}"
                db.savePetToDB(ctx.author.id, ctx.author.name, pet)
                await ctx.send(output)
            else:
                await ctx.send("You already have a pet with this name!")

        # get a particular pet's stats
        @self.client.command()
        async def stats(ctx, name):
            
            #check if pet is in the db
            pet = db.checkForPet(ctx.author.id, name)
            if pet:
                output = "{} is a {} And looks like {}. They are a {} sized pet. They are the color {} and have a closeeness of {}. Your pet is {}." 
                await ctx.send(output.format(pet[0], pet[1], emoji.emojize(':' + pet[1].lower() +':', use_aliases=True), pet[5], pet[3], pet[4], pet[7]))   
            else:
                await ctx.send("No pet with that name!")
            #pet = self.players[ctx.author.id].pets[name]
            

