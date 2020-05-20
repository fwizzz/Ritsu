import discord
from discord.ext import commands
from PIL import Image
from PIL import ImageSequence
import os
import requests
from io import StringIO


class fun(commands.Cog):

    """As the name suggests , These commands are totally for fun!"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, *, member: discord.Member):
        """Slaps a member"""

        if member is None:
            await ctx.send('mention who you want to slap you fool' + ctx.message.author.mention)
        else:
            slapperAvatarURL = ctx.author.avatar_url
            slappedAvatarURL = member.avatar_url
            slapperResponse = requests.get(slapperAvatarURL,stream = True).raw
            slappedResponse = requests.get(slappedAvatarURL,stream=True).raw

            slapperAvatar = Image.open(slapperResponse)
            slappedAvatar = Image.open(slappedResponse)

            slapperAvatar = slapperAvatar.resize((60, 60), Image.ANTIALIAS)
            slappedAvatar = slappedAvatar.resize((50, 60), Image.ANTIALIAS)

            bg = Image.open("slappuh.gif")

            frames = []

            for frame in ImageSequence.Iterator(bg):
                frame = frame.convert("RGBA")
                f = frame.copy()
                f.paste(slappedAvatar, (60, 50))
                f.paste(slapperAvatar, (240, 120))
                frames.append(f)

            frames[0].save('output.gif', save_all=True, append_images=frames[1:])
            file = discord.File("output.gif",filename="output.gif")
            embed = discord.Embed(title=f"{ctx.author.display_name} slapped {member.display_name}",
                                  color=discord.Color.dark_red())
            embed.set_image(url="attachment://output.gif")
            await ctx.send(file=file,embed=embed)

    @commands.command()
    async def quote(self,ctx,member: discord.Member,*,msg):
        embed = discord.Embed(description=f" ❝  ***{msg}***  ❞"
                              f"\n    - *{member.display_name}*")
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)





def setup(bot):
   bot.add_cog(fun(bot))


