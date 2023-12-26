from config import token, gifs, blacklist, command
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    
    # Checks if author is itself in order to prevent a feedback loop.
    if message.author == client.user:
        return
    
    # Ensures it doesn't respond to a bot command by comparing to a list of blocked commands
    if message.content.startswith(blacklist):
        return
    
    # Test ping - Turn this into a switch statement or something similar for more commands. its easy trust
    if message.content.startswith(command + 's' or 'status'):
        await message.channel.send('I am alive (i didnt kms)')

    # Checks all messages for 'toji', returns a random gif.
    msg = message.content.lower()
    word = 'toji'
    
    if word in msg:
        await message.channel.send(random.choice(gifs))

client.run(token)
