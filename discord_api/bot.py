import discord
from discord.ext import commands as discord_commands

import textwrap

class Bot:
    def __init__(self, command_prefix: str, token: str):
        # Configure Bot
        self.client = discord_commands.Bot(command_prefix = command_prefix)
        self.token = token

        # ready event
        @self.client.event
        async def on_ready():
            print("Ready!")

        @self.client.command()
        async def ping(ctx, *args):
            await ctx.send(f'You pinged PetBot! {args}')

        """
        Figure out how to do this add_command function.

        Basically I want to be able to pass in a function in a way that
        makes it easier for the user of this class to create commands

        Here is the general idea of what I want to do:

        def add_command(command: str, function):
            @self.client.command()
            function

        """

        @self.client.command()
        async def userinfo(ctx):
            output = textwrap.dedent(f"""\
            username: {ctx.author.name}
            display_name: {ctx.author.display_name}
            discriminator: {ctx.author.discriminator}
            user_id: {ctx.author.id}
            """)
            
            await ctx.send(output)

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

        @self.client.command()
        async def botinfo(ctx):
            output: str = textwrap.dedent(f"""\
            command_prefix: {ctx.bot.command_prefix}
            description: {ctx.bot.description}
            """)
            
            await ctx.send(output)

        @self.client.command()
        async def commands(ctx):
            output: str = "commands: "

            for command in ctx.bot.commands:
                output += command.name + ", "
            output += '\n'
            
            await ctx.send(output)

        self.client.run(self.token)
