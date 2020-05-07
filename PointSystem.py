import pandas as pd
import discord
from discord.ext import commands
pointsdata = pd.DataFrame({})

pointsdf = pd.DataFrame(columns=['member', 'points', 'memberID','level'])


def init_csv():
    pointsdf.to_csv("PointSystem.csv")


def add_member(member : discord.Member):
    try:
        pd.read_csv("PointSystem.csv")
    except FileNotFoundError:

        print("points system not initilized")

    data = pd.read_csv("PointSystem.csv")
    newRow ={'member' : member, 'points': 0, 'memberID':member.id, 'level': 1 }
    newData = data.append(newRow,ignore_index=True)
    newData.to_csv("PointSystem.csv",index=False)

    print(f"{member} added, points : {newData.tail(1).points.values}")

def add_points(row : pd.DataFrame,points):
    row.points = row.points.values[0] + points

def get_level(points):
    if points < 1000 :
        return 1
    if points > 1000 and points < 2000:
        return 2
    if points > 2000 and points < 3000:
        return 3


def add_level(row: pd.DataFrame):
    row.level = get_level(row.points.values[0])




def add_stuff(member : discord.Member,points:int):
    try:
        pd.read_csv("PointSystem.csv")
    except FileNotFoundError:
        print("points system not initilized")

    data = pd.read_csv("PointSystem.csv")
    memberRow = data[data.memberID == int(member.id)]
    add_points(memberRow,points)
    add_level(memberRow)
    #memberRow.points = memberRow.points.values[0] + points
    data[data.memberID == int(member.id)] = memberRow
    data.to_csv("PointSystem.csv",index=False)
    print(memberRow)






class PointSystemCommands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def head(self,ctx):
        data = pd.read_csv("PointSystem.csv")
        await ctx.send(f"```{data.head()}```")

    @commands.command()
    async def score(self, ctx,member : discord.Member):
        data = pd.read_csv("PointSystem.csv")
        try:
            memberRow = data[data.memberID == int(member.id)]
            await ctx.send(memberRow.points.values[0])
        except:
            await ctx.send("0")


    


def setup(bot):
    bot.add_cog(PointSystemCommands(bot))








