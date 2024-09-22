import datetime

import disnake
from disnake.ext import commands

class TimeMeoute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def timeoute(self, interaction, member: disnake.Member, time: str, reason: str):
        if member == interaction.author:
            return await interaction.response.send_message(
                "Вы не можете замутить самого себя",
                ephemeral=True
            )
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        cool_time = disnake.utils.format_dt(time, style ="f")
        embed = disnake.Embed(
            title="Отдохни браток",
            description = f"Пользователь{member.mention} был отправлен в ссылку по причине {reason}."
                          f"Он вернется {cool_time}",
            color=0x9B84EE
        ).set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral = True)

    @commands.slash_command()
    async def untimeoute(self, interaction, member: disnake.Member):
        await member.timeout(reason=None, until=None)
        await interaction.response.send_message(f"Untimed out {member.mention}", ephemeral=True)

def setup(bot):
    bot.add_cog(TimeMeoute(bot))