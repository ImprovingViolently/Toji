from config import token, gifs, blacklist, command, status
from discord.ext import commands
import commands as cmd
import discord, embeds, random, sys

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
            return
        else:
            if toji.alive == 1:
                await message.channel.send(random.choice(gifs))

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(embed=embeds.invalidCommand())

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

#client.run(token)
bot.run(token)
