import nextcord
from nextcord.ext import commands
import random

class CoinflipCog(commands.Cog, name="Coinflip"):

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @nextcord.slash_command(name="coinflip", description="Flips the coin")
    @commands.has_permissions(administrator=True)
    async def coinflip(self, interaction):
        FLIP = random.randint(0, 1)
        if FLIP == 0:
            FLIP_RESULT = "HEADS"
        else:
            FLIP_RESULT = "TAILS"

        coin_embed = nextcord.Embed(title="YOU GOT",
                                description=f"{FLIP_RESULT}",
                                color=0x774dea
                                )
        coin_embed.set_author(name="Coinflip")
        if FLIP_RESULT == "HEADS":
            coin_embed.set_image('https://media.discordapp.net/attachments/1078398427773276291/1078400350089920562/large_new_pound.png')
        else:
            coin_embed.set_image('https://media.discordapp.net/attachments/1078398427773276291/1078400388060938410/large_new_pound_rev.png')
        await interaction.response.send_message(embed=coin_embed)

def setup(bot):
    bot.add_cog(CoinflipCog(bot))
