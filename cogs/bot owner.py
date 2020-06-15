from discord.ext import commands
import discord
import asyncio
import math
from cogs.utils.constants import bot_avatar


class BotOwner(commands.Cog):
    """Shows help for bot"""

    def __init__(self, bot):
        self.bot = bot

    async def is_owner(ctx):
        return ctx.author.id == 247292930346319872

    @commands.command(hidden=True)
    @commands.check(is_owner)
    async def show_guilds(self,ctx):
        text = ""

        for i in self.bot.guilds:
            text += f"\n {i.name}"
        await ctx.send(text)

    @commands.command(hidden=True)
    @commands.check(is_owner)
    async def leave_guild(self,ctx, *, guildname):
        for guild in self.bot.guilds:
            if guild.name == guildname:
                await ctx.message.add_reaction("<:greenTick:596576670815879169>")
                await guild.leave()

    @commands.command(hidden=True)
    @commands.check(is_owner)
    async def show_cogs(self,ctx):
        text = ""

        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            text += f"\n {cog.qualified_name}"
        await ctx.send(text)

    @commands.command(name="reload-cogs",hidden = True)
    @commands.check(is_owner)
    async def reloadcogs(self,ctx):

        cogs = ["games","admins","fun","music","other"]

        for cog in cogs:
            try:

                await msg.send(content = f"<a:loading:718075868345532466> | reloading `{cog}`")
            except:
                msg = await ctx.send(f"<a:loading:718075868345532466> | reloading `{cog}`")

            self.bot.reload_extension(f"cogs.{cog}")

            await msg.delete()




    @commands.command(name="unload", hidden=True)
    @commands.check(is_owner)
    async def unload(self, ctx, cog):

            msg = await ctx.send(f"<a:loading:718075868345532466> | unloading `{cog}`",delete_after = 10)
            self.bot.unload_extension(cog)
            await msg.delete()
            self.bot.reload_extension(cog)


def setup(bot):
    bot.add_cog(BotOwner(bot))