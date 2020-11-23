from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import twichapi
import time


app = Flask(__name__)


line_bot_api = LineBotApi('YSPO5Lo95dWQ8bsn2EEdidVdkljkoDZ6jP1T2cKstGiF1gqu45sdHzujEaCP7CCNdmJarygBaMvmPS8ak8LzgZ54CN9pYO8ZTKDATJs8DzSSqQf6oKWsVruBdm1ZDiO0MgT1EDq60OnECgzuoNLR0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7bb0bef8815d63997732ee31994fa807')


# 接收LINE的資訊，簡單來說就是使用API
@app.route("/callback", methods=['POST']) #這邊是將網址多輸入callback就會執行
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)
    

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def Speak(event):  #讓LineBot對使用者做回應
    
    if '!' in event.message.text:
        if '!追隨' in event.message.text :
            data=twichapi.FL()
            d={}
            text=''
            for i in data['streams']:
                n=i['channel']['display_name']
                url='https://www.twitch.tv/'+i['channel']['name']
                d[n]=url
            for i,j in d.items():
                text+= i+':'+j+'\n'

            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text
            ))                           
        else:
            l=list(event.message.text)
            for i in range(len(l)):
                if l[i]=='!':
                    if i != len(l)-1:
                        l=l[i+1:]
                        break
                    else:
                        l=['1','1']

            l=''.join(l)
            data=twichapi.API(l)
            if data==False:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='該實況主目前沒有開台')
                )
            else:
                url='https://www.twitch.tv/'+l
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='{}\n實況標題:{}\n實況分類:{}\n觀看人數:{}\n連結:{}'
                    .format(data[0]['user_name'],data[0]['title'],data[0]['game_name'],data[0]['viewer_count'],url))
                    )                    
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='請輸入正確指令\n!實況主帳號:查詢該實況主是否開台\n!追隨:查詢追隨名單中開台的實況主')
        )


if __name__ == "__main__":
    app.run()
    
   
       


    
    
