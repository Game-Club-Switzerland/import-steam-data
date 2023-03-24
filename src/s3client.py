import os
from dotenv import find_dotenv, load_dotenv
import boto3
import json

load_dotenv(find_dotenv())

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=os.environ['S3_ACCESS_KEY'],
        aws_secret_access_key=os.environ['S3_SECRET_ACCESS_KEY'],
        endpoint_url='https://sos-'+os.environ['S3_REGION']+'.'+os.environ['S3_ENDPOINT'],
    )
    return s3_client

# data to s3 bucket 
def dictToS3(data, bucket, filename):
    s3 = s3client()
    s3.put_object(
        Bucket=bucket, 
        Key=filename, 
        Body=json.dumps(data), 
        ACL='public-read',
        ContentType='application/json')
    
# Get Object, add Value and put it back
def updateObject(bucket, filename, key, value):
    s3 = s3client()
    response = s3.get_object(Bucket=bucket, Key=filename)
    print(" Response:")
    print(response)
    data = response.get('Body').read().decode('utf-8')
    print(" Data:")
    print(data)
    if len(data) == 0 :
        print("No Data")
        json_data = {}
    else:
        json_data = json.loads(data)
    json_data[key] = value
    print("Data:")
    print(json_data)
    s3.put_object(
        Bucket=bucket, 
        Key=filename, 
        Body=json.dumps(json_data), 
        ACL='public-read',
        ContentType='application/json')