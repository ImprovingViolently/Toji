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

## SQL injection blacklist
sqlBlacklist = [
    "'",
    '"',
    '%',
    '$',
    ' union '
]
