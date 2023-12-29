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
    cnx = databaseConnect()
    cursor = cnx.cursor(buffered=True)
    query = 'SELECT gif_url FROM gifs'
    cursor.execute(query)
    for (gif_url) in cursor:
        if gifShortURL in str(gif_url):
            print(cursor)
            cursor.close()
            cnx.close()
            return True
        else:
            pass
    cursor.close()
    cnx.close()

def addGifQuery(gifShortURL, userID):
    cnx = databaseConnect()
    cursor = cnx.cursor()
    sql = '''
        INSERT IGNORE INTO gifs (gif_url, user_id)
        VALUES (%s, %s)
    '''
    val = [
        (str(gifShortURL), str(userID))
    ]
    cursor.executemany(sql, val)
    cnx.commit()
    print("Query successful")
    cursor.close()
    cnx.close()

def removeGifQuery(gifShortURL):
    cnx = databaseConnect()
    cursor = cnx.cursor()
    sql = "DELETE FROM gifs WHERE gif_url = '{}';".format(gifCleaner(gifShortURL))
    cursor.execute(sql)
    cnx.commit()
    print("Query successful")
    cursor.close()
    cnx.close()

def tojiSummon():
    cnx = databaseConnect()
    cursor = cnx.cursor()
    query = 'SELECT * FROM gifs'
    cursor.execute(query)
    gifCandidates = ['toji-jjk-jujutsu-kaisen-tuesday-toji-picmix-gif-8168723334892853958']
    for (gif_id, gif_url, user_id) in cursor:
        print(gif_url)
        gifCandidates.append("{}".format(gif_url))
    cursor.close()
    cnx.close()
    return gifCandidates
