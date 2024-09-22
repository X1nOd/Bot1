import random

import disnake
from disnake.ext import commands

class Randomaizer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="random", aliases=["r"])
    async def rand_command(self, ctx, min, max):
        randomaizer = random.randint(int(min), int(max))
        await ctx.send(f"Ваше число {randomaizer}")

def setup(bot):
    bot.add_cog(Randomaizer(bot))