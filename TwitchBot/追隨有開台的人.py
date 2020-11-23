# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:22:45 2020

@author: fomsin
"""

import requests
import json
endpoint ="https://api.twitch.tv/kraken/streams/followed"

headers = {"Client-ID": "2n84o544ggw9qjlu375ca1mn5x5t7s",
        "Authorization": "OAuth t1afmp9grqz8nlt3chzmh34pqxazjk",
        "Accept":"application/vnd.twitchtv.v5+json",
        
        }

data=requests.get(endpoint,headers=headers)
data=data.json()



        
        
        