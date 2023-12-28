import discord
# CREDENTIALS

## Discord
discordtoken = 'your-token'

## mySQL

dbUser = 'your-user'
dbPassword= 'your-password'
dbHost = 'your-ip'
dbDatabase = 'your-database'

# BOT CONFIG
## Sets command prefix
command = '^'

## Sets discord bot's status.
status = discord.Game(command+'help')

## Pool of available gifs for the gif randomiser.
gifs = [
    'https://tenor.com/view/toji-toji-jjk-fushiguro-jjk-toji-princess-toji-kawaii-gif-6512503698876272780',
    'https://tenor.com/view/toji-jjk-jujutsu-kaisen-tuesday-toji-picmix-gif-8168723334892853958',
    'https://tenor.com/view/toji-jjk-edit-toji-edit-toji-fushiguro-toji-jjk-gif-2595306297905933760',
    'https://tenor.com/view/toji-toji-fushiguro-cute-wife-toji-wife-gif-13087645902577823041'
]

## Does not respond with Toji gif if message starts with the following. Add any other comand prefixes you might have to this list.
blacklist = (
    '!',
    '$',
    '#',
    '?',
    ':',
    '&',
    '%',
    '^'
)
