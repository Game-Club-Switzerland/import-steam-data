import os
from dotenv import find_dotenv, load_dotenv
import xmltodict
import urllib
from s3client import dictToS3, updateObject
from steamapi import getSteamGame

load_dotenv(find_dotenv())

def __main__():
    print("Import Steam Game")
    appid = '440'
    game = getSteamGame(appid)
    print(game)
    print("Add to S3")
    dictToS3(game, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GAME_PATH']+appid+'.json',)
    print("Add to S3 Index")
    updateObject(os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GAME_PATH']+'index.json', appid, game)

if __name__== "__main__":
    __main__()