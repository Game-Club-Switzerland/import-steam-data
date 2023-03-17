import os
from dotenv import find_dotenv, load_dotenv
import boto3

load_dotenv(find_dotenv())

def s3client():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id=os.environ['S3_ACCESS_KEY'],
        aws_secret_access_key=os.environ['S3_SECRET_ACCESS_KEY'],
        endpoint_url='https://sos-'+os.environ['S3_REGION']+os.environ['S3_ENDPOINT'],
    )
    return s3_client