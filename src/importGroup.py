import os
from dotenv import find_dotenv, load_dotenv
import json
import xmltodict
import urllib

load_dotenv(find_dotenv())

def getGroup():
    response = urllib.request.urlopen(os.environ['STEAMGROUPURL']).read()
    data = xmltodict.parse(response)
    return data

# dict to json file
def dictToJsonFile(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp)

def __main__():
    print("Import Group")
    group = getGroup()
    print(group)
    dictToJsonFile(group, '../public/group.json')
    print(os.environ['APIKEY'])

if __name__== "__main__":
    __main__()