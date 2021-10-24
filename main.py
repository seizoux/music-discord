import discord
from discord import client
import os
from discord.ext import commands

# bot prefix
intents=discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix="PREFIX HERE", intents=intents)

# loading all the cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        client.load_extension(f"cogs.{filename[:-3]}")

token="TOKEN HERE"
client.run(token)
