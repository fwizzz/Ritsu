import discord
from discord.ext import commands
from cogs.XOgame.XOgamediscord import initXOgame , Terminate , StartGame
from discord.ext.commands.cooldowns import BucketType
from cogs.XOgame.utils import TicTacToe , toEmoji
class games(commands.Cog):

    """Here are some games that you can try playing with your friends :video_game: """

    def __init__(self,bot):
        self.bot= bot

    @commands.command(aliases = ["ttt","TTT","tictactoe","TicTacToe"])
    @commands.cooldown(1, 180,BucketType.default)
    async def Tictactoe(self,ctx,member:discord.Member):

        """**Tic-tac-toe** (American English), **noughts and crosses** (British English), or Xs and Os is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. \n \n"""
        await initXOgame(ctx,ctx.author,member)

        if ctx.author.id != 247292930346319872:
            if member.id == ctx.author.id:
                await ctx.send(
                    "you want to play against yourself? , **you simply can't** <a:think:706046107154907136> \ntry pinging one of your friends (if you have any)")
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
    bot.add_cog(games(bot))