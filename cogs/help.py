from discord.ext import commands
import discord
import asyncio
import math
from cogs.utils.constants import bot_avatar


class Help(commands.Cog, name="Help"):
    """Shows help for bot"""

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['hlp','commands'], hidden=True)
    async def help(self, ctx, cog=None):
        """Shows help message."""

        color = 0xDC322F

        nextbtn = "⏩"
        prevbtn = "⏪"
        valids = [nextbtn, prevbtn]

        if cog is None:
            desc = ""
            cats = []
            cogs = []
            subtext = []
            page = 0

            for cog in self.client.cogs:
                cogs.append(cog)

            pages = math.ceil(len(cogs) / 7)
            while True:
                use = cogs[page * 7:(page * 7) + 6]
                for cog in cogs:
                    cog = self.client.get_cog(cog)
                    commands = cog.get_commands()
                    shown_commands = []
                    for command in commands:
                        if command.hidden:
                            pass
                        else:
                            shown_commands.append(command)

                    if len(shown_commands) > 0:
                        if cog.__doc__ is None:
                            doc = "No description"
                        else:
                            doc = cog.__doc__

                        name = cog.qualified_name
                        commands = cog.get_commands()

                        shown_commands = []

                        for command in commands:
                            if command.hidden:
                                pass
                            else:
                                cmdname_modified = f"`{command.name}`  "
                                shown_commands.append(cmdname_modified)




                        cmds = "".join(shown_commands)
                        subtext.append(cmds)

                        if name == "moderation":
                            cats.append(f"<a:BearCop:711584228659429458> **{name}**")

                        elif name == "fun":
                            cats.append(f"<:haha:613185229653409883> **{name}**")
                        elif name == "music":
                            cats.append(f"<:FeelsBeatsMan:597591202614738947> **{name}** ")

                        elif name == "leveling":
                            cats.append(f"<a:kat:710821703286259782> **{name}**")

                        elif name == "other":
                            cats.append(f"<:rooEZSip:596577108675788800> **{name}**")

                        elif name == "games":
                            cats.append(f":video_game: **{name}**")

                        elif name == "reddit":
                            cats.append(f"<:reddit:711990234736361566> **{name}**")


                        #desc += "**__" + name + "__** \n"

                #desc += '```py\n\n"<> denotes an argument/parameter of a command"\n@ DO NOT ACTUALLY USE TYPE <> WHEN TYPING COMMANDS \n``` \n'
                desc += f'''
```diff

-██████╗ ██╗████████╗███████╗██╗   ██╗
-██╔══██╗██║╚══██╔══╝██╔════╝██║   ██║
-██████╔╝██║   ██║   ███████╗██║   ██║
_██╔══██╗██║   ██║   ╚════██║██║   ██║
_██║  ██║██║   ██║   ███████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝


```
:heavy_check_mark::heavy_check_mark:<a:processing:585955989178810379> **__Links__**
'''
                desc += f"\n[`GitHub`](https://github.com/fwizzz/Ritsu) • [`Support Server`](https://discord.gg/9zSXyE9) • [`Invite`](https://discord.com/oauth2/authorize?client_id=577140178791956500&scope=bot&permissions=52166195) \n"
                desc += f'\n:heavy_check_mark::heavy_check_mark:<a:processing:585955989178810379> **__Categories__** '
                desc += f'\n\n• Use `rt help <command>` for more help ; example : `rt help slap`'
                embed = discord.Embed(

                    description=desc,
                    color = 0xDC322F, #ctx.guild.get_member(577140178791956500).top_role.color,
                    timestamp=ctx.message.created_at
                )
                embed.set_thumbnail(url=bot_avatar)

                for cat in cats:

                  embed.add_field(name=cat,value=subtext[cats.index(cat)])

                embed.add_field(name=":heavy_check_mark: ",value="_ _")
                embed.add_field(name=":heavy_check_mark: ", value="_ _")
                owner = self.client.get_user(247292930346319872)
                embed.set_footer(text = f"Created by {str(owner)}",icon_url=owner.avatar_url)
                try:
                    await msg.edit(embed=embed)
                except:
                    msg = await ctx.send(embed=embed)

                def check(r, u):
                    return (u.id == ctx.author.id) and ((r.message.id == msg.id) and r.emoji in valids)

                try:
                    r, u = await self.client.wait_for("reaction_add", timeout=60, check=check)

                    if r.emoji == nextbtn:
                        page += 1
                        if page > pages - 1:
                            page = pages - 1
                        desc = ""
                        cats  = ""


                    elif r.emoji == prevbtn:

                        page -= 1
                        if page < 0:
                            page = 0
                        desc = ""
                        cats = ""




                    try:
                        await msg.remove_reaction(r.emoji, u)
                    except:
                        pass
                except:
                    try:
                        await msg.clear_reactions()
                        break
                    except:
                        pass
                    break
        else:
            cogg = self.client.get_cog(cog)
            if cogg is not None:
                desc = ''
                if cogg.__doc__ is not None:
                    desc = cogg.__doc__ + "\n\n"

                shown_commands = []

                for command in cogg.get_commands():
                    if command.hidden:
                        pass
                    else:
                        cmdname_modified = f"►**{command.name}**"
                        shown_commands.append(cmdname_modified)

                if len(shown_commands) > 0:
                    cmds = "\n".join(shown_commands)



                    if cogg.qualified_name == "moderation":
                        cogname = f"**{cogg.qualified_name}**    <a:BearCop:711584228659429458>  \n"

                    if cogg.qualified_name == "fun":
                        cogname = f"**{cogg.qualified_name}**    <:haha:613185229653409883> \n"

                    if cogg.qualified_name == "music":
                        cogname = f"**{cogg.qualified_name}**    <:FeelsBeatsMan:597591202614738947>  \n"

                    if cogg.qualified_name == "leveling":
                        cogname = f"**{cogg.qualified_name}**    <a:kat:710821703286259782>  \n"

                    if cogg.qualified_name == "games":
                        cogname = f"**{cogg.qualified_name}**    :video_game: \n"

                    if cogg.qualified_name == "other":
                        cogname = f"**{cogg.qualified_name}**    <:rooEZSip:596577108675788800>  \n"

                    if cogg.qualified_name == "reddit":
                        cogname = f"**{cogg.qualified_name}**    <:reddit:711990234736361566> \n"






                    embed = discord.Embed(
                        title=cogname,
                        description=desc,
                        color=color,
                        timestamp=ctx.message.created_at
                    )
                    embed.set_thumbnail(url=bot_avatar)
                    embed.add_field(name="**Commands**",value=cmds)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send("This command category is not available")
            else:
                cmd = self.client.get_command(cog)
                if cmd is not None:
                    if cmd.hidden is False:
                        desc = ""
                        try:
                            desc += cmd.help + "\n"
                        except:
                            desc += "No description provided.\n"
                        if len(cmd.clean_params) > 0:
                            params = []
                            pr = ""
                            for p in cmd.clean_params:
                                params.append(p)
                            for p in params:
                                pr += " <" + p + ">"
                            desc += "**Syntax** : `" + cmd.name + pr + "`\n"

                        aliases = cmd.aliases

                        if len(aliases) > 0:
                            desc += "**Aliases** : " + ", ".join(aliases) + "\n"

                        sub_cmds = []
                        try:
                            if len(cmd.commands) > 0:
                                for scmd in cmd.commands:
                                    sub_cmds.append(scmd)

                            if len(sub_cmds) > 0:
                                desc += "\n**Subcommands** : \n"
                                for scmd in sub_cmds:
                                    pr = ""
                                    for p in scmd.clean_params:
                                        pr += "<" + p + "> "
                                    desc += "`" + cmd.name + " " + scmd.name + " " + pr + "`\n"


                        except:
                            pass

                        embed = discord.Embed(
                            title=cmd.name,
                            description=desc,
                            color=color,
                            timestamp=ctx.message.created_at
                        )
                        embed.set_thumbnail(url=bot_avatar)

                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("This command id hidden.")
                else:
                    await ctx.send(f"No command found with the name `{cog}`.")


def setup(bot):
    bot.add_cog(Help(bot))
