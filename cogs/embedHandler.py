import discord
from discord.ext import commands
import pandas as pd
data = pd.read_csv("PointSystem.csv")


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


def get_member_points(member):
    try:
      memberRow = data[data.memberID == int(member.id)]
      points = memberRow.points.values[0]
      return points
    except:
        return 0

def get_level(points):
    if points < 1000 :
        return 1
    if points > 1000 and points < 2000:
        return 2
    if points > 2000 and points < 3000:
        return 3



async def StatusEmbed(ctx,member,desc = None):
    if member.is_on_mobile() and member.status != discord.Status.offline:
        embed = discord.Embed(title=member.display_name,
                              description=desc, color=member.top_role.color)
        embed.add_field(name="**Device **", value="Phone: :iphone:  ", inline=False)
        # embed.set_author(member.display_name)
        embed.add_field(name='**Status**', value=get_status(member=member), inline=False)

        embed.add_field(name="**Level :small_orange_diamond:**", value=f"**{get_level(get_member_points(member))}   **",inline=False)
        embed.add_field(name="**Nezu points**", value=f"**{get_member_points(member)} :small_blue_diamond: **", inline=False)
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
        embed.add_field(name="**Level :small_orange_diamond:**", value=f"**{get_level(get_member_points(member))}   **",inline=False)
        embed.add_field(name="**Nezu points**", value=f"**{get_member_points(member)} :small_blue_diamond: **",
                        inline=False)
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
        embed.add_field(name="**Level :small_orange_diamond:**", value=f"**{get_level(get_member_points(member))}   **",inline=False)
        embed.add_field(name="**Nezu points**", value=f"**{get_member_points(member)} :small_blue_diamond: **",
                        inline=False)
        embed.add_field(name="**Joined Server At**", value=f"{str(member.joined_at.date)[:10]}", inline=False)
        embed.add_field(name="**Account Created at**", value=f"{str(member.created_at.date)[:10]}", inline=False)
        embed.add_field(name="**Top Role**", value=member.top_role.mention, inline=False)
        embed.add_field(name="**Activity**", value=get_activity(member=member), inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)