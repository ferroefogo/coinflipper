import nextcord
from utils.utils import wait
from nextcord.ext import commands
from .converter import converter
import random

class OddsCog(commands.Cog, name="Odds"):

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @nextcord.slash_command(name="odds", description="Gives a random Odd between 0 and custom number!")
    @commands.has_permissions(administrator=True)
    async def odds(self, interaction, maximum: int):

    
        ODDS = random.randint(0, maximum)
        
        converter(ODDS)
        file = nextcord.File("./number.png")


        odd_embed = nextcord.Embed(title="YOUR ODD IS",
                                color=0x774dea
                                )
        odd_embed.set_author(name='Coinflipper')
        odd_embed.set_image(url="attachment://number.png")
        await interaction.response.send_message(file = file, embed=odd_embed)
        

def setup(bot):
    bot.add_cog(OddsCog(bot))
