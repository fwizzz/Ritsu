import discord
from discord.ext import commands
import pandas as pd
from ServerXpSystem import ServerXPsystem as SXS
import numpy as np
from cogs.embedHandler import get_level,get_rank
import asyncio
import os

class leveling(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases =["ranks","guildranks","lb"])
    async def leaderboard(self,ctx,rows = 10):
        data = pd.read_csv(f"ServerXpSystem/{ctx.guild.name}.csv")
        data.sort_values(by=['XP'], inplace=True, ascending=False, ignore_index=True)
        data.index += 1
        data.drop(['Unnamed: 0', 'memberID'],axis=1,inplace=True)
        embed = discord.Embed(title=f"{ctx.guild.name} Leaderboard", description=f"```{data.head(10)}```", color=discord.Colour.magenta())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command(aliases= ["rank","ShowRank","Rankshow","rankshow"])
    async def showrank(self,ctx,member: discord.Member=None):
        try:
            if member is not None:
                data = pd.read_csv(f"ServerXpSystem/{member.guild.name}.csv")
                memberRow = data[data.memberID == int(member.id)]
                level = get_level(memberRow.level.values[0])
                embed = discord.Embed(title=f"{member.display_name} rank", description=level)
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="Rank", value=f"**{get_rank(member)}**")
                await ctx.send(embed=embed)
            else:
                member = ctx.author

                data = pd.read_csv(f"ServerXpSystem/{member.guild.name}.csv")
                memberRow = data[data.memberID == int(member.id)]
                level = get_level(memberRow.level.values[0])
                embed = discord.Embed(title=f"{member.display_name} rank", description=level)
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="Rank", value=f"**{get_rank(member)}**")
                await ctx.send(embed=embed)

        except:
            await ctx.send("please try again")

    async def is_owner(ctx):
        return ctx.author.id == 247292930346319872

    @commands.command(hidden = True)
    @commands.check(is_owner)
    async def remove_member(self,ctx,member:discord.Member):
            msg = await ctx.send(f"<a:loading:706195460439933000> | Removing **{member.name}**")
            data = pd.read_csv(f"ServerXpSystem/{member.guild.name}.csv")
            data = data[data.memberID != int(member.id)]
            data.to_csv(f"ServerXpSystem/{ctx.guild.name}.csv",index = False)
            await asyncio.sleep(2)
            await msg.edit(content = f"<:verified:610713784268357632> | Removed **{member.name}** from the leaderboard")

    @commands.command(hidden=True)
    @commands.check(is_owner)
    async def fuck_up_levels(self, ctx):
        member = ctx.author
        msg = await ctx.send(f"<a:loading:706195460439933000> | Resetting levels for **{member.guild.name}**")
        os.remove(f"ServerXpSystem/{ctx.guild.name}.csv")
        await asyncio.sleep(2)
        await msg.edit(content=f"<:verified:610713784268357632> | **{member.guild.name}** levels reset")



def setup(bot):
    bot.add_cog(leveling(bot))
