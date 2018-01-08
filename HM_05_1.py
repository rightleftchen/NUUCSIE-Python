# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:50:55 2017

@author: Rightleft
"""

import requests
from bs4 import BeautifulSoup        

url = 'http://www.cwb.gov.tw/V7/forecast/taiwan/'
list1 = [ "Taipei_City.htm" , "New_Taipei_City.htm" , "Taoyuan_City.htm" , "Taichung_City.htm", "Tainan_City.htm", 
         "Kaohsiung_City.htm" ,"Keelung_City.htm", "Hsinchu_City.htm","Hsinchu_County.htm" ,"Miaoli_County.htm" ,
          "Changhua_County.htm", "Nantou_County.htm","Yunlin_County.htm" ,"Chiayi_City.htm" ,"Chiayi_County.htm"  ,
          "Pingtung_County.htm" , "Yilan_County.htm" ,"Hualien_County.htm" ,"Taitung_County.htm" ,"Penghu_County.htm",
          "Kinmen_County.htm", "Lienchiang_County.htm"  ]
n=0
list2 = []
list3 = []
while n < len(list1):
    list1[n] = url + list1[n]
    html = requests.get(list1[n])
    html.encoding="utf-8"
    sp = BeautifulSoup(html.text, 'html.parser')
    data1 = sp.find_all("option")  # 縣市
    data2 = sp.find("td")           # 目前溫度
    print(data1[n].text, "  ", data2.text ,"度")
    list2.append(data1[n].text)
    list3.append(data2.text)
    n=n+1
#content= """<table border="1"> """    
"""f=open('weather.html','w')
content += "<tr>"
for i in list2:
    content += "<td>"
    content += i
    content += "</td>"
content += "</tr>"
content +="<tr>"
for j in list3:
    content += "<td>"
    content += j
    content += "</td>"
content += "</tr>"
content += "</table>"
f.write(content)
f.close()"""