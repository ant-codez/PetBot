import discord
from discord.ext import commands

class Bot:
    def __init__(self, command_prefix: str,):
        # Configure Bot
        commands.Bot(command_prefix = command_prefix)

        # ready event
        @client.event
        async def on_ready(self):
            print("Ready!")

        # load commands
        @client.command
        async def ping(self, arg1):
            print(f"You pinged me with {arg1}")