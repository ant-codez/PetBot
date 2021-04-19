import discord
import asyncio
from bot import Bot

class Client:
    def __init__(self, game_title: str):
        discord.Game(game_title)
        self.bot: Bot = Bot("$")


