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
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    msg = message.content.lower()
    word = 'toji'
    gifs = ['test0',
            'test1',
            'test2',
            'test3',
            'test4',
            'test5',]

    if word in msg:
        await message.channel.send(random.choice(gifs))

client.run('INSERT YOUR OWN TOKEN HERE')
