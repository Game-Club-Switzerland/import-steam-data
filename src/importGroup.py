import os
from dotenv import find_dotenv, load_dotenv
import xmltodict
import urllib
from s3client import s3client, dictToS3

load_dotenv(find_dotenv())

def getGroup():
    response = urllib.request.urlopen(os.environ['STEAM_GROUP_URL']).read()
    data = xmltodict.parse(response)
    return data

def __main__():
    print("Import Group")
    group = getGroup()
    dictToS3(group, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAM_GROUP_ID']+'.json',)

if __name__== "__main__":
    __main__()