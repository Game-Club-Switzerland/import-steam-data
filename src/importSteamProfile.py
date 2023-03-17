import os
from dotenv import find_dotenv, load_dotenv
import json
import urllib
from s3client import s3client, dictToS3

load_dotenv(find_dotenv())

## Load Memberlist from S3 Storage
def getGroupfromS3():
    print(os.environ['S3_BUCKET'])
    response = s3client.get_object(
        Bucket=os.environ['S3_BUCKET'],
        Key=os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAM_GROUP_ID']+'.json',
    )
    return response

def getGroup():
    url = 'https://'+os.environ['S3_BUCKET']+'.sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT']+os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAM_GROUP_ID']+'.json'
    print(url)
    url='https://sos-ch-dk-2.exo.io/gameclubch/api/rest/v1/steam/group/103582791430857185.json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['memberList']['members']['steamID64']

## Load Steam Profile from API
def getSteamProfile(steamID):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+os.environ['STEAM_API_KEY']+'&steamids='+steamID
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['response']['players'][0]

def getSteamProfilefromGroup(group):
    for member in group:
        print(member)
        profile = getSteamProfile(member)
        #print(profile)
        dictToS3(profile, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_PROFILE_PATH']+member+'.json',)

## Update Steam Profile in S3 Storage

## Update Play List with Player to S3 Storage

def __main__():
    print("Import SteamProfile")
    print("Load Members from Group")
    group = getGroup()
    #print(group)
    getSteamProfilefromGroup(group)


if __name__== "__main__":
    __main__()