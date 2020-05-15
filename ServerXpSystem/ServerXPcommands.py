import discord
from discord.ext import commands
import pandas as pd
from ServerXpSystem import ServerXPsystem as SXS
import numpy as np
from cogs.embedHandler import get_level,get_rank

class ServerXPcommands(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        


    @commands.command(aliases =["leaderboard","ranks","ServerRank"])
    async def serverRanks(self,ctx,rows = 10):
        data = pd.read_csv(f"ServerXPSystem/{ctx.guild.name}.csv")
        data.sort_values(by=['XP'], inplace=True, ascending=False, ignore_index=True)
        data.index += 1
        data.drop(['Unnamed: 0', 'memberID'],axis=1,inplace=True)
        embed = discord.Embed(title=f"{ctx.guild.name} Leaderboard", description=f"```{data.head(10)}```", color=discord.Colour.magenta())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command(aliases= ["showrank","ShowRank","Rankshow","rankshow"])
    async def memberRank(self,ctx,member: discord.Member):
        try:
            data = pd.read_csv(f"ServerXPSystem/{member.guild.name}.csv")
            memberRow = data[data.memberID == int(member.id)]
            level = get_level(memberRow.level.values[0])
            embed = discord.Embed(title=f"{member.display_name} rank",description=level)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Rank",value=f"**{get_rank(member)}**")
            await ctx.send(embed=embed)
        except:
            pass








def setup(bot):
    bot.add_cog(ServerXPcommands(bot))
