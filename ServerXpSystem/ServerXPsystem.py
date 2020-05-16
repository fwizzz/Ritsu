import discord
import pandas as pd

pd.options.mode.chained_assignment = None

serverXPdf = pd.DataFrame(columns=['member', 'XP', 'memberID', 'level'])

def init_csv(guildname : str):
    serverXPdf.to_csv(f"ServerXPSystem/{guildname}.csv")


def add_member(member: discord.Member):
    try:
        pd.read_csv(f"ServerXPSystem/{member.guild.name}.csv")
    except FileNotFoundError:

        print("XP data not initilized")

    data = pd.read_csv(f"ServerXPSystem/{member.guild.name}.csv")
    newRow = {'member': member, 'XP': 0, 'memberID': member.id , 'level' : 1}
    newData = data.append(newRow, ignore_index=True)
    newData.to_csv(f"ServerXPSystem/{member.guild.name}.csv",index=False)



def add_XP(row : pd.DataFrame,XP):
    row.XP = row.XP.values[0] + XP

def get_level(points):
    if points < 1000 :
        return 0
    else:
        return points // 1000
def add_level(row: pd.DataFrame):
    row.level = get_level(row.XP.values[0])

def add_data(member: discord.Member,XP: int):
    try:
        pd.read_csv(f"ServerXPSystem/{member.guild.name}.csv")
    except FileNotFoundError:
        print("points system not initilized")

    data = pd.read_csv(f"ServerXPSystem/{member.guild.name}.csv")
    memberRow = data[data.memberID == int(member.id)]
    add_XP(memberRow, XP)
    add_level(memberRow)
    data[data.memberID == int(member.id)] = memberRow
    data.to_csv(f"ServerXPSystem/{member.guild.name}.csv", index=False)



