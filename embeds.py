from config import *
import discord
import parse

generalColour = 0xb300ff
successColour = 0x00ff00
errorColour = 0xff0000

# HELP

def helpCommand():
    embedVar = discord.Embed(title="Help", description="Here is a list of commands:", color=generalColour)
    embedVar.add_field(name= command + "help", value="Returns a list of commands.", inline=False)
    embedVar.add_field(name= command + "status", value="Shows whether the bot is online.", inline=False)
    embedVar.add_field(name= command + "toggle", value="Toggle's bot auto respond.", inline=False)
    return embedVar

# TOJI TOGGLE

def tojiOn():
    embedVar = discord.Embed(title="Toji has been enabled!", description="To turn Toji back off, use " + command + "toggle", color=successColour)
    return embedVar

def tojiOff():
    embedVar = discord.Embed(title="Toji has been disabled!", description="To turn Toji back on, use " + command + "toggle", color=successColour)
    return embedVar

# TOJI STATE

def tojiState(alive):
    embedVar = discord.Embed(title="TojiToggle", description="Toji is currently " + parse.tojiStateChecker(alive), color=0x00ff00)
    embedVar.add_field(name= command + "toggle", value="To toggle Toji's auto respond.", inline=False)
    return embedVar

# ADDGIF

def addgifCommand():
    embedvar = discord.Embed(title="Adding GIF", description="Attempting to add the desired GIF to the database.", color=generalColour)
    return embedvar

def addgifSuccess(link):
    embedvar = discord.Embed(title="GIF Successfully Added!", description="The GIF you have requested has been successfully added!", color=successColour)
    embedvar.set_image(url=link)
    return embedvar

# REMOVEGIF

def removegifCommand():
    embedvar = discord.Embed(title="Removing GIF", description="Attempting to remove selected GIF.", color=generalColour)
    return embedvar

def removegifSuccess():
    embedvar = discord.Embed(title="Successfully removed GIF!", description="GIF has been removed successfully!", color=successColour)
    return embedvar

# ERRORS

def invalidCommand():
    embedVar = discord.Embed(title="Invalid Command", description="You have sent an invalid command!", color=errorColour)
    embedVar.add_field(name="For a list of commands, try:", value= command + "help", inline=False)
    return embedVar

def invalidState():
    embedVar = discord.Embed(title="ERROR", description="CONTACT MSG WITH ERROR code [TOJI_TOGGLE_CRIT_FAIL_ELIF]", color=errorColour)
    return embedVar

def addgifInvalid():
    embedvar = discord.Embed(title="Failure: Invalid", description="Failed to add GIF to the database as the source is not " + gifPrefix, color=errorColour)
    return embedvar

def gifDuplicate():
    embedvar = discord.Embed(title="Failure: Duplicate", description="Failed to add GIF to the database as the GIF is already in the database.", color=errorColour)
    return embedvar

def gifFake():
    embedvar = discord.Embed(title="GIF Doesn't Exist", description="Check your link and try again.", color=errorColour)
    return embedvar

# DEBUG

def killCommand():
    embedVar = discord.Embed(title="TOJIBOT PROCESS HAS ENDED", description="CONTACT MSG WITH ERROR code [TOJI_BOT_DEATH_KILL_MANUAL]", color=errorColour)
    return embedVar
