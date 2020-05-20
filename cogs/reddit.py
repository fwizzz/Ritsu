import discord
from discord.ext import commands
import praw
import random
from setup import reddit_client_id
from setup import reddit_client_secret
from setup import reddit_username

reddit_bot = praw.Reddit(client_id=reddit_client_id,
                      client_secret=reddit_client_secret,
                      user_agent='random',
                      username=reddit_username)

color = discord.Color.orange()

class reddit(commands.Cog):

    """This category includes Commands relating to reddit posts"""
    @commands.command()
    async def meme(self, ctx):
        subreddit = reddit_bot.subreddit('memes')
        hotposts = subreddit.hot(limit=100)
        postlist = list(hotposts)
        randompost = random.choice(postlist)
        embed = discord.Embed(title=randompost.title,
                              description=f':thumbsup: {randompost.score} \n \n :speech_balloon:{len(randompost.comments)} ',
                              url=randompost.url, colour=0x3498d)
        embed.set_image(url=randompost.url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ["new"])
    async def newpost(self, ctx, subreddit_name):
        """sends you the fresh posts from a subreddit"""
        subreddit = reddit_bot.subreddit(f'{subreddit_name}')
        newposts = subreddit.new(limit=10)
        postlist = list(newposts)
        randompost = random.choice(postlist)

        if randompost.over_18:
            if ctx.channel.is_nsfw():
                if "https://v.redd.it/" in randompost.url:
                    await ctx.send(randompost.title)
                    await ctx.send(randompost.url)
                elif "https://youtube.com/" in randompost.url:
                    await ctx.send(randompost.title)
                    await ctx.send(randompost.url)
                else:
                    embed = discord.Embed(title=randompost.title,
                                          url=randompost.url,
                                          colour=color)
                    embed.set_image(url=randompost.url)
                    embed.set_footer(text="Reddit",icon_url="https://lh3.googleusercontent.com/proxy/WSALMFr5sh0W6ISOCIE05dGkMWFr07YltgfykxUx-6stycRoLB_LRG50DrdTUwPmVOrNLNDEug6gThwbMYMXDRGpiQCBocwxFJ5VonhzaLHJ44qxruE")
                    embed.add_field(name="<:reddit_updoot:684067800066949180> upvotes ", value=randompost.score)
                    embed.add_field(name="💬 comments ", value=len(randompost.comments))

                    await ctx.send(embed=embed)
            else:
                await ctx.send(
                    ":police_officer: **Stop right there** :oncoming_police_car:  , **NSFW** commands can only be used in NSFW channels")
        else:
            if "https://v.redd.it/" in randompost.url:
                await ctx.send(randompost.title)
                await ctx.send(randompost.url)
            elif "https://youtube.com/" in randompost.url:
                await ctx.send(randompost.title)
                await ctx.send(randompost.url)
            else:
                embed = discord.Embed(title=randompost.title,
                                      url=randompost.url,
                                      colour=0x3498db)
                embed.set_image(url=randompost.url)
                embed.add_field(name="<:reddit_updoot:684067800066949180> upvotes ", value=randompost.score)
                embed.set_footer(text="Reddit",
                                 icon_url="https://lh3.googleusercontent.com/proxy/WSALMFr5sh0W6ISOCIE05dGkMWFr07YltgfykxUx-6stycRoLB_LRG50DrdTUwPmVOrNLNDEug6gThwbMYMXDRGpiQCBocwxFJ5VonhzaLHJ44qxruE")
                embed.add_field(name="💬 comments ", value=len(randompost.comments))

                await ctx.send(embed=embed)




    @commands.command(aliases = ["hot"])
    async def hotpost(self,ctx, subreddit_name):
        """sends you the hottest posts from a subreddit"""
        subreddit = reddit_bot.subreddit(f'{subreddit_name}')
        hotposts = subreddit.hot(limit=10)
        postlist = list(hotposts)
        randompost = random.choice(postlist)

        if randompost.over_18:
            if ctx.channel.is_nsfw():
                if "https://v.redd.it/" in randompost.url:
                    await ctx.send(randompost.title)
                    await ctx.send(randompost.url)
                elif "https://youtube.com/" in randompost.url:
                    await ctx.send(randompost.title)
                    await ctx.send(randompost.url)

                else:
                    embed = discord.Embed(title=randompost.title,
                                          url=randompost.url,
                                          colour=color)
                    embed.set_image(url=randompost.url)
                    embed.add_field(name="<:reddit_updoot:684067800066949180> upvotes ", value=randompost.score)
                    embed.set_footer(text="Reddit",
                                     icon_url="https://lh3.googleusercontent.com/proxy/WSALMFr5sh0W6ISOCIE05dGkMWFr07YltgfykxUx-6stycRoLB_LRG50DrdTUwPmVOrNLNDEug6gThwbMYMXDRGpiQCBocwxFJ5VonhzaLHJ44qxruE")
                    embed.add_field(name=" 💬 comments", value=len(randompost.comments))

                    await ctx.send(embed=embed)
            else:
                await ctx.send(":police_officer: **Stop right there** :oncoming_police_car:  , **NSFW** commands can only be used in NSFW channels")
        else:
            if "https://v.redd.it/" in randompost.url:
                await ctx.send(randompost.title)
                await ctx.send(randompost.url)
            elif "https://youtube.com/" in randompost.url:
                await ctx.send(randompost.title)
                await ctx.send(randompost.url)

            else:
                embed = discord.Embed(title=randompost.title,
                                      url=randompost.url,
                                      colour=color)
                embed.set_image(url=randompost.url)
                embed.set_footer(text="Reddit",icon_url="https://lh3.googleusercontent.com/proxy/WSALMFr5sh0W6ISOCIE05dGkMWFr07YltgfykxUx-6stycRoLB_LRG50DrdTUwPmVOrNLNDEug6gThwbMYMXDRGpiQCBocwxFJ5VonhzaLHJ44qxruE")
                embed.add_field(name="<:reddit_updoot:684067800066949180> upvotes ", value=randompost.score)
                embed.add_field(name="💬 comments ", value=len(randompost.comments))

                await ctx.send(embed=embed)






    @commands.command()
    async def copypasta(self,ctx):
       subred1 = reddit_bot.subreddit("copypasta")
       subred2 = reddit_bot.subreddit("emojipasta")
       post = random.choice(list(subred1.hot(limit=20))+list(subred2.hot(limit=20)))

       if post.selftext == "":
          await ctx.send(f"{post.title}")
       else:
          await ctx.send(f"{post.selftext}")




    @commands.command()
    async def detectreddit(self, ctx,url):
            post = praw.models.Submission(reddit_bot,url = url)

            embed = discord.Embed(title=post.title,
                          description=f':thumbsup: {post.score} \n \n :speech_balloon: {len(post.comments)} ',
                          url=post.url, colour=0x3498d)
            embed.set_image(url=post.url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(reddit(bot))
