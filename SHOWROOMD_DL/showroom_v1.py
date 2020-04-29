import datetime
import time
import urllib
from urllib import request
import re
import os
import streamlink
import subprocess

def showroomislive(url):
    with request.urlopen(url) as f:
        page = f.read().decode('utf-8')
        f.close
    pattern = re.compile('<script id="js-live-data"(.*?)"></script>')
    result = re.search(pattern, page)
    is_live = result.group(1)
    pattern = re.compile('<title>(.*?)</title>')
    result = re.search(pattern, page)
    room_name = result.group(1)
    if len(is_live) > 10000:
        is_live_flag = True
    else:
        is_live_flag = False
    return is_live_flag, room_name

def livedownload(url,name):
    showroom_content = showroomislive(url)
    flag = showroom_content[0]
    if flag:
        filename = showroom_content[1]
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        filename = re.sub(rstr, " ", filename)
        print(name + "record start")
        filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
        subprocess.call(["streamlink", url, 'high', "--hls-segment-timeout", "1", "-o", filename,])
    if not flag:
        print("record not start")
nagomi_url ="https://www.showroom-live.com/digital_idol_22"
nagomi_name = "西條和"
aina_url ="https://www.showroom-live.com/digital_idol_15"
aina_name = "武田愛奈"
a = showroomislive(nagomi_url)
print(a)
a = showroomislive(aina_url)
print(a)