import requests
from selenium import webdriver
import time
import json
import bs4
import calendar
import text02
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import urllib.request as req
import csv
import os 
import numpy as np
from tkinter import *
from tkinter import  messagebox
import tkinter.ttk as ttk
from PIL import Image,ImageTk
import urllib.request
import gzip
#爬蟲
#url='https://opendata.epa.gov.tw/Data/contents/AQI/'
#html=requests.get(url)
#bs4data=bs4.BeautifulSoup(html.text,'lxml')
#data=bs4data.find('p','color_a')
#url=data.find('a')['href']
#
#time.sleep(3)
#html2=requests.get(url)
#data=json.loads(html2.text)

#直接讀
with open("aqi11_23",'r',encoding='utf-8') as load_f:
     data = json.load(load_f)
#with open('aqi11_23','w') as file_object:
#    json.dump(data,file_object)

#資料處理
import pandas as pd
data=pd.DataFrame(data)
city=[]
where=[]
for i in  data['County']:
    if i not in city:
       city.append(i)
for i in data['SiteName']:
    where.append(i)



 
#主頁面
class LoginPage(object):

    def goAQI(self):
        self.root.destroy()
        AQI()
    def gotemp(self):
        self.root.destroy()
        TEMP()
    def getweather(self):
        self.root.destroy()
        weather()
 
    def __init__(self):
        self.root = Tk()
        self.root.title('天氣查詢系統')       
        im=Image.open("unnamed.jpg")
        img=ImageTk.PhotoImage(im)        
      
        
        canvas = Canvas(self.root, width=250,height=250,bd=0, highlightthickness=0)
        
 
        Label1=Label(self.root,text='歡迎使用天氣查詢系統',bg='lightblue',fg='black',font=('微軟正黑體',12))
        Button1=Button(self.root, text="各地空氣品質查詢",command=self.goAQI)
        Button3=Button(self.root, text="台中歷年氣溫、降雨量查詢",command=self.gotemp)
        Button2=Button(self.root, text="各地近一周天氣查詢",command=self.getweather)
        
        canvas.create_window(125,20, window=Label1)
        canvas.create_window(125,70, window=Button1)
        canvas.create_window(125,145, window=Button2)
        canvas.create_window(125,220, window=Button3)        
        canvas.create_image(125,125, image=img)
        canvas.pack()
        
        self.root.mainloop()
 
#空氣品質查詢
class AQI(object): 
    def AQIBACK(self):
        self.root.destroy()
        LoginPage()  
    def get(self,event):
        if self.var.get() != '':
            l=[]
            for i in range(len(data)):
                if data.loc[i]['County']==self.var.get() :                   
                    l.append(data.loc[i]['SiteName'])
            self.cb1['value']=tuple(l)
            self.var1.set('')
            
    def datashow(self):
        if self.var1.get() != '':
            self.lb.delete(0,len(data))
            for i in range(len(data)):
                 if data.loc[i]['SiteName']==self.var1.get():
                     for x in data[:]:
                        self.lb.insert(END,'{} : {}'.format(x,data.loc[i][x]))
        else:
            messagebox.showinfo('未選擇','請先選取位置')
 

 
    def __init__(self):
        dic={'PM2.5':'● 細懸浮微粒 (PM2.5)\n交通污染 (道路揚塵、車輛排放廢氣)、營建施工、工業污染、境外污染、露天燃燒',
         'PM10':'● 懸浮微粒 (PM10)\n交通污染 (道路揚塵、車輛排放廢氣)、營建施工、工業污染、境外污染、露天燃燒',
         'SO2':'● 二氧化硫 (SO2)\n自然界 (火山)、燃料中硫份燃燒。',
         'NOx':'● 氮氧化物 (NOx)\n燃燒過程中，空氣中氮或燃料中氮化物氧化而成，光化學反應中可反應成二氧化氮。',
         'CO':'● 一氧化碳 (CO)\n除森林火災、甲烷氧化及生物活動等自然現象產生外石化等燃料之不完全燃燒產生',
         'O3':'● 臭氧 (O3)\n係一種由氮氧化物、反應性碳氫化合物及日光照射後產生之二次污染物。' 
         }
        self.root=Tk()
        self.root.title('各地區空氣品質查詢')
        self.root.geometry('500x500')
        self.root.configure(bg='lightblue')
        
        notebook =ttk.Notebook(self.root)
        
           
        frame1 = Frame() 
        label1 = Label(frame1,text=dic['PM2.5'],wraplength =350,justify='left')
        label1.pack(padx=10,pady=10)
        notebook.add(frame1,text='PM2.5')
        
        frame2 = Frame() 
        label2 = Label(frame2,text=dic['PM10'],wraplength =350,justify='left')
        label2.pack(padx=10,pady=10)
        notebook.add(frame2,text='PM10')
        
        frame3 = Frame() 
        label3 = Label(frame3,text=dic['SO2'],wraplength =350,justify='left')
        label3.pack(padx=10,pady=10)
        notebook.add(frame3,text='SO2')
        
        frame4 = Frame() 
        label4 = Label(frame4,text=dic['NOx'],wraplength =350,justify='left')
        label4.pack(padx=10,pady=10)
        notebook.add(frame4,text='NOx')
        
        frame5 = Frame() 
        label5 = Label(frame5,text=dic['CO'],wraplength =350,justify='left')
        label5.pack(padx=10,pady=10)
        notebook.add(frame5,text='CO')
        
        frame6 = Frame() 
        label6= Label(frame6,text=dic['O3'],wraplength =350,justify='left')
        label6.pack(padx=10,pady=10)
        notebook.add(frame6,text='O3')
        #卷軸
        roll=Scrollbar(self.root)                
        #建立清單
        self.lb = Listbox(self.root,height=10,width=30,font=('微軟正黑體',12),yscrollcommand=roll.set) 
        #按鈕
        sure=Button(text='搜尋',command=self.datashow           
        )
        back=Button(text='回主選單',command=self.AQIBACK           
        )  
        #標籤
        selectcity=Label(self.root,text='選擇城市',bg='blue',fg='yellow')
        selectwhere=Label(self.root,text='選擇地區',bg='blue',fg='yellow')
        
        
        #選擇縣市
        self.var=StringVar()
        self.cb=ttk.Combobox(self.root,textvariable=self.var)
        self.cb.bind('<<ComboboxSelected>>',self.get)
        self.cb['value']=tuple(city)
        
        
        #選擇地區
        self.var1=StringVar()
        self.cb1=ttk.Combobox(self.root,textvariable=self.var1)
        self.cb1['value']=tuple(where)
        #定位
        selectcity.place(x=0,y=0)
        selectcity.place(x=0,y=0)
        self.cb.place(x=80,y=0)
        selectwhere.place(x=0,y=30)
        self.cb1.place(x=80,y=30)
        sure.place(x=300,y=15)
        back.place(x=420,y=10)
        self.lb.place(x=30,y=100)
        roll.place(x=400,y=100,relheight=0.53)
        notebook.place(x=30,y=380,relheight=0.3,relwidth=0.8)
        
        self.root.mainloop()
#氣溫降水量查詢
class TEMP(object):
    def TEMPBACK(self):
        self.window.destroy()
        LoginPage() 
    def table_find(year,month,vals = ''):
        url = "https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker="+year+"-"+month
        with req.urlopen(url) as response:
            data = response.read().decode('utf-8')
    
        root = bs4.BeautifulSoup(data,'html.parser')
    
        tr = root.find_all('tr')
        tr1 = tr[2:len(tr)]
        tr1_text = []
        for i in range(len(tr1)):
            tr1_list = tr1[i].text
            tr1_text.append(tr1_list.split('\n'))
            del tr1_text[i][0]
        tr_key = tr1_text[0]
        td = tr_key.index(vals)    
        for j in range(len(tr1_text)):
            for k in range(len(tr1_text[i])):
                tr1_text[j][k] = tr1_text[j][k].replace('\xa0','')
        tr1_text = np.array(tr1_text)
        return tr1_text[:,[0,td]]
    def get_temperature(self):
        mon_temp = text02.table_find(self.cb1.get(),self.cb2.get(),"氣溫(℃)")
        f = Figure(figsize=(10, 6), dpi=100)
        t = f.add_subplot(111) 
        t.set_title("temperature")
        t.set_xlabel('day')
        t.set_ylabel('temperature(℃)')
        x = [p[0] for p in mon_temp[2:]]
        y = [p[1] for p in mon_temp[2:]]
        for i in range(len(y)):
            if y[i] == '...':
                y[i] = None
            else:
                y[i] = float(y[i])
        t.plot(x, y, '-o')  
        
        canvas = FigureCanvasTkAgg(f, master=self.window)
        canvas.draw() 
        canvas.get_tk_widget().place(x = 20, y = 40) 
        plt.show()
    
    def get_rain(self):
        mon_temp = text02.table_find(self.cb1.get(),self.cb2.get(),"降水量(mm)")
        f = Figure(figsize=(10, 6), dpi=100)
        r = f.add_subplot(111) 
        r.set_title("Rainfall")
        r.set_xlabel('day')
        r.set_ylabel('rainfall(mm)')
        x = [p[0] for p in mon_temp[2:]]
        y = [p[1] for p in mon_temp[2:]]
        for i in range(len(y)):
            if y[i] == 'T':
                y[i] = 0
            elif y[i] == '...':
                y[i] = None
            else:
                y[i] = float(y[i])
        r.plot(x, y, '-o')  
        
        canvas = FigureCanvasTkAgg(f, master=self.window)
        canvas.draw() 
        canvas.get_tk_widget().place(x = 20, y = 40) 
        plt.show()
    def __init__(self):
        self.window = Tk()
        # frame1 = tk.Frame(window)
        self.window.title('台中天氣')
        self.window.geometry('1200x720')
        self.window.configure(background='LightSteelBlue')
        years = ['2015','2016','2017','2018','2019','2020']
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
        
        lab1 = Label(self.window,text="年份:", background = 'LightSteelBlue').place(x=10, y=10) 
        lab2 = Label(self.window,text="月份:", background = 'LightSteelBlue').place(x=120, y=10) 
        
        
        var1 = StringVar()
        self.cb1 = ttk.Combobox(self.window,textvariable = var1, value = (years))
        self.cb1.current(0)
        self.cb1.place(x=50, y=10, width = 60, height = 20)
        
        var2 = StringVar()
        self.cb2 = ttk.Combobox(self.window,textvariable = var2, value = (months))
        self.cb2.current(0)
        self.cb2.place(x=160, y=10, width = 60, height = 20) 
        
        button1 = Button(self.window,text = "氣溫(℃)", command = self.get_temperature)
        button1.place(x=240, y=10)
        back=Button(text='回主選單',command=self.TEMPBACK           
        ).place(x=1100,y=10)
        
        button1 = Button(self.window,text = "降水量(mm)", command = self.get_rain)
        button1.place(x=340, y=10)
        
        self.window.mainloop()
class weather(object):
    def destory(self):
        self.root1.destroy()
    def re(self):
        self.root.destroy()
        LoginPage()
               
    def get_weather_data(self) :
        self.city_name = self.enter.get()
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(self.city_name)
        
        
        
        weather_data = urllib.request.urlopen(url1).read()
        
        weather_data = gzip.decompress(weather_data).decode('utf-8')
      
        self.weather_dict = json.loads(weather_data)
        
        if  self.weather_dict.get('desc') == 'invilad-citykey':
            print(messagebox.askokcancel("xing","城市名稱有誤,請重新輸入"))
        else:
          
            self.show_data(self.weather_dict,self.city_name)
    
    def show_data(self,weather_dict,city_name):
        forecast = weather_dict.get('data').get('forecast')
        self.root1=Tk()
        self.root1.geometry('800x280')
        self.root1.title(city_name + '天氣狀況')
        
        
        for i in range(5):
            LANGS = [(forecast[i].get('date'),'日期'),
                        (forecast[i].get('high'),'最高温'),
                        (forecast[i].get('low'),'最低溫'),
                        (forecast[i].get('type'),'天氣')]
            group = LabelFrame(self.root1,text = '天氣狀況',padx = 0,pady = 0)
            group.pack(padx=11,pady=0,side = LEFT)
            for lang, value in LANGS:
                c = Label(group,text = value + ': ' + lang)
                c.pack(anchor = W)
        Label(self.root1,text = '這週天氣如下,請注意保暖' ,
                fg = 'green').place(x=40,y=20,height=40)
        Button(self.root1,text = '確認並退出',width=10,command =self.destory).place(x=500,y=230,width = 80,height=40)#
        self.root1.mainloop()
    def __init__(self):
        self.root = Tk()
        self.root.title('天氣查詢')
        Label(self.root,text = '請輸入城市').grid(row=0,column=0)
        self.enter = Entry(self.root)
        self.enter.grid(row = 0,column=1,padx = 20, pady = 20)
        self.enter.delete(0,END)
        self.enter.insert(0,'台中')
        running = 1
    
     
        Button(self.root, text = "確認",width=10,command = self.get_weather_data)\
                .grid(row = 3, column=0,sticky = W, padx = 10, pady = 5)
        Button(self.root, text = '退出',width=10,command = self.re)\
                .grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
        if running==1:
            self.root.mainloop()


    
 
 
if __name__ == '__main__':
    LoginPage()
 

