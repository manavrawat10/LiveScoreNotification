# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:16:50 2018

@author: Manvenddra
"""

import bs4 as bs
from urllib import request
from  win10toast import ToastNotifier
import time
#from plyer import notification
toaster = ToastNotifier()

url = "http://www.cricbuzz.com/cricket-match/live-scores"
i=1
while True:
    sauce = request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,"lxml")
    #print(soup)
    score = []
    results = []
    #for live_matches in soup.find_all('div',attrs={"class":"cb-mtch-lst cb-col cb-col-100 cb-tms-itm"}):
    for div_tags in soup.find_all('div', attrs={"class": "cb-lv-scrs-col text-black"}):
        score.append(div_tags.text)
    for result in soup.find_all('div', attrs={"class": "cb-lv-scrs-col cb-text-complete"}):
        results.append(result.text)
    toaster.show_toast(title=score[0],msg=results[0])
    time.sleep(60*5)
    if i==(180/5):
        break
    i=i+1
