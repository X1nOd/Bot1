import disnake
from disnake.ext import commands
from Token import Token
import os

Bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1031998091659849779])

@Bot.event
async def on_ready():
    print("Bot is ready!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")

Bot.run(Token)