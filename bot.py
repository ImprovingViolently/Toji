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
                UIDping = "<@{}>".format(str(message.author.id))
                await message.channel.send(gifPrefix + random.choice(tojiSummon()))
                if countValidate(str(UIDping)) == True:
                    countUpdate(countCheck(UIDping), UIDping)
                    await message.channel.send('TojiCount increased by 1, ' + UIDping + ', your TojiCount is now ' + str(countCheck(UIDping)) + '!')
                else:
                    countNew(UIDping)
                    await message.channel.send(UIDping + " has invoked Toji for the first time!")

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

@bot.command(aliases=cmd.tojiCount)
async def tojicount(ctx, target):
    if countValidate(str(target)) == True:
        await ctx.send(target + "'s TojiCount is: " + str(countCheck(target)))
    else:
        await ctx.send(str(target) + " is yet to invoke Toji.")

@bot.command(aliases=cmd.tojilb)
async def leaderboard(ctx):
    rank = 1
    embedvar = discord.Embed(title="TojiCount Leaderboard", color=0xb300ff)
    for tuples in countList():
        uid = str(tuples[0]).replace('<@', '')
        username = await bot.fetch_user(uid.replace('>', ''))
        embedvar.add_field(name="{} - {}".format(rank, username), value=str(tuples[1]) + " mention(s) of Toji", inline=False)
        rank += 1
    await ctx.send(embed=embedvar)

@bot.command()
async def sqltest(ctx):
    query = 'SELECT * FROM gifs'
    database = sqlQuery(query, False, True)
    for (gif_id, gif_url, user_id) in database:
        await ctx.send("{}, {}, {}".format(gif_id, gif_url, user_id))
        await ctx.send(gifPrefix + gif_url)

bot.run(discordtoken)
