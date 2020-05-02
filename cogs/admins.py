import discord
from discord.ext import commands
import asyncio

class admins(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        await member.kick(reason=reason)
        if reason is not None:
            if str(reason).startswith("for"):
                await ctx.send(f'{member.mention} kicked  {reason}')
            else:
                await ctx.send(f"{member.mention} kicked for {reason}")
        else:
            await ctx.send(f'{member.mention} kicked')



    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member: discord.Member,*,reason=None):

        await member.ban(reason=reason)
        if reason is not None:
            if str(reason).startswith("for"):
                await ctx.send(f'{member.mention} banned  {reason}')
            else:
                await ctx.send(f"{member.mention} banned for {reason}")
        else:
            await ctx.send(f"{member.mention} banned")




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int = None):
        """clears messages, you will require the Manage messages permission to use this command"""

        if amount is not None:
            await ctx.channel.purge(limit=amount)
            await ctx.send('**MESSAGES CLEARED** ' + ctx.message.author.mention)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send('please specify the number of messages to clear')

def setup(bot):
    bot.add_cog(admins(bot))








