from config import token, gifs, blacklist, command
from parse import msgParse
import discord
import embeds
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

    # Checks if author is itself in order to prevent a feedback loop. DO NOT REMOVE THIS
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
            await message.channel.send(embed=embeds.tojiOff())
        elif toji.alive == 0:
            toji.alive = 1
            await message.channel.send(embed=embeds.tojiOn())
        else:
            await message.channel.send(embed=embeds.invalidState())
    
    # State checker. Returns an embed dependent on the toji.alive variable

    elif parsedMessage == 's' or parsedMessage == 'status':
        if toji.alive == 0 or toji.alive == 1:    
            await message.channel.send(embed=embeds.tojiState(toji.alive))
        else:
            await message.channel.send(embed=embeds.invalidState())  
    
    # Help command. Returns embed containing a list of commands

    elif parsedMessage == 'h' or parsedMessage == 'help':
        await message.channel.send(embed=embeds.helpCommand())
    
    # Fallback in case of invalid command
    
    else:
        await message.channel.send(embed=embeds.invalidCommand())

client.run(token)
