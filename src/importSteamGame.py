import os
from dotenv import find_dotenv, load_dotenv
import urllib
import json
from s3client import dictToS3, updateObject
from steamapi import getSteamGame

load_dotenv(find_dotenv())

# import Gamelist from Json
def getGameList():
    url = 'https://'+os.environ['S3_BUCKET']+'.sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT']+'/'+os.environ['S3_OBJECT_GAME_PATH']+'importGames.json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data

def getallGameswithSteamAppID(gameList):
    steamGameList = {}
    for game in gameList:
        if 'steamAppId' in game:
            print(game['steamAppId'])
            steamGameList[game['steamAppId']] = game
    return steamGameList

def addAllSteamGamesToS3(steamGameList):
    for gameSteamAppId in steamGameList:
        print("To S3 Storage")
        print(gameSteamAppId)
        gameSteamData = getSteamGame(gameSteamAppId)
        dictToS3(gameSteamData, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GAME_PATH']+gameSteamAppId+'.json',)
        updateObject(os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GAME_PATH']+'index.json', gameSteamAppId, gameSteamData)

def __main__():
    print("Import Steam Game")
    gameList = getGameList()
    print(gameList)
    print("get all Steam Game")
    steamGameList = getallGameswithSteamAppID(gameList)
    print(steamGameList)
    print("add Steam Games to S3")
    addAllSteamGamesToS3(steamGameList)

if __name__== "__main__":
    __main__()