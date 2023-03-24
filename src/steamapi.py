import urllib
import json
import os
from dotenv import find_dotenv, load_dotenv

def getSteamProfilebyID(steamID):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+os.environ['STEAM_API_KEY']+'&steamids='+steamID
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['response']['players'][0]

def getSteamGame(appId):
    url = 'https://store.steampowered.com/api/appdetails?appids='+appId
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data[appId]['data']

def GetOwnedGames(steamID):
    url = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+os.environ['STEAM_API_KEY']+'&steamid='+steamID+'&format=json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['response']['games']

def GetRecentlyPlayedGames(steamID):
    url = 'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key='+os.environ['STEAM_API_KEY']+'&steamid='+steamID+'&format=json'
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    return data['response']['games']