import discord
from discord.ext import commands
from setup import discord_bot_token
import praw
from setup import reddit_client_id,reddit_client_secret,reddit_username
import pandas as pd
from ServerXpSystem import ServerXPsystem as SXS

pd.options.mode.chained_assignment = None

bot = commands.Bot(command_prefix='n.')
game = discord.Game(name='n.help')

reddit_bot = praw.Reddit(client_id=reddit_client_id,
                      client_secret=reddit_client_secret,
                      user_agent='random',
                      username=reddit_username)





def SetupBot(bot):
    bot.load_extension("cogs.admins")
    bot.load_extension("cogs.fun")
    bot.load_extension("cogs.music")
    bot.load_extension("cogs.reddit")
    bot.load_extension("ServerXpSystem.ServerXPcommands")
    bot.remove_command("help")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.other")
    bot.run(discord_bot_token)

@bot.event
async def on_ready():
    print('ready')
    await bot.change_presence(status=discord.Status.online, activity=game)

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
        SXS.add_data(member=message.author, XP=10)
    else:
        # print(f"{message.author} missing , so adding")
        SXS.add_member(member=message.author)

    await bot.process_commands(message)






@bot.event
async def on_member_join(member: discord.Member):

    if member.guild.id == 577192344529404154:
        pass
    else:
        await member.guild.system_channel.send('Welcome to ' + member.guild.name + ' ! ' + member.mention)
    if member.guild.id == 411564918303752192:
        role = discord.utils.get(member.guild.roles, name="Refugees")
        await member.add_roles(role)

SetupBot(bot)
