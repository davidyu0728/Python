import datetime
import time
import urllib
from urllib import request
import re
import os
import streamlink
import sys

class ShowroomDownload:
    def __init__(self, url):
        self.url = url
    def islivestart(self):
        with request.urlopen(self.url) as f:
            page = f.read().decode('utf-8')
            f.close
        pattern = re.compile('<script id="js-live-data"(.*?)"></script>')
        result = re.search(pattern, page)
        is_live = result.group(1)
        pattern = re.compile('<title>(.*?) - SHOWROOM</title>')
        result = re.search(pattern, page)
        room_name = result.group(1)
        if len(is_live) > 10000:
            is_live_flag = True
        else:
            is_live_flag = False
        return is_live_flag, room_name
    def livedownload(self):
        while 1:
            showroom_content = self.islivestart()
            flag = showroom_content[0]
            name = showroom_content[1]
            if flag:
                rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
                filename = re.sub(rstr, " ", name)
                print(name + "record start")
                filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
                subprocess.call(["streamlink", self.url, 'high', "--hls-segment-timeout", "1", "-o", filename,])
            if not flag:
                #time.sleep(10)
                #pass
                print(name + "record not start")

def isLiveTime(liveDate, liveTime): # time as xx:xx
    #d = datetime.datetime.strptime((liveDate + liveTime) + datetime.timedelta(minutes=-5) , '%Y%m%d%H%M')
    liveTimePlan = datetime.datetime.strptime(liveDate + liveTime, "%Y%m%d%H%M")
    liveTimeMinus = datetime.datetime.strptime(liveDate + liveTime, "%Y%m%d%H%M") + datetime.timedelta(minutes=-5)
    timeNow = datetime.datetime.now() # time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if liveTimePlan > timeNow and timeNow > liveTimeMinus:
        flag = 0
        print("preparing")
        return "preparing"
    if liveTimePlan < timeNow:
        flag = 0
        print("miss")
        return "miss"
    else:
        print("waiting")
        time.sleep(60)
        return True
# argv0:url,argv1:date,argv2:
url = sys.argv[1]
liveDate = sys.argv[2]
liveTime = sys.argv[3]

flag = True
url = "https://www.youtube.com/watch?v=im6M_8uF1t4"
if "youtube" in url:
    urlFlag = "YT"
if = "showroom" in url:
    urlFlag = "SH"
while flag == True:
    flag = isLiveTime("20200501", "1407")
if flag = 0: #trying to download the
    if urlFlag == "YT":
        subprocess.call(["bash","record_youtube.sh", url, "best", "loop", "1"])
    if urlFlag == "SH":
        shdl = ShowroomDownload(url)
        shdl.livedownload
