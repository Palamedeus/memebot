import discord
import praw
from discord.ext import commands
import random

prefix = "/" #Change the inside of the quotes to whatever prefix you want, like "!" or "?".
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():  #Prints in cmd/terminal when bot is ready
    print("The bot is ready! ", bot.user)

reddit = praw.Reddit(client_id='client_id_goes_here',                       #The Client id of your reddit app. Should be right below "personal use script"
                     client_secret='client_secret_goes_here',   #The secret of your reddit app
                     user_agent='name_goes_here')                #The name of your reddit app


@bot.command()       #Ping command
async def ping(ctx):
    await ctx.send(f'Pong! Your latency is {round(bot.latency * 1000)} miliseconds')
    
@bot.command()                   #Finally, our meme command.
async def meme(ctx):
    memesubs = ["memes", "dankmemes", "okbuddyretard", "wholesomememes", "historymemes", "196", "comedyheaven", "politicalcompassmemes", "deepfriendmemes"]   #Replace these with the subreddits YOU want
    memes_submissions = reddit.subreddit(random.choice(memesubs)).hot()  #Picks a random subreddit an pulls the hot post
    post_to_pick = random.randint(1, 50)                                  
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)    #Gets a random post from hot of that subreddit.

    fullpost = ("https://www.reddit.com", submission.permalink)             
    post = "".join(fullpost)                                                  #Creates a link to the post

    embed=embed=discord.Embed(title=f"{submission.title}", url=f"{post}", description=f"Posted on r/{submission.subreddit} by u/{submission.author}", color=random.randint(0, 0xFFFFFF))
    #^^^ Creates an embed with the title, link user, and subreddit of the post.
    
    embed.set_image(url=submission.url)        #Adds the actual image of the meme          
    await ctx.send(embed=embed)                #sends the embed
    
    
 
bot.run('token')        #IMPORTANT. THE BOT WONT WORK UNLESS YOU PUT YOUR BOT TOKEN THERE.
