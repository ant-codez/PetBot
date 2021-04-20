from discord_api.bot import Bot

from player import Player
from pet.abstract_pet import AbstractPet

#TODO: remove this dependency
import asyncio

#TODO: get a database working
from database import Database
db = Database()


class PetBot(Bot):
    def __init__(self, command_prefix: str, token: str):
        super().__init__(command_prefix, token)

        # Define the specific pet bot commands
        self.players = {}
        # temporary function until every thing is abstracted further
        def get_pet_stats(self, pet: AbstractPet):
            output = f"-Stats: {pet.name}, {pet.species}, {pet.size}, {pet.ability_type}, {pet.subtype}, {pet.color}, {pet.rarity}"
            return output

        # give the player an egg
        @self.client.command()
        async def get(ctx):
            self.players[ctx.author.id] = Player(ctx.author.name, ctx.author.id)
            
            # Deal with full inventory
            self.players[ctx.author.id].giveEgg()
            await ctx.send("Congrats you got an egg!")

        # hatch a players egg
        @self.client.command()
        async def hatch(ctx):
            self.players[ctx.author.id] = Player(ctx.author.name, ctx.author.id)
            
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
            if db.checkForPet(ctx.author.id, name):
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
            
            def check(m):
                return m.author.id == ctx.author.id
            
            pet = self.players[ctx.author.id].pets[name]
            output = f"{pet.name}, {pet.species}, {pet.size}, {pet.ability_type}, {pet.subtype}, {pet.color}, {pet.rarity}"

            await ctx.send(f"{output}")


