from config import command

def msgParse(message):
    if command in message:
        parsedMessage = message.replace(command, '')
        return parsedMessage
