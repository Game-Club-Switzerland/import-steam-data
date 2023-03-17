import os
from dotenv import find_dotenv, load_dotenv
import json
import xmltodict
import urllib
from s3client import s3client

load_dotenv(find_dotenv())

def getGroup():
    response = urllib.request.urlopen(os.environ['STEAM_GROUP_URL']).read()
    data = xmltodict.parse(response)
    return data

# dict to json file
def dictToJsonFile(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

# data to s3 bucket 
def dictToS3(data, bucket, filename):
    s3 = s3client()
    s3.put_object(
        Bucket=bucket, 
        Key=filename, 
        Body=json.dumps(data), 
        ACL='public-read',
        ContentType='application/json')

def __main__():
    print("Import Group")
    group = getGroup()
    dictToS3(group, os.environ['S3_BUCKET'], os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAM_GROUP_ID']+'.json',)

if __name__== "__main__":
    __main__()