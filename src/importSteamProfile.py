import os
from dotenv import find_dotenv, load_dotenv
import xmltodict
import urllib
from s3client import s3client

load_dotenv(find_dotenv())

## Load Memberlist from S3 Storage
def getGroupfromS3():
    print(os.environ['S3_BUCKET'])
    response = s3client.get_object(
        Bucket=os.environ['S3_BUCKET'],
        Key=os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAMGROUPID']+'.json',
    )
    return response

def getGroup():
    url = 'https://'+os.environ['S3_BUCKET']+'.sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT']+os.environ['S3_OBJECT_STEAM_GROUP_URL']+os.environ['STEAMGROUPID']+'.json'
    response = urllib.request.urlopen(url).read()
    data = xmltodict.parse(response)
    return data

## Load Steam Profile from API

## Update Steam Profile in S3 Storage

## Update Play List with Player to S3 Storage

def __main__():
    print("Import SteamProfile")
    print("Load Members from Group")
    group = getGroup()
    print(group)


if __name__== "__main__":
    __main__()