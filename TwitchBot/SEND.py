from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import json
import time
line_bot_api = LineBotApi('YSPO5Lo95dWQ8bsn2EEdidVdkljkoDZ6jP1T2cKstGiF1gqu45sdHzujEaCP7CCNdmJarygBaMvmPS8ak8LzgZ54CN9pYO8ZTKDATJs8DzSSqQf6oKWsVruBdm1ZDiO0MgT1EDq60OnECgzuoNLR0wdB04t89/1O/w1cDnyilFU=')
#push message to one user

count=0
live=[]


while True:
        endpoint ="https://api.twitch.tv/kraken/streams/followed"

        headers = {"Client-ID": "2n84o544ggw9qjlu375ca1mn5x5t7s",
                "Authorization": "OAuth 5cqoudrcnzolxc0wevuquzw2uvya49",
                "Accept":"application/vnd.twitchtv.v5+json",
                
                }
        
        data=requests.get(endpoint,headers=headers)
        data=data.json()
        live2=[]
        
        for i in data['streams']:
            live2.append(i['channel']['display_name'])
            if count != 0:
                if i['channel']['display_name'] not in live:
                    name=i['channel']['display_name']
                    url='https://www.twitch.tv/'+i['channel']['name']
                    title=i['channel']['status']
                    game=i['game']
                    line_bot_api.push_message('U4bbbcfa59bc2eb498a82bec7b84601f9', TextSendMessage(text='{}開台了!\n實況標題:{}\n實況分類:{}\n連結:{}'
                            .format(name,title,game,url)))

                    
            if i['channel']['display_name'] not in live:
                live.append(i['channel']['display_name'])
        for i in live:
            if i not in  live2:
                live.remove(i)     
        time.sleep(60) 
        count+=1
        

    
    