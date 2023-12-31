from config import *
import mysql.connector

def tojiStateChecker(bool):
    enabledStatement = 'armed and ready'
    disabledStatement = 'disabled. Toji is dead for the third time'

    if bool == 1:
        return enabledStatement
    elif bool == 0:
        return disabledStatement
    else:
        return 

def databaseConnect():
    cnx = None
    cnx = mysql.connector.connect(user=dbUser, password=dbPassword, host=dbHost, database=dbDatabase)
    print("MySQL Database connection successful")

    return cnx

def gifValidator(gifURL):
    if gifPrefix in gifURL:
        return True
    else:
        return False

def gifCleaner(gifValidURL):
    shortURL = gifValidURL.replace(gifPrefix, '')
    return shortURL

def gifDuplicateDetector(gifShortURL):
    query = 'SELECT gif_url FROM gifs'
    database = sqlQuery(query, False, True)
    for (gif_url) in database:
        if gifShortURL in str(gif_url):
            return True
        else:
            pass
    return False

def addGifQuery(gifShortURL, userID):
    query = "INSERT IGNORE INTO gifs (gif_url, user_id) VALUES ('{}', '{}')".format(str(gifShortURL), str(userID))
    sqlQuery(query, True, False)

def removeGifQuery(gifShortURL):
    query = "DELETE FROM gifs WHERE gif_url = '{}';".format(gifCleaner(gifShortURL))
    sqlQuery(query, True, False)

def tojiSummon():
    query = 'SELECT * FROM gifs'
    database = sqlQuery(query, False, True)
    gifCandidates = ['toji-jjk-jujutsu-kaisen-tuesday-toji-picmix-gif-8168723334892853958']
    for (gif_id, gif_url, user_id) in database:
        gifCandidates.append("{}".format(gif_url))
    return gifCandidates

def countValidate(targetUID):
    query = "SELECT * FROM tojicount;"
    database = sqlQuery(query, False, True)
    for (count_id, uid, count) in database:
        if targetUID in uid:
            return True
        else:
            pass
    return False

def countNew(UID):
    query = "INSERT IGNORE INTO tojicount (uid, count) VALUES ('{}', 1);".format(UID)
    sqlQuery(query, True, True)

def countCheck(UID):
    query = "SELECT count FROM tojicount WHERE uid = '{}';".format(UID)
    for count in sqlQuery(query, False, True):
        counter = count
    return counter[0]

def countUpdate(counter, uid):
    counter += 1
    query = "UPDATE tojicount SET count = {} WHERE uid = '{}';".format(counter, uid)
    sqlQuery(query, True, False)

def countList():
    query = "SELECT uid, count FROM tojicount;"
    database = sqlQuery(query, False, True)
    leaderboard = {}
    for (uid, count) in database:
        leaderboard[str(count)] = uid
    sortedLeaderboard = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
    return sortedLeaderboard

def sqlQuery(query, commit, returnValue):
    cnx = databaseConnect()
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    if commit == True:
        cnx.commit()
    if returnValue == True:
        output = cursor.fetchall()
    cursor.close()
    cnx.close()
    if returnValue == True:
        return output
