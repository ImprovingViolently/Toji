from config import token, gifs, blacklist, command
from parse import msgParse, tojiState
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

class toji:
    alive = 1

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    msg = message.content.lower()

    # Checks if author is itself in order to prevent a feedback loop.
    if message.author == client.user:
        return

    if message.content.startswith(command):
        parsedMessage = msgParse(msg)
        await commandSwitch(parsedMessage, message)

    # Checks all messages for 'toji', returns a random gif.
    word = 'toji'
    
    if word in msg:
        if message.content.startswith(blacklist):
            return
        else:
            if toji.alive == 1:
                await message.channel.send(random.choice(gifs))

# Checks if it is a command

async def commandSwitch(parsedMessage, message):
    
    # Toggle command turns on/off bot auto respond.
    
    if parsedMessage == 't' or parsedMessage == 'toggle':
        if toji.alive == 1:
            toji.alive = 0
            embedVar = discord.Embed(title="Toji has been disabled!", description="To turn Toji back on, use " + command + "toggle", color=0x00ff00)
            await message.channel.send(embed=embedVar)
        elif toji.alive == 0:
            toji.alive = 1
            embedVar = discord.Embed(title="Toji has been enabled!", description="To turn Toji back off, use " + command + "toggle", color=0x00ff00)
            await message.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="ERROR", description="CONTACT MSG WITH ERROR code [TOJI_TOGGLE_CRIT_FAIL_ELIF]", color=0x00ff00)
            await message.channel.send(embed=embedVar)
    
    # State checker. Returns an embed dependent on the toji.alive variable

    elif parsedMessage == 's' or parsedMessage == 'status':
        print(toji.alive)
        if toji.alive == 0 or toji.alive == 1:    
            embedVar = discord.Embed(title="TojiToggle", description="Toji is currently " + tojiState(toji.alive), color=0x00ff00)
            embedVar.add_field(name= command + "toggle", value="To toggle Toji's auto respond.", inline=False)
            await message.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="ERROR", description="CONTACT MSG WITH ERROR code [TOJI_TOGGLE_CRIT_FAIL_ELIF]", color=0x00ff00)
            await message.channel.send(embed=embedVar)  
    
    # Help command. Returns embed containing a list of commands

    elif parsedMessage == 'h' or parsedMessage == 'help':
        embedVar = discord.Embed(title="Help", description="Here is a list of commands:", color=0x00ff00)
        embedVar.add_field(name= command + "help", value="Returns a list of commands.", inline=False)
        embedVar.add_field(name= command + "status", value="Shows whether the bot is online.", inline=False)
        await message.channel.send(embed=embedVar)
    
    #elif parsedMessage == 'debugoverridetojistate':
    #    toji.alive = 123
    #    await message.channel.send('MANUAL OVERRIDE ENABLED')
    
    # Fallback in case of invalid command
    
    else:
        embedVar = discord.Embed(title="Invalid Command", description="You have sent an invalid command!", color=0x00ff00)
        embedVar.add_field(name="For a list of commands, try:", value= command + "help", inline=False)
        await message.channel.send(embed=embedVar)

client.run(token)
