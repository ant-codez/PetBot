"""
This is a temporary file to help explain the program flow.
"""

from bot import Bot

import os

prefix = "$"
token = os.getenv("DISCORD_TOKEN")
bot: bot = Bot(prefix, token)