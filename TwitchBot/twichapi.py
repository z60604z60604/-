import requests
import json
import time

def API(who):
    endpoint = "https://api.twitch.tv/helix/streams?"

    headers = {"Client-ID": "2n84o544ggw9qjlu375ca1mn5x5t7s",
            'Authorization':'Bearer 1j5apimj63d4xv3mm9kl64ryurdjj7'
            }
    
    params = {"user_login": who}
    data=requests.get(endpoint,headers=headers,params=params)
    data=data.json()
    if data['data']== []:
        return False
    else:
        return data['data']
def FL():
    endpoint ="https://api.twitch.tv/kraken/streams/followed"

    headers = {"Client-ID": "2n84o544ggw9qjlu375ca1mn5x5t7s",
            "Authorization": "OAuth t1afmp9grqz8nlt3chzmh34pqxazjk",
            "Accept":"application/vnd.twitchtv.v5+json",
        
            }

    data=requests.get(endpoint,headers=headers)
    data=data.json()
    return data

   
  
    

