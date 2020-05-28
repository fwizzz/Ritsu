import discord
import pandas as pd
import sys
from cogs.utils.processing import mapnum
import datetime
from cogs.utils.flags import UserFlags
import requests





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
        return "<:dnd2:464520569560498197>"

    elif member.status == discord.Status.online:
        return "<:online:313956277808005120>"

    elif member.status == discord.Status.idle:
        return "🌙"

    elif member.status == discord.Status.offline:
        return "<:status_offline:596576752013279242>"


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



def progress(count, total):
    bar_len = 10
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '░' * (bar_len - filled_len)

    return '%s' % (bar)





def get_level(points):
    a, b = points, (points // 1000 + 1) * 1000
    if a > 1000:
        a, b = mapnum(points, (points // 1000 + 1) * 1000)
    return f"**Level {points // 1000}** \n  {progress(count=a, total=b)} `({points}/{(points // 1000 + 1) * 1000})`"


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


def format_date(join_date: datetime.datetime):
    today = datetime.date.today()
    days = join_date.date() - today
    year = int(days.days / 365)
    remaining_days = days.days % 25

    if year == 0:
        return f"{join_date.day} {join_date.strftime('%B')},{join_date.year}"

    return f"{join_date.day} {join_date.strftime('%B')},{join_date.year}"


def get_content_type(url):
    return requests.head(url).headers['Content-Type']

def get_device(member : discord.Member):

    if member.is_on_mobile():
        return ":iphone: Mobile "
    else:
        return ":desktop: Desktop"






def add_bot(member):
    if member.bot:
        return "<:bot:714777219590782996>"
    else:
        return ""

async def get_badges_desc(member: discord.Member, bot):
    val = (await bot.http.get_user(member.id))['public_flags']
    badges = [*UserFlags(val)]
    stuff = ""
    for i in list(badges):
        if str(i) == "hs_balance":
            stuff += "<:hsBalance:710512831463686235> "
        elif str(i) == "hs_brilliance":
            stuff += "<:BrillianceLogo:710518070640378021> "

        elif str(i) == "hs_bravery":
            stuff += "<:bravery:710518487390486549> "

        elif str(i) == "early_supporter":
            stuff += "<:earlysupporter:710859759938568212> "

        elif str(i) == "bug_hunter_lvl1":
            stuff += "<:Bughunter:710861051322957905> "

        elif str(i) == "bug_hunter_lvl2":
            stuff += "<:bug2:710864460612632596> "

        elif str(i) == "verified_dev":
            stuff += "<:dev:710864395588206612> "
        elif str(i) == "hs_events":
            stuff += "<:events:710864377791643690> "

        elif str(i) == "discord_partner":
            stuff += "<:DiscordPartner:710860869252415630> "

        else:
            pass

    if get_content_type(member.avatar_url) == "image/gif":
        stuff += "<:nitro:710866062924709938> "


    if member.premium_since is not None:
        stuff += "<:booster:711878282965942333>"

    return stuff


async def StatusEmbed(ctx, member : discord.Member, bot):
        embed = discord.Embed(title=f"{get_status(member)} {member.display_name}  {add_bot(member)}",
                              description=await get_badges_desc(member,bot), color=0x2f3136)

        embed.add_field(name="General info",
                        value=f"•  **Join date**      : {format_date(member.joined_at)} "
                              f"\n•  **Created date** : {format_date(member.created_at)} "
                              f"\n•  **User Id**      : {member.id}"
                              f"\n•  **Device**      : {get_device(member)}")

        # embed.set_author(member.display_name)
        #embed.add_field(name="Badges", value=await get_badges(member, bot), inline=False)

        embed.add_field(name="Server Level :small_orange_diamond:", value=f"{get_level(get_member_XP(member))} ", inline=False)


        embed.add_field(name="Server Rank", value=f"**{get_rank(member)} **")



        if member.top_role == ctx.guild.default_role:
           pass
        else:
            embed.add_field(name="Top role", value=member.top_role.mention, inline=False)


        embed.add_field(name="Activity", value=get_activity(member=member), inline=False)

        embed.set_thumbnail(url=member.avatar_url)




        await ctx.send(embed=embed)

