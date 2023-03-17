import os
from dotenv import find_dotenv, load_dotenv
import xmltodict
import urllib
from s3client import s3client

load_dotenv(find_dotenv())

## Load Memberlist from S3 Storage
def getGroupfromS3():
    response = s3client.get_object(
        Bucket=os.environ['S3_BUCKET'],
        Key=os.environ['S3_OBJECT_STEAM_GROUP_PATH']+os.environ['STEAMGROUPID']+'.json',
    )
    return response

## Load Steam Profile from API

## Update Steam Profile in S3 Storage

## Update Play List with Player to S3 Storage