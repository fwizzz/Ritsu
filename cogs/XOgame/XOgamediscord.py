import discord
from discord.ext import commands
from cogs.XOgame.utils import TicTacToe , deleteGame , toEmoji
import asyncio

async def initXOgame(ctx,player1 : discord.Member,player2 : discord.Member):
    game = TicTacToe(ctx.guild,player1.display_name,player2.display_name)
    game.new_grid()


async def Terminate(ctx,game :  TicTacToe):
    deleteGame(game)
    await ctx.send("Game terminated")

async def StartGame(ctx,bot,player1 : discord.Member,player2 : discord.Member):
    game = TicTacToe(ctx.guild,player1.display_name, player2.display_name,o = "<:circle:711135987606093905>")
    await ctx.send(f"{game.show_grid()}")
    taken_list = []


    while True:
        if not game.is_won():
            if not game.ended():
                await ctx.send(f"{player1.mention} please enter the number of the box you want to fill `(1,2,3...9)`")

                def check(m):
                    return m.content in game.empty_boxes()  and m.author == player1

                msg = await bot.wait_for('message', check=check,timeout=20)
                try:
                    game.fill_x(int(msg.content))
                    taken_list.append(int(msg.content))
                    await ctx.send(f"{game.show_grid()}")
                except Exception:
                    pass

            else:
                await ctx.send("its a draw :crossed_swords: ")
                await Terminate(ctx,game)
                break
        elif game.is_won():
            await ctx.send(f"**{player2.mention}** has won!")
            await Terminate(ctx,game)
            break

        if not game.is_won():
            if not game.ended():

                await ctx.send(f"{player2.mention} please enter the number of the box you want to fill `(1,2,3...9)`")

                def check(m):
                    return m.content in game.empty_boxes() and m.author == player2

                msg = await bot.wait_for('message', check=check,timeout=20)

                try:
                  game.fill_o(int(msg.content))
                  await ctx.send(f"{game.show_grid()}")
                except Exception:
                    pass

            else:
                await ctx.send("its a draw :crossed_swords: ")
                await Terminate(ctx,game)
                break
        elif game.is_won():
            await ctx.send(f"**{player1.mention}** Has won !")
            await Terminate(ctx,game)
            break













