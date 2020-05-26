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
        ritsu = ctx.guild.get_member(577140178791956500)
        owner = ctx.guild.get_member(247292930346319872)
        embed = discord.Embed(title="About Ritsu",
                              description="**Ritsu** is a multi purpose discord bot that has Moderation commands , Fun commands , Music commands and many more!. The bot is still in dev so you can expect more commands and features.To get a list of commands , please use **rt help** ",
                              color=0x2f3136)
        embed.add_field(name="General information",
                        value="**► __Bot Id__**: 577140178791956500 \n"
                              "**► __Developer__** : **fwiz#6999** \n"
                              "**► __Prefix__** : rt  \n"
                              f"**► __Servers__** : {len(self.bot.guilds)}  \n")
        embed.add_field(name="**Links**",
                        value=f"**► [Support Server](https://discord.gg/EVN6qcG)** \n"
                              f"**► [Github](https://github/fwizzz/nezuko)**\n"
                              f"**► [Invite link](https://discord.com/oauth2/authorize?client_id=577140178791956500&scope=bot&permissions=521661951) \n** ")
        embed.set_thumbnail(url=ritsu.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def guildinfo(self, ctx,*, guildname  = None ):

        def get_tier(guild : discord.Guild):
            if guild.premium_tier == 0:
                return f"🔷 **Level 0** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 1:
                return f"🔷 **Level 1** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 2:
                return f"🔷 **Level 2** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 3:
                return f"🔷 **Level 3** ({guild.premium_subscription_count} boosts)"

        if guildname is not None:

            for guild in self.bot.guilds:
                if guildname == guild.name:
                    await ctx.message.add_reaction("<:greenTick:596576670815879169>")
                    embed = discord.Embed(title=f"{guild.name} ", description=ctx.guild.description,
                                          color=discord.Color.green())
                    embed.set_thumbnail(url=guild.icon_url)
                    embed.add_field(name="**Region :round_pushpin: **", value=f"{str(guild.region)}", inline=False)
                    embed.add_field(name="**Owner :crown: **", value=guild.owner.mention, inline=False)
                    embed.add_field(name="**Created at :clock7: ** ", value=f"{str(guild.created_at)[:10]}",
                                    inline=False)
                    embed.add_field(name="**Member Count**", value=f"{guild.member_count}", inline=False)
                    embed.add_field(name="**Server Boost level**", value=get_tier(guild), inline=False)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"**{guildname}** not found ")

        else:

            embed = discord.Embed(title=f"{ctx.guild.name} ", description=ctx.guild.description,
                                  color=discord.Color.green())
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="**Region :round_pushpin: **", value=f"{str(ctx.guild.region)}", inline=False)
            embed.add_field(name="**Owner :crown: **", value=ctx.guild.owner.mention, inline=False)
            embed.add_field(name="**Created at :clock7: ** ", value=f"{str(ctx.guild.created_at)[:10]}",
                            inline=False)
            embed.add_field(name="**Member Count**", value=f"{ctx.guild.member_count}", inline=False)
            embed.add_field(name="**Server Boost level**", value=get_tier(ctx.guild), inline=False)
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

    @commands.command(hidden = True)
    async def jishaku(self,ctx):
        await ctx.send("who tf is jishaku and why does everybody keep calling him")




def setup(bot):
    bot.add_cog(other(bot))
