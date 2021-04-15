import discord
import random
import asyncio
import os
from discord.ext import commands
from equation_generator import EquationGenerator
from database import Database

client = commands.Bot(command_prefix = '$')
e_generator = EquationGenerator()
op_list = ["+", "*", "/", "-"]
db = Database()

@client.event
async def on_ready():
    print('PetBot is ready');

@client.command()
async def ping(ctx):
    await ctx.send(f'You pinged PetBot! {round(client.latency * 1000)}ms')
     
#token
token = ""
client.run(token)