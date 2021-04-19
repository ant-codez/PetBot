"""
This is a temporary file to help explain the program flow.
"""
from pet_bot import PetBot

import os

prefix = "$"
token = os.getenv("DISCORD_TOKEN")
petbot: PetBot = PetBot(prefix, token)
petbot.start()
