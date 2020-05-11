#coding=utf-8 
import datetime
import re
import streamlink
import requests 
import subprocess
import sys

def isQkunlive(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    r = requests.get(url=url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    page = r.content.decode()
    pattern = re.compile('"live_status":(.*?),"hidden_till"')
    result = re.search(pattern, page)
    flag = result.group(1)
    return flag

def liveRec(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    r = requests.get(url=url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    page = r.content.decode()
    pattern = re.compile('<title id="link-app-title">(.*?) - 哔哩哔哩直播，二次元弹幕直播平台</title>')
    result = re.search(pattern, page)
    filename = result.group(1)
    filename = filename + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.ts'
    subprocess.call(["streamlink", url, 'best', "-o", filename])

if __name__ == "__main__":
    url = sys.argv[1]
    #url = "https://live.bilibili.com/1022"
    while True:
        if isQkunlive(url) == "1":
            liveRec(url)


#subprocess.call(["streamlink", self.url, 'best', "--hls-segment-timeout", "1", "-o", filename,])
#streamlink https://live.bilibili.com/13946381 best -l debug -o test_bilibili.ts