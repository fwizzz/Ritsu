import discord
from discord.ext import commands
import praw
import random
from setup import reddit_client_id
from setup import reddit_client_secret
from setup import reddit_username
from cogs.utils.constants import reddit_icon
from cogs.embedHandler import reddit_embed
import yarl
import re
import io


reddit_bot = praw.Reddit(client_id=reddit_client_id,
                      client_secret=reddit_client_secret,
                      user_agent='random',
                      username=reddit_username)

color = discord.Color.orange()


class reddit(commands.Cog):

    """This category includes Commands relating to reddit posts"""



    @commands.command()
    async def meme(self, ctx):
        sublist = ["memes","dankmemes","meme","dankmeme"]
        subname = random.choice(sublist)
        subreddit = reddit_bot.subreddit(subname)
        hotposts = subreddit.hot(limit=100)
        postlist = list(hotposts)
        randompost = random.choice(postlist)
        embed = await reddit_embed(subreddit,randompost,color)
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
                    embed = await reddit_embed(subreddit,randompost,color)
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
                embed = await reddit_embed(subreddit,randompost,color)
                await ctx.send(embed=embed)

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
                    embed = await reddit_embed(subreddit,randompost,color)

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
                embed = await reddit_embed(subreddit,randompost,color)

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





def setup(bot):
    bot.add_cog(reddit(bot))
