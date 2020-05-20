import discord
from discord.ext import commands
import pandas as pd
from cogs.embedHandler import StatusEmbed
class other(commands.Cog):

    """This category involves commands that have no particular category"""

    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def say(self,ctx,*,message):
        await ctx.send(message)

    @commands.command()
    async def about(self, ctx):
        nezukobot = ctx.guild.get_member(577140178791956500)
        owner = ctx.guild.get_member(247292930346319872)
        embed = discord.Embed(description="A simple discord bot", color=nezukobot.top_role.color)
        embed.set_author(name="nezuko", icon_url=nezukobot.avatar_url)
        embed.add_field(name="**Code**", value="[Link](https://github.com/fwizzz/NezukoBot)")
        embed.add_field(name="**Library**", value="discord.py")
        embed.add_field(name="**Servers**", value=len(self.bot.guilds))
        embed.set_footer(text=f"Created by fvviz#6032", icon_url=owner.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def guildinfo(self, ctx):

        def get_tier(guild : discord.Guild):
            if guild.premium_tier == 0:
                return f"🔷 **Level 0** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 1:
                return f"🔷 **Level 1** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 2:
                return f"🔷 **Level 2** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 3:
                return f"🔷 **Level 3** ({guild.premium_subscription_count} boosts)"


        embed = discord.Embed(title=f"{ctx.guild.name} ",description=ctx.guild.description,
                              color=discord.Color.green())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="**Region :round_pushpin: **",value=f"{str(ctx.guild.region)}",inline=False)
        embed.add_field(name="**Owner :crown: **",value=ctx.guild.owner.mention,inline=False)
        embed.add_field(name="**Created at :clock7: ** ",value=f"{str(ctx.guild.created_at)[:10]}",inline=False)
        embed.add_field(name="**Member Count**",value=f"{ctx.guild.member_count}",inline=False)
        embed.add_field(name="**Server Boost level**",value=get_tier(ctx.guild),inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["ui","info", "stats", "Status","showprofile","profile","showinfo"])
    async def userinfo(self, ctx, *, member : discord.Member = None):
        if member is not None:
            await StatusEmbed(ctx,member,bot = self.bot)
        else:
            await StatusEmbed(ctx,ctx.author,bot=self.bot)


    @commands.command()
    async def pfp(self, ctx, *, member: discord.Member):
        """Displays the profile picture of a member"""

        embed = discord.Embed(title=f"{member.display_name}'s avatar",color = member.top_role.color)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(other(bot))
