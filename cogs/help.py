rom discord.ext import commands
import discord
import asyncio


class Help(commands.Cog, name="Help"):
    """Shows help for bot"""

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['hlp'], hidden=True)
    async def help(self, ctx, cog=None):
        """Shows help message."""




        color = ctx.guild.get_member(577140178791956500).top_role.color

        nextbtn = "⏩"
        prevbtn = "⏪"
        valids = [nextbtn, prevbtn]

        if cog is None:
            desc = ""
            cats = ""
            cogs = []
            page = 0

            for cog in self.client.cogs:
                cogs.append(cog)

            pages = math.ceil(len(cogs) / 5)
            while True:
                use = cogs[page * 5:(page * 5) + 6]
                for cog in use:
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

                        if name == "admins":
                            name = "admins "
                            cats += f"► **{name}**    <:rooCop:596577110982918146>  \n"
                        elif name == "fun":
                            cats += f"► **{name}** <a:1coolestpp:648915201592262696>  \n"
                        elif name == "Music":
                            cats += f"► **{name}** <a:ColorfulDino:710821295645786170>  \n"
                        elif name == "ServerXPcommands":
                            cats += f"► **{name}** <a:kat:710821703286259782>   \n"


                        #desc += "**__" + name + "__** \n"
                desc = f"Type `help <category>` to get help on a category. \n "
                desc +=  "```diff\n+ <> denotes an argument that has to be passed in \n- DO NOT ACTUALLY USE <> WHEN USING COMMANDS ```"
                embed = discord.Embed(
                    description=desc,
                    color = color,
                    title="Nezuko help",
                    timestamp=ctx.message.created_at
                )
                embed.set_thumbnail(url=self.client.user.avatar_url)
                embed.add_field(name="**Categories**",value=cats)

                links = "[►GitHub](https://github.com/fwizzz/Nezuko)\n [►Support Server](https://discord.gg/55ywZKj)"
                owner = self.client.get_user(247292930346319872)
                embed.add_field(name= "**Links**",value = links)
                embed.set_footer(text = f"Created by {str(owner)}",icon_url=owner.avatar_url)
                try:
                    await msg.edit(embed=embed)
                except:
                    msg = await ctx.send(embed=embed)

                await msg.add_reaction(prevbtn)
                await asyncio.sleep(0.1)
                await msg.add_reaction(nextbtn)

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

                    if cogg.qualified_name == "admins":
                        cogname = f"**{cogg.qualified_name}**    <:rooCop:596577110982918146>  \n"

                    if cogg.qualified_name == "fun":
                        cogname = f"**{cogg.qualified_name}**    <a:1coolestpp:648915201592262696>  \n"

                    if cogg.qualified_name == "Music":
                        cogname = f"**{cogg.qualified_name}**    <a:ColorfulDino:710821295645786170>  \n"

                    if cogg.qualified_name == "ServerXPcommands":
                        cogname = f"**{cogg.qualified_name}**    <a:kat:710821703286259782>  \n"





                    embed = discord.Embed(
                        title=cogname,
                        description=desc,
                        color=color,
                        timestamp=ctx.message.created_at
                    )
                    embed.set_thumbnail(url=self.client.user.avatar_url)
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
                        embed.set_thumbnail(url=self.client.user.avatar_url)

                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("This command id hidden.")
                else:
                    await ctx.send(f"No command found with the name `{cog}`.")


def setup(bot):
    bot.add_cog(Help(bot))