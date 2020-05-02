import discord
from discord.ext import commands

class other(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    async def say(self,ctx,*,message):
        await ctx.send(message)

    @commands.command()
    async def about(self, ctx):
        nezukobot = ctx.guild.get_member(577140178791956500)
        owner = ctx.guild.get_member(247292930346319872)
        embed = discord.Embed(description="A simple discord bot", color=nezukobot.top_role.color)
        embed.set_author(name="nezuko", icon_url=nezukobot.avatar_url)
        embed.add_field(name="**Code**", value="[Link](https://github.com/fwizzz/NezukoBot)")
        embed.add_field(name="**Library**", value="discord.py")
        embed.add_field(name="**Servers**", value=len(self.bot.guilds))
        embed.set_footer(text=f"Created by fvviz#6032", icon_url=owner.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def guildinfo(self, ctx):

        def get_tier(guild : discord.Guild):
            if guild.premium_tier == 0:
                return f"🔷 **Level 0** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 1:
                return f"🔷 **Level 1** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 2:
                return f"🔷 **Level 2** ({guild.premium_subscription_count} boosts)"
            if guild.premium_tier == 3:
                return f"🔷 **Level 3** ({guild.premium_subscription_count} boosts)"


        embed = discord.Embed(title=f"{ctx.guild.name} ",description=ctx.guild.description,
                              color=discord.Color.green())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="**Region :round_pushpin: **",value=f"{str(ctx.guild.region)}",inline=False)
        embed.add_field(name="**Owner :crown: **",value=ctx.guild.owner.mention,inline=False)
        embed.add_field(name="**Created at :clock7: ** ",value=f"{str(ctx.guild.created_at)[:10]}",inline=False)
        embed.add_field(name="**Member Count**",value=f"{ctx.guild.member_count}",inline=False)
        embed.add_field(name="**Server Boost level**",value=get_tier(ctx.guild),inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx, arg=None):

        bot = ctx.guild.get_member(577140178791956500)

        if arg == "ban":
            embed = discord.Embed(title="Ban command", description="Bans a member "
                                                                   "\n **note**: you will require permissions to use this command",
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.ban @member**")
            await ctx.send(embed=embed)

        elif arg == "kick":
            embed1 = discord.Embed(title="Kick command", description="Kicks a member "
                                                                     "\n **note**: you will require permissions to use this command",
                                   color=bot.top_role.color)
            embed1.add_field(name="**USAGE**", value="the command is used like this "
                                                     "\n **n.kick @member**")
            await ctx.send(embed=embed1)



        elif arg == "clear":
            embed3 = discord.Embed(title="Clear command", description="clears specified amount of messages "
                                                                      '\n **note**: you will need to specify the number of messages to clear',
                                   color=bot.top_role.color)
            embed3.add_field(name="**USAGE**", value="the command is used like this "
                                                     "\n **n.clear number-of-messages-here**")
            await ctx.send(embed=embed3)




        elif arg == "slap":
            embed = discord.Embed(title="Slap command", description="Slaps a member "
                                                                    '\n **note**: you will need to specify a member to Slap',
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.slap @member**")
            await ctx.send(embed=embed)

        elif arg == "help":
            embed = discord.Embed(title="help command", description="Help command"
                                                                     '\n use **n.help command-name to get help on a specific command',
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.help**"
                                                    "\n **n.help command-name-here**")
            await ctx.send(embed=embed)

        elif arg == "dm":
            embed = discord.Embed(title="DM command", description="DM's a member "
                                                                  '\n **NOTE**: you will need to specify a message and a member to send it to .'
                                                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    '\n **n.dm @member message-here **')
            await ctx.send(embed=embed)

        elif arg == "serverinfo":
            embed = discord.Embed(title="Server info command", description="shows the info about the server"
                                  ,
                                  color=bot.top_role.color)

            embed.add_field(name="**Aliases**",value="`serverinfo`|`serverstats`|`guildinfo`|`guildstats`",inline=False)
            embed.add_field(name="**Usage**", value="the command is used like this "
                                                    "\n **n.serverinfo**"
                            )
            await ctx.send(embed=embed)
        elif arg == "pfp":
            embed = discord.Embed(title="Pfp command", description="sends the pfp of a member"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.pfp @member**"
                            )
            await ctx.send(embed=embed)

        elif arg == "quote":
            embed = discord.Embed(title="Quote command", description="Quotes a message"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.quote @member message-here**"
                            )
            await ctx.send(embed=embed)

        elif arg == "say":
            embed = discord.Embed(title="Say command", description="says something"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    '\n **n.say message-here **'
                            )
            await ctx.send(embed=embed)
        elif arg == "status":
            embed = discord.Embed(title="Status command", description="shows the staus of a  member "
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**Aliases**", value="`stats`|`info`|`userinfo`", inline=False)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.status @member**"
                            )

            await ctx.send(embed=embed)

        elif arg == "copypasta":
            embed = discord.Embed(title="members command", description="sends reddit copypasta messages"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.copypasta**"
                            )
            await ctx.send(embed=embed)

        elif arg == "hotpost":
            embed = discord.Embed(title="Hotpost command", description="sends a hot post from a subreddit"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.hotpost subreddit-name-here**"
                            )
            await ctx.send(embed=embed)

        elif arg == "newpost":
            embed = discord.Embed(title="Newpost command", description="sends a new post from a subreddit"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.newpost subreddit-name-here**"
                            )
            await ctx.send(embed=embed)

        elif arg == "meme":
            embed = discord.Embed(title="Meme command", description="sends a meme from a subreddit"
                                  ,
                                  color=bot.top_role.color)
            embed.add_field(name="**USAGE**", value="the command is used like this "
                                                    "\n **n.meme**"
                            )
            await ctx.send(embed=embed)


        elif arg == None:

            embed = discord.Embed(title="Bot commands", description="use **n.** before a command"

                                                                    "\n for help on a specific command ,**USE**"

                                                                    "\n  `n.help command-name-here`",

                                  color=bot.top_role.color)
            embed.add_field(name="**Admin commands :crown: ** ",value=" `ban` | `kick` | `clear`",inline=False)
            embed.add_field(name="** Fun commands :speech_balloon:**",value= "`slap` | `quote`",inline=False)
            embed.add_field(name="**Other commands  :gear:**",value= "`dm`| `serverinfo` | `pfp`| `status` | `say`",inline=False)
            embed.add_field(name="**Reddit commands :globe_with_meridians:**",value="`copypasta` | `hotpost` | `newpost` | `meme`")

            bot = ctx.guild.get_member(577140178791956500)
            embed.set_author(name="nezuko", icon_url=bot.avatar_url)

            await ctx.send(embed=embed)
        else:
            await ctx.send("command does not exist")


    @commands.command(aliases=["info", "stats", "Status"])
    async def status(self, ctx, *, member: discord.Member):

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

        async def custom_status(desc):
            if member.is_on_mobile() and member.status != discord.Status.offline:
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name="**DEVICE **", value="Phone: :iphone:  ", inline=False)
                # embed.set_author(member.display_name)
                embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
                embed.add_field(name="**JOINED SERVER AT**", value=f"{member.joined_at.date}", inline=False)
                embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{member.created_at.date}", inline=False)
                embed.add_field(name="**TOP ROLE**", value=member.top_role.mention)
                embed.add_field(name="**ACTIVITY**", value=get_activity(member=member), inline=False)

                embed.set_thumbnail(url=member.avatar_url)

                await ctx.send(embed=embed)

            elif member.status != discord.Status.offline:
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name='**DEVICE **', value="PC:  :desktop:  ", inline=False)
                embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
                embed.add_field(name="**JOINED SERVER AT**", value=f"{str(member.joined_at)[:9]}", inline=False)
                embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{str(member.created_at)[:9]}", inline=False)
                embed.add_field(name="**TOP ROLE**", value=member.top_role.mention, inline=False)
                embed.add_field(name="**ACTIVITY**", value=get_activity(member=member))
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.send(embed=embed)

            elif member.status == discord.Status.offline:
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name="**DEVICE**", value=":no_entry:  ", inline=False)
                embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
                embed.add_field(name="**JOINED SERVER AT**", value=f"{member.joined_at.date}", inline=False)
                embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{member.created_at.date}", inline=False)
                embed.add_field(name="**TOP ROLE**", value=member.top_role.mention, inline=False)
                embed.add_field(name="**ACTIVITY**", value=get_activity(member=member), inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                await ctx.send(embed=embed)

        if member.id == 577140178791956500:
            await custom_status(desc="waifu")

        elif member.id == 247292930346319872:
            await custom_status(desc="not telling")

        elif member.is_on_mobile() and member.status != discord.Status.offline:
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name="**DEVICE **", value="Phone: :iphone:  ", inline=False)

            embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
            embed.add_field(name="**JOINED SERVER AT**", value=f"{member.joined_at.date}", inline=False)
            embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{member.created_at.date}", inline=False)
            embed.set_thumbnail(url=member.avatar_url)

            embed.add_field(name="**TOP ROLE**", value=member.top_role.mention, inline=False)
            embed.add_field(name="**ACTIVITY**", value=get_activity(member=member), inline=False)
            await ctx.send(embed=embed)


        elif member.status != discord.Status.offline:
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name="**DEVICE **", value="PC:  :desktop:  ", inline=False)

            embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
            embed.add_field(name="**JOINED SERVER AT**", value=f"{member.joined_at.date}", inline=False)
            embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{member.created_at.date}", inline=False)
            embed.add_field(name="**TOP ROLE**", value=member.top_role.mention, inline=False)
            embed.add_field(name="**ACTIVITY**", value=get_activity(member=member), inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

        elif member.status == discord.Status.offline:
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name="DEVICE", value=":no_entry:  ", inline=False)
            embed.add_field(name='**STATUS**', value=get_status(member=member), inline=False)
            embed.add_field(name="**JOINED SERVER AT**", value=f"{member.joined_at.date}", inline=False)
            embed.add_field(name="**ACCOUNT CREATED AT**", value=f"{member.created_at.date}", inline=False)
            embed.add_field(name="**TOP ROLE**", value=f"{member.top_role.mention}", inline=False)
            embed.add_field(name="**ACTIVITY**", value=get_activity(member=member), inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def pfp(self, ctx, *, member: discord.Member):
        """Displays the profile picture of a member"""

        embed = discord.Embed(title=f"{member.display_name}'s avatar",color = member.top_role.color)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def dm(self, ctx,member: discord.Member,*,msg):

        try:
            await member.send(msg)
            await ctx.channel.purge(limit=2)
        except:
            await ctx.send("something is wrong,i think the member might've blocked his dms")







def setup(bot):
    bot.add_cog(other(bot))