import json
import urllib
import os
from dotenv import find_dotenv, load_dotenv
from s3client import dictToS3

load_dotenv(find_dotenv())

## Import Group Json from URL
def getPlayerIndexfromUrl():
    #url ='https://gameclubch.sos-ch-dk-2.exo.io/api/rest/v1/steam/player/index.json'
    url = 'https://'+os.environ['S3_BUCKET']+'.sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT']+'/'+os.environ['S3_OBJECT_STEAM_PLAY_PATH']+'index.json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data

## Check if one of the members is gameing
def checkIfPlayerIsPlaying(player):
    # check if player['gameid'] exists
    if 'gameid' in player:
        if player['gameid'] != '0':
            return True
        else:
            return False
    else:
        return False
    
## check if player['gameid'] exists
def checkGameID(player):
    if 'gameid' in player:
        return True
    else:
        return False

def checkPlayerIndex(playerIndex):
    playGroup = {}
    for player in playerIndex:
        if checkIfPlayerIsPlaying(playerIndex[player]):
            playGroup[player] = playerIndex[player]
    dictToS3(playGroup, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_PLAY_PATH']+'index.json',)

def __main__():
    print("Check if Player is playing")
    playerIndex = getPlayerIndexfromUrl()
    checkPlayerIndex(playerIndex)


if __name__== "__main__":
    __main__()
