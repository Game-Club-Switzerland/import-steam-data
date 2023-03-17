import os
from dotenv import find_dotenv, load_dotenv
import json
import xmltodict
import urllib
import boto3

load_dotenv(find_dotenv())

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=os.environ['S3_ACCESS_KEY'],
        aws_secret_access_key=os.environ['S3_SECRET_ACCESS_KEY'],
        endpoint_url=os.environ['S3_ENDPOINT'],
    )
    return s3_client

def getGroup():
    response = urllib.request.urlopen(os.environ['STEAMGROUPURL']).read()
    data = xmltodict.parse(response)
    return data

# dict to json file
def dictToJsonFile(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

# data to s3 bucket 
def dictToS3(data, bucket, filename):
    s3 = s3client()
    s3.put_object(Bucket=bucket, Key=filename, Body=json.dumps(data), ACL='public-read')

def __main__():
    print("Import Group")
    group = getGroup()
    dictToS3(group, os.environ['S3_BUCKET'], 'api/rest/v1/steam/group/103582791430857185.json',)

if __name__== "__main__":
    __main__()