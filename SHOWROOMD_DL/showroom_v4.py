import datetime
import time
import urllib
from urllib import request
import re
import os
import streamlink
import sys
import subprocess

class LiveDownload:
    def __init__(self, url):
        self.url = url
    def whichplatfrom(self):
        if "youtube" in self.url:
            urlFlag = "YT"
        if "showroom" in self.url:
            urlFlag = "SH"
        return urlFlag
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
        platfrom = self.whichplatfrom()
        while 1:
            if platfrom == "SH":
                showroom_content = self.islivestart()
                flag = showroom_content[0]
                name = showroom_content[1]
                if flag:
                    rstr = r"[\/\\\:\*\?\"\<\>\|\　]"  # '/ \ : * ? " < > |'
                    filename = re.sub(rstr, " ", name)
                    print(name + "record start")
                    filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
                    subprocess.call(["streamlink", self.url, 'high', "--hls-segment-timeout", "1", "-o", filename,])
                if not flag:
                    #time.sleep(10)
                    #pass
                    print(name + "record not start")
            if platfrom == "YT":
                with request.urlopen(url) as f:
                    page = f.read().decode('utf-8')
                    f.close
                pattern = re.compile('<title>(.*?)</title>')
                result = re.search(pattern, page)
                filename = result.group(1)
                flag = "scheduledStartTime" in page
                if not flag:
                    pattern = re.compile('<title>(.*?)</title>')
                    result = re.search(pattern, page)
                    filename = result.group(1)
                    print(filename + "record start")
                    filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
                    subprocess.call(["streamlink", self.url, 'best', "--hls-segment-timeout", "1", "-o", filename,])
                if flag:
                    print(filename + "record not start")


def isLiveTime(liveDate, liveTime): # time as xx:xx
    #d = datetime.datetime.strptime((liveDate + liveTime) + datetime.timedelta(minutes=-5) , '%Y%m%d%H%M')
    liveTimePlan = datetime.datetime.strptime(liveDate + liveTime, "%Y%m%d%H%M")
    liveTimeMinus = datetime.datetime.strptime(liveDate + liveTime, "%Y%m%d%H%M") + datetime.timedelta(minutes=-3)
    timeNow = datetime.datetime.now() # time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if liveTimePlan > timeNow and timeNow > liveTimeMinus:
        print("preparing")
        return 0
    if timeNow > liveTimePlan:
        print("miss")
        return 0
    if timeNow < liveTimeMinus:
        print("waiting")
        restTimeH = str(datetime.datetime.strptime(str(liveTimePlan - timeNow).split(".")[0], "%H:%M:%S")).split(" ")[1][0:5].split(":")[0]
        restTimeM = str(datetime.datetime.strptime(str(liveTimePlan - timeNow).split(".")[0], "%H:%M:%S")).split(" ")[1][0:5].split(":")[1]
        print(int(restTimeH),int(restTimeM))
        if int(restTimeH) > 1 and int(restTimeM) > 30:
            print("离开始还有 : " + restTimeH + "小时" + restTimeM + "分钟")
            time.sleep(3600)
        if int(restTimeH) == 1 and int(restTimeM) > 30:
            print("离开始还有 : " + restTimeH + "小时" + restTimeM + "分钟")
            time.sleep(600)
        if int(restTimeH) < 1 and int(restTimeM) <= 30:
            print("离开始还有 : " + restTimeH + "小时" + restTimeM + "分钟")
            time.sleep(60)
        return True

# argv0:url,argv1:date,argv2:
# print(len(sys.argv))
if __name__ == "__main__":
    if len(sys.argv)  == 2:
        url = sys.argv[1]
        flag = 0
    if len(sys.argv) == 4:
        url = sys.argv[1]
        liveDate = sys.argv[2]
        liveTime = sys.argv[3]
        flag = True
    while flag == True:
        flag = isLiveTime(liveDate, liveTime)
        #print(flag)
    if flag == 0: #trying to download the
            dl = LiveDownload(url)
            dl.livedownload()
