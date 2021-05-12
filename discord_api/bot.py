import discord
import asyncio
from discord.ext import commands as discord_commands

import textwrap
import random

class Bot:
    def __init__(self, command_prefix: str, token: str):
        # Configure Bot
        self.client = discord_commands.Bot(command_prefix = command_prefix)
        self.token = token
        
        #variable used for shop command
        self.shopItem = None
        self.shopItemPrice = 0
        
        # ready event
        @self.client.event
        async def on_ready():
            print("Ready!")

        # ping with variable arguments
        @self.client.command()
        async def ping(ctx, *args):
            await ctx.send(f'You pinged PetBot! {args}')

        # $userinfo will print some user information
        @self.client.command()
        async def userinfo(ctx):
            output = textwrap.dedent(f"""\
            username: {ctx.author.name}
            display_name: {ctx.author.display_name}
            discriminator: {ctx.author.discriminator}
            user_id: {ctx.author.id}
            """)
            
            await ctx.send(output)

        # $guildinfo will print some guild information
        @self.client.command()
        async def guildinfo(ctx):
            output: str  = textwrap.dedent(f"""\
            name: {ctx.guild.name}
            region: {ctx.guild.region}
            created: {ctx.guild.created_at} UTC
            channels: {ctx.guild.channels}
            verification_level: {ctx.guild.verification_level}
            description: {ctx.guild.description}
            """)
            
            await ctx.send(output)

        # $botinfo will print some bot information
        @self.client.command()
        async def botinfo(ctx):
            output: str = textwrap.dedent(f"""\
            command_prefix: {ctx.bot.command_prefix}
            description: {ctx.bot.description}
            """)
            
            await ctx.send(output)

        # $commands with print the available commands
        @self.client.command()
        async def commands(ctx):
            output: str = "commands: "

            for command in ctx.bot.commands:
                output += command.name + ", "
            output += '\n'
            
            await ctx.send(output)
   
    #testing out timer loops. Updating shop items every minute.
    async def updateShop(self):
        fruit = {"Round Fruit" : 80, "Square Fruit" : 80, "Triangle Fruit" : 80, "Heart Fruit" : 300, "Mushroom" : 300, "Strong Fruit" : 100, "Tasty Fruit" : 100}
        
        await self.client.wait_until_ready();
        print("UPADTING SHOP")
        
        while not self.client.is_closed():
            self.shopItem = random.choice(list(fruit))
            self.shopItemPrice = fruit[self.shopItem]
            print("We are selling item: ", self.shopItem)
            await asyncio.sleep(60 * 3)
        
    # this will start the bot and must be called after commands are constructed
    def start(self):
        #call task to be run in background
        self.client.loop.create_task(self.updateShop())
        
        self.client.run(self.token)
