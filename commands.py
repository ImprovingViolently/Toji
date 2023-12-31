toggle = [
    'tog',
    't'
]

status = [
    'state',
    's'
]

help = [
    'hlp',
    'h'
]

kill = [
    'DEBUG.KILL'
]

addGif = [
    'add',
    'ag'
]

removeGif = [
    'remove',
    'rm'
]

tojiCount = [
    'count',
    'tc'
]

tojilb = [
    'board',
    'lb'
]

helpcommands = {
    'help': ('Displays a list of commands. When run with another command, provides information on that command.', help, command + '{help} {command}', 'help'),
    'status': ('Shows whether the bot is online.', status, command + '{status}', 'status'),
    'toggle': ("Toggle's bot auto respond.", toggle, command + '{toggle}', 'toggle'),
    'addgif': ('Adds a GIF to the database.', addGif, command + '{addgif} {link} where {link} is a ' + gifPrefix + ' link.', 'addgif'),
    'removegif': ('Removes a GIF from the database.', removeGif, command + '{removegif} {link} where {link} is a ' + gifPrefix + ' link.', 'removegif'),
    'tojicount': ('Returns how many times a user has invoked Toji.', tojiCount, command + '{tojicount} {target} where {target} is a ping.', 'tojicount'),
    'leaderboard': ('Returns a ranked list of TojiCounts.', tojilb, command + '{leaderboard}', 'leaderboard')
}
