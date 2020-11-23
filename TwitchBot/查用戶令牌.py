# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:13:24 2020

@author: fomsin
"""



import requests
import json
#https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=2n84o544ggw9qjlu375ca1mn5x5t7s&redirect_uri=https://www.twitch.tv/&scope=viewing_activity_read&state=c3ab8aa609ea11e793ae92361f002671
data=requests.get('https://id.twitch.tv/oauth2/authorize'+
    '?client_id=2n84o544ggw9qjlu375ca1mn5x5t7s'+
    '&redirect_uri=https://www.twitch.tv/'+
   '&response_type=code'+
    '&scope=<space-separated list of scopes>')



data=requests.post('https://id.twitch.tv/oauth2/token'+
   '?client_id=2n84o544ggw9qjlu375ca1mn5x5t7s'+
   '&client_secret=p8na4crplh5e7aszjebo6w7g6rrcrt'+
   '&code=6tne8ws7xzr29sqeo00uvjn2y254qa'+
   '&grant_type=authorization_code'+
   '&redirect_uri=https://www.twitch.tv/')
data=data.json()

#應用程式令牌
data=requests.post('https://id.twitch.tv/oauth2/token?client_id=2n84o544ggw9qjlu375ca1mn5x5t7s&client_secret=p8na4crplh5e7aszjebo6w7g6rrcrt&grant_type=client_credentials')
    
data=data.json()