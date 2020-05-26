import discord
from discord.ext import commands
from setup import discord_bot_token
import praw
from setup import reddit_client_id,reddit_client_secret,reddit_username
import pandas as pd
from ServerXpSystem import ServerXPsystem as SXS

pd.options.mode.chained_assignment = None

bot = commands.Bot(command_prefix='dev ')
game = discord.Game(name='rt help')

reddit_bot = praw.Reddit(client_id=reddit_client_id,
                      client_secret=reddit_client_secret,
                      user_agent='random',
                      username=reddit_username)


def SetupBot(bot):
    bot.load_extension("cogs.admins")
    bot.load_extension("cogs.fun")
    bot.load_extension("cogs.music")
    bot.load_extension("cogs.reddit")
    bot.load_extension("cogs.games")
    bot.load_extension("ServerXpSystem.ServerXPcommands")
    bot.remove_command("help")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.other")

    bot.run(discord_bot_token)

@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=game)

@bot.event
async def on_guild_join(ctx):
        nezukobot = ctx.guild.get_member(577140178791956500)

        embed = discord.Embed(title="Bot commands", description="use **n.** before a command"

                                                                    "\n for help on a specific command ,**USE**"

                                                                    "\n  `n.help command-name-here`",

                                  color=nezukobot.top_role.color)
        embed.add_field(name="**Admin commands :crown: ** ",value=" `ban` | `kick` | `clear`",inline=False)
        embed.add_field(name="** Fun commands :speech_balloon:**",value= "`slap` | `quote`",inline=False)
        embed.add_field(name="**Other commands  :gear:**",value= "`dm`| `serverinfo` | `pfp`| `status` | `say`",inline=False)
        embed.add_field(name="**Reddit commands :globe_with_meridians:**",value="`copypasta` | `hotpost` | `newpost` | `meme`")


        embed.set_author(name="nezuko", icon_url=nezukobot.avatar_url)
        await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    server = bot.get_guild(id=581084433646616576)
    channel = bot.get_channel(id=690919915464425492)

    if message.guild == None:
        msg = discord.Embed(description=message.content, color=0x3498d)
        msg.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        await channel.send(embed=msg)

    if "https://www.reddit.com/" in message.content:

        post = praw.models.Submission(reddit_bot, url=message.content)
        print(message.content)

        if "https://v.redd.it/" in post.url:

            msg = await channel.send(post.url)
        else:
            embed = discord.Embed(title=post.title,
                                  # description=f':thumbsup: {post.score} \n \n :speech_balloon: {len(post.comments)} ',
                                  url=post.url, colour=0x3498d)
            embed.set_image(url=post.url)
            embed.set_footer(text=f'👍 {post.score} | 💬 {len(post.comments)}')
            embed.set_author(name=f"Post sent by {message.author.display_name}", icon_url=message.author.avatar_url)

            channel = message.channel
            msg = await channel.send(embed=embed)

        if message.author.guild.id == 581084433646616576:
            await msg.add_reaction("<:upvote:681135395354050593>")
            await msg.add_reaction("<:downvote:681135516296413238>")
        else:
            pass

    try:
        pd.read_csv(f"ServerXpSystem/{message.guild.name}.csv")
        print(f"{message.guild.name}.csv  found")
    except:
        print(f"{message.guild.name}.csv  not found, adding...")
        SXS.init_csv(message.guild.name)

    Xpdata = pd.read_csv(f"ServerXpSystem/{message.guild.name}.csv")

    if str(message.author) in Xpdata["member"].values:
        # print(f" {message.author} found")

        if not message.author.bot:
            SXS.add_data(member=message.author, XP=10)
        else:
            pass
    else:
        # print(f"{message.author} missing , so adding")
        if not message.author.bot:
            SXS.add_member(member=message.author)
        else:
            pass

    if message.guild.id == "ur bot sux":
        print(message.author,":",message.content)



    await bot.process_commands(message)



@bot.command(hidden = True)
async def show_cogs(ctx):
    text  = ""

    for i in bot.cogs:
        cog = bot.get_cog(i)
        text += f"\n {cog.qualified_name}"
    await ctx.send(text)

@bot.command(hidden = True)
async def show_guilds(ctx):
    text  = ""

    for i in bot.guilds:
        text += f"\n {i.name}"
    await ctx.send(text)


@bot.command(hidden=True)
async def leave_guild(ctx,*,guildname):
    for guild in bot.guilds:
        if guild.name == guildname:
           await ctx.message.add_reaction("<:greenTick:596576670815879169>")
           await guild.leave()




@bot.event
async def on_guild_join(guild : discord.Guild):

    owner = bot.get_user(247292930346319872)
    ritsu = bot.get_user(577140178791956500)
    logchannel = bot.get_channel(712640308319617034)

    embed = discord.Embed(title = "Greetings",description="Thanks for adding Ritsu in this server , **Ritsu** is a multi purpose discord bot that has Moderation commands , Fun commands , Music commands and many more!. The bot is still in dev so you can expect more commands and features.To get a list of commands , please use **rt help** " , color = 0x2f3136)
    embed.add_field(name="General information",value="**► __Bot Id__**: 577140178791956500 \n**► __Developer__** : **fwiz#6999** \n**► __Prefix__** : rt ")
    embed.add_field(name="**Links**",value = f"**► [Support Server](https://discord.gg/EVN6qcG)** \n**► [Github](https://github/fwizzz/nezuko)**\n**► [Invite link](https://discord.com/oauth2/authorize?client_id=577140178791956500&scope=bot&permissions=521661951)** ")
    embed.set_thumbnail(url = ritsu.avatar_url)

    m = 0
    for channel in guild.channels:
        if m ==0:
            try:
                await channel.send(embed=embed)
                m +=1
            except:
                pass

    await logchannel.send(f"The bot has been added to **{guild.name}** , We've reached our **{len(bot.guilds)}th** server! <:PogChamp:528969510519046184> :champagne_glass: ")

    


@bot.event
async def on_command_error(ctx,error):

    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f"❌| **{error}** \n__for more help on that command,use__ **rt help {ctx.command.name}**")

    elif isinstance(error,commands.BotMissingPermissions):
        await ctx.send("❌| **I'm missing permissions to execute that command**")

    elif isinstance(error,commands.CommandNotFound):
        pass

    else:
        await ctx.send(f"❌|**{error}**")


SetupBot(bot)


