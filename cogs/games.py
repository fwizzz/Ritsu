import discord
from discord.ext import commands
from cogs.XOgame.XOgamediscord import initXOgame , Terminate , StartGame

class Games(commands.Cog):

    def __init__(self,bot):
        self.bot= bot

    @commands.command(aliases = ["ttt","TTT","tictactoe"])
    async def TicTacToe(self,ctx,member:discord.Member):
        await initXOgame(ctx,ctx.author,member)

        if member.id == ctx.author.id:
            await ctx.send("you want to play against yourself? , **you simply can't** <a:think:706046107154907136> \ntry pinging one of your friends (if you have any)")
        else:
            await ctx.send(
                f"{member.mention} , **{ctx.author.display_name}** wants to play Tic Tac Toe with you , Are you ready? `(Y/n)`")

            def check(m):
                return m.content in 'Yn' and m.author == member

            msg = await self.bot.wait_for('message', check=check, timeout=20)

            if msg.content == "Y":
                await StartGame(ctx, bot=self.bot, player1=ctx.author, player2=member)

            else:
                await Terminate(ctx)





def setup(bot):
    bot.add_cog(Games(bot))