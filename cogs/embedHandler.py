import discord
import pandas as pd
import sys
from cogs.utils.processing import mapnum
def get_roles(rolelist):
    stuff = ""
    for i in rolelist:
        stuff += i.mention
    return stuff


def get_activity(member):
    if member.activity == None:
        return None
    elif member.activity.type != discord.ActivityType.custom:
        text = f"{member.activity.type.name} {member.activity.name}"
        return text

    else:
        return member.activity.name


def get_status(member):
    if member.status == discord.Status.dnd:
        return "DND 🔴"

    elif member.status == discord.Status.online:
        return "ONLINE 🟢 "

    elif member.status == discord.Status.idle:
        return "IDLE 🌙 "

    elif member.status == discord.Status.offline:
        return "OFFLINE 💀 "


def get_data(guildname):
    data = pd.read_csv(f"ServerXpSystem/{guildname}.csv")
    return data
    

def get_member_XP(member):
    try:
      data = get_data(member.guild.name)
      memberRow = data[data.memberID == int(member.id)]
      points = memberRow.XP.values[0]
      return points
    except:
        return 0

def progress(count, total, status=''):
    bar_len = 10
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '░' * (bar_len - filled_len)

    return '%s' % (bar)


def get_level(points):
    a, b = mapnum(points,(points//1000+1) * 1000)

    return f"**Level {points // 1000}** \n  {progress(count=a,total=b)} `({points}/{(points//1000+1) * 1000})`"

def get_rank(member: discord.Member):
    try:
        data = get_data(member.guild)
        data.sort_values(by=['XP'], inplace=True, ascending=False, ignore_index=True)
        data.index += 1
        rank = data[data.memberID == int(member.id)].index.values[0]


        if rank == 1:
            return f"{rank}/{member.guild.member_count} :crown: "
        else:
            return f"{rank}/{member.guild.member_count}"


    except:
        return "not found"






async def StatusEmbed(ctx,member,desc = None):
    if member.is_on_mobile() and member.status != discord.Status.offline:
        embed = discord.Embed(title=member.display_name,
                              description=desc, color=member.top_role.color)
        embed.add_field(name="**Device **", value="Phone: :iphone:  ", inline=False)
        # embed.set_author(member.display_name)
        embed.add_field(name='**Status**', value=get_status(member=member), inline=False)

        embed.add_field(name="**Server Level :small_orange_diamond:**", value=f"{get_level(get_member_XP(member))} ",inline=False)
        embed.add_field(name="**Server Rank**", value=f"**{get_rank(member)} **", inline=False)
        embed.add_field(name="**Joined Server at**", value=f"{str(member.joined_at.date)[:10]}", inline=False)
        embed.add_field(name="**Account Created at*", value=f"{str(member.created_at.date)[:10]}", inline=False)
        embed.add_field(name="**Top role**", value=member.top_role.mention,inline=False)
        embed.add_field(name="**Activity**", value=get_activity(member=member), inline=False)

        embed.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=embed)

    elif member.status != discord.Status.offline:
        embed = discord.Embed(title=member.display_name,
                              description=desc, color=member.top_role.color)
        embed.add_field(name='**Device **', value="PC:  :desktop:  ", inline=False)
        embed.add_field(name='**Status**', value=get_status(member=member), inline=False)
        embed.add_field(name="**Server Level :small_orange_diamond:**", value=f"{get_level(get_member_XP(member))} ",inline=False)
        embed.add_field(name="**Server Rank**", value=f"**{get_rank(member)} **", inline=False)
        embed.add_field(name="**Joined Server at**", value=f"{str(member.joined_at)[:10]}", inline=False)
        embed.add_field(name="**Account Created at**", value=f"{str(member.created_at)[:10]}", inline=False)
        embed.add_field(name="**Top Role**", value=member.top_role.mention, inline=False)
        embed.add_field(name="**Activity**", value=get_activity(member=member))
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    elif member.status == discord.Status.offline:
        embed = discord.Embed(title=member.display_name,
                              description=desc, color=member.top_role.color)
        embed.add_field(name="**Device**", value=":no_entry:  ", inline=False)
        embed.add_field(name='**Status**', value=get_status(member=member), inline=False)
        embed.add_field(name="**Server Level :small_orange_diamond:**", value=f"{get_level(get_member_XP(member))} ",inline=False)
        embed.add_field(name="**Server Rank**", value=f"**{get_rank(member)} **", inline=False)
        embed.add_field(name="**Joined Server At**", value=f"{str(member.joined_at.date)[:10]}", inline=False)
        embed.add_field(name="**Account Created at**", value=f"{str(member.created_at.date)[:10]}", inline=False)
        embed.add_field(name="**Top Role**", value=member.top_role.mention, inline=False)
        embed.add_field(name="**Activity**", value=get_activity(member=member), inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)