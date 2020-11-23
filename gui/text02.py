#爬蟲 氣象觀測站單月報表


import urllib.request as req
import bs4
import time
import csv
import os 
import numpy as np


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

    


