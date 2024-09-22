from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, intaraction):
        await intaraction.response.send_message("Иди нахуй, сука!")


def setup(bot):
    bot.add_cog(Ping(bot))
