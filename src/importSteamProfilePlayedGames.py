import os
from dotenv import find_dotenv, load_dotenv
import json
import urllib
from s3client import dictToS3
from steamapi import GetRecentlyPlayedGames,GetOwnedGames
import time

load_dotenv(find_dotenv())

def getGroup():
    url = 'https://'+os.environ['S3_BUCKET']+'.sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT']+'/'+os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAM_GROUP_ID']+'.json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['memberList']['members']['steamID64']


GetRecentlyPlayedGames

def getSteamProfileRecentlyPlacedGamesfromGroup(group):
    for member in group:
        print(str(member))
        recentlyPlayedGames = GetRecentlyPlayedGames(member)
        ownedGames = GetOwnedGames(member)
        #print(profile)
        dictToS3(recentlyPlayedGames, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_PROFILE_PATH']+'/'+member+'/'+'GetRecentlyPlayedGames.json',)
        dictToS3(ownedGames, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_PROFILE_PATH']+'/'+member+'/'+'GetOwnedGames.json',)
        time.sleep(1)

def __main__():
    print("Import Steam Group Members")
    groupList = getGroup()
    print(groupList)
    print("add Steam Profile Recently Placed Games to S3")
    getSteamProfileRecentlyPlacedGamesfromGroup(groupList)

if __name__== "__main__":
    __main__()