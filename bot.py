from config import *
from parse import *
from discord.ext import commands
import commands as cmd
import discord, embeds, random, sys
import mysql.connector

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=command, intents=intents, help_command=None)

class toji:
    alive = 1

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    status = discord.Game(command+'help')
    await bot.change_presence(status=discord.Status.online, activity=status)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'toji' in message.content.lower():
        if message.content.startswith(blacklist):
            await bot.process_commands(message)
            return
        else:
            if toji.alive == 1:
                await message.channel.send(gifPrefix + random.choice(tojiSummon()))

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(embed=embeds.invalidCommand())
    await ctx.send(error)

@bot.command(aliases=cmd.help)
async def help(ctx):
    await ctx.send(embed=embeds.helpCommand())

@bot.command(aliases=cmd.status)
async def status(ctx):
    if toji.alive == 0 or toji.alive == 1:    
        await ctx.send(embed=embeds.tojiState(toji.alive))
    else:
        await ctx.send(embed=embeds.invalidState())  

# Toggles the toji auto-respond. Simply checks state, toggles accordingly and calls relevant embed.
@bot.command(aliases=cmd.toggle)
async def toggle(ctx):
    if toji.alive == 1:
        toji.alive = 0
        await ctx.send(embed=embeds.tojiOff())
    elif toji.alive == 0:
        toji.alive = 1
        await ctx.send(embed=embeds.tojiOn())
    else:
        await ctx.send(embed=embeds.invalidState())

@bot.command(aliases=cmd.kill)
async def kill(ctx):
     await ctx.send(embed=embeds.killCommand())
     sys.exit()

@bot.command(aliases=cmd.addGif)
async def addgif(ctx, link):
    await ctx.send(embed=embeds.addgifCommand())
    if gifValidator(link) == True:
        if gifDuplicateDetector(gifCleaner(link)) == False:
            gifLink = gifCleaner(link)
            userID = ctx.message.author.id
            addGifQuery(gifLink, userID)
            await ctx.send(embed=embeds.addgifSuccess(link))
        else:
            await ctx.send(embed=embeds.gifDuplicate())
    else:
        await ctx.send(embed=embeds.addgifInvalid())

@bot.command(aliases=cmd.removeGif)
async def removegif(ctx, link):
    await ctx.send(embed=embeds.removegifCommand())
    if gifDuplicateDetector(gifCleaner(link)) == True:
        removeGifQuery(link)
        await ctx.send(embed=embeds.removegifSuccess())
    else:
        await ctx.send(embed=embeds.gifFake())

@bot.command()
async def sqltest(ctx):
    cnx = databaseConnect()
    cursor = cnx.cursor()
    query = 'SELECT * FROM gifs'
    cursor.execute(query)
    for (gif_id, gif_url, user_id) in cursor:
        print("{}, {}, {}".format(gif_id, gif_url, user_id))
        await ctx.send("{}, {}, {}".format(gif_id, gif_url, user_id))
        await ctx.send(gifPrefix + gif_url)
    cursor.close()
    cnx.close()

bot.run(discordtoken)
