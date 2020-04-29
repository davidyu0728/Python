import datetime
import time
import urllib
from urllib import request
import re
import os
import streamlink
import subprocess
url = "https://www.showroom-live.com/ME_SAYA_TANIZAKI"
def showroomislive(url):
    with request.urlopen(url) as f:
        page = f.read().decode('utf-8')
        f.close
    pattern = re.compile('<script id="js-live-data"(.*?)"></script>')
    #<title>武田愛奈　22/7(ナナブンノニジュウニ) - SHOWROOM</title>
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

while 1:
    showroom = showroomislive(url)
    flag = showroom[0]
    filename = showroom[1]
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    filename = re.sub(rstr, "_", filename)
    datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    quanlity = "high"

    if flag:
        print("record start")
        filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
        subprocess.call(["streamlink", url, 'high', "--hls-segment-timeout", "5", "--hls-timeout", "5", "-l", "debug", "-o", filename,])
    if not flag:
        print("record not start")
"""
    cmd = ["streamlink", url, 'high', "-o", filename]
    p = subprocess.Popen(cmd,shell=True, close_fds=True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    returncode = p.returncode
    print(returncode)
"""