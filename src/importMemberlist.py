import os
from dotenv import find_dotenv, load_dotenv
import json
import xmltodict
import urllib

load_dotenv(find_dotenv())

def getMembers():
    response = urllib.request.urlopen(os.environ['STEAMGROUPURL']).read()

    data = xmltodict.parse(response)
    return data

def __main__():
    print("Import Members")
    members = getMembers()
    print(members)
    print(os.environ['APIKEY'])

if __name__== "__main__":
    __main__()