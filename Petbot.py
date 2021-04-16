import discord
import random
import asyncio
import os
from discord.ext import commands
from Player import Pet, Player
from database import Database

client = commands.Bot(command_prefix = '$')

players = {}

@client.event
async def on_ready():
    print('PetBot is ready');

@client.command()
async def test(ctx):
    #players[ctx.author.id] = (Player(ctx.author.name, ctx.author.id))
    print(players[ctx.author.id].name, players[ctx.author.id].id)
    
    await ctx.send("test complete")

@client.command()
async def ping(ctx):
    await ctx.send(f'You pinged PetBot! {round(client.latency * 1000)}ms')

@client.command()
async def getEgg(ctx):
    players[ctx.author.id] = (Player(ctx.author.name, ctx.author.id))
    
    if players[ctx.author.id].giveEgg():
        await ctx.send("Congrats you got an egg!")
    else:
        await ctx.send("You're carrying too many eggs!")

@client.command()
async def hatchEgg(ctx):
    players[ctx.author.id] = (Player(ctx.author.name, ctx.author.id))
    
    await ctx.send("what is your pets name?")
    
    def check(m):
        return m.author.id == ctx.author.id
    
    try:
        name = await client.wait_for('message', check = check, timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("Timeout")
    
    if players[ctx.author.id].hatchEgg(name.content):
        await ctx.send("Congrats you hatched an egg")
    else:
        await ctx.send("You're carrying too many eggs!")

@client.command()
async def petStats(ctx):
    await ctx.send("which pet do you want to check?")
    
    def check(m):
        return m.author.id == ctx.author.id
    
    try:
        name = await client.wait_for('message', check = check, timeout=10.0)
    except asyncio.TimeoutError:
        await ctx.send("Timeout")
    
    try:
        rtnString = players[ctx.author.id].pets[name.content].getStats()
        await ctx.send("Here are your pet stats")
        await ctx.send(rtnString)
    except:
        await ctx.send("Pet name not found!")
#token

token = "ODMyMTUyOTQwNDIwNjYxMjUw.YHfo0Q.EtBH2cSBvEEB5ifaFlhwOCv8VcY"
client.run(token)