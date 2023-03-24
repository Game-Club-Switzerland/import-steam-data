
## Steam Web API - Docu

https://developer.valvesoftware.com/wiki/Steam_Web_API


### Game Info

Game by appId
https://store.steampowered.com/api/appdetails?appids=440

All Games
https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json


## Deploy our Game List
aws s3 sync ./public/ s3://gameclubch/ --endpoint-url https://sos-ch-dk-2.exo.io --acl "public-read" --profile gameclubchapp