import discord
from discord.ext import commands
import pandas as pd
from ServerXpSystem import ServerXPsystem as SXS

class ServerXPcommands(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def ServerStats(self,ctx,rows=5):
        data =pd.read_csv(f"ServerXPSystem/{ctx.guild.name}.csv")
        await ctx.send(f"```{data.head(rows)}```")

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def daily(self,ctx):
        data = pd.read_csv(f"ServerXPSystem/{ctx.guild.name}.csv")

        if int(ctx.author.id) in  data["memberID"].values:
            SXS.add_data(ctx.author,100)
        else:
            SXS.add_member(ctx.author)
            SXS.add_data(ctx.author,100)

        await ctx.send("you earned 100 xp")

    @commands.command(aliases =["leaderboard","ranks","ServerRank"])
    async def serverRanks(self,ctx,rows = 10):
        data = pd.read_csv(f"ServerXPSystem/{ctx.guild.name}.csv")
        data.sort_values(by=['XP'], inplace=True, ascending=False)
        data.drop(['Unnamed: 0', 'memberID'],axis=1,inplace=True)
        embed = discord.Embed(title=f"{ctx.guild.name} Leaderboard", description=f"```{data.head(10)}```", color=discord.Colour.magenta())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)








def setup(bot):
    bot.add_cog(ServerXPcommands(bot))