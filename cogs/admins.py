import discord
from discord.ext import commands
import asyncio

class moderation(commands.Cog):
    """This category involves moderator commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        """This command is used to kick a member from a server ,
           The **Kick_members** permission is required to use this command.
           An optional reason can be  specified for the kick """

        if reason is not None:

            embed2 = discord.Embed(title="Infraction information", color=discord.Color.red())
            embed2.add_field(name="Type", value="Kick")
            embed2.add_field(name="Reason", value="Not specified")
            embed2.set_thumbnail(url=member.avatar_url)
            embed2.set_author(name=member.name, url=member.avatar_url)
            embed2.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)
            await member.kick(reason=reason)
            await ctx.send(embed = embed2)
            await member.send(embed = embed2)
        else:

            embed1 = discord.Embed(title="Infraction information", color=discord.Color.red())
            embed1.add_field(name="Type", value="Kick")
            embed1.add_field(name="Reason", value="Not specified")
            embed1.set_thumbnail(url=member.avatar_url)
            embed1.set_author(name=member.name, url=member.avatar_url)
            embed1.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)

            await ctx.send(embed=embed1)
            await member.send(embed=embed1)

            await member.kick(reason=reason)







    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member: discord.Member,*,reason=None):

        if reason is not None:

            embed2 = discord.Embed(title="Infraction information", color=discord.Color.red())
            embed2.add_field(name="Type", value="Ban")
            embed2.add_field(name="Reason", value="Not specified")
            embed2.set_thumbnail(url=member.avatar_url)
            embed2.set_author(name=member.name, url=member.avatar_url)
            embed2.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)
            await member.send(embed=embed2)
            await ctx.send(embed=embed2)
            await member.ban(reason=reason)


        else:

            embed1 = discord.Embed(title="Infraction information", color=discord.Color.red())
            embed1.add_field(name="Type", value="Ban")
            embed1.add_field(name="Reason", value="Not specified")
            embed1.set_thumbnail(url=member.avatar_url)
            embed1.set_author(name=member.name, url=member.avatar_url)
            embed1.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)

            await ctx.send(embed=embed1)
            await member.send(embed=embed1)
            await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int = None):
        """clears messages, you will require the Manage messages permission to use this command"""

        if amount is not None:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send('**Messages cleared** ' + ctx.message.author.mention)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send('please specify the number of messages to clear')

def setup(bot):
    bot.add_cog(moderation(bot))








