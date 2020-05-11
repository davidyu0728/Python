import datetime
import time
import urllib
from urllib import request
import re
import os
import streamlink
import subprocess
from multiprocessing import Pool
from multiprocessing import Process, Queue

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
                print(name + "record not start")
if __name__ == '__main__':
    aina_url ="https://www.showroom-live.com/digital_idol_15"
    mizuha_url = "https://www.showroom-live.com/digital_idol_21"
    kawaseuta_url = "https://www.showroom-live.com/kawaseuta"
    moe_url = "https://www.showroom-live.com/digital_idol_20"
    reina_url = "https://www.showroom-live.com/digital_idol_9"
    ruri_url = "https://www.showroom-live.com/digital_idol_4"
    kanae_url = "https://www.showroom-live.com/digital_idol_18"
    urara_url = "https://www.showroom-live.com/digital_idol_19"
    nagomi_url ="https://www.showroom-live.com/digital_idol_22"
    sally_url = "https://www.showroom-live.com/digital_idol_11"
    chiharu_url = "https://www.showroom-live.com/digital_idol_2"

    aina = ShowroomDownload(aina_url)
    mizuha = ShowroomDownload(mizuha_url)
    kawaseuta = ShowroomDownload(kawaseuta_url)
    moe = ShowroomDownload(moe_url)
    reina = ShowroomDownload(reina_url)
    ruri = ShowroomDownload(ruri_url)
    kanae = ShowroomDownload(kanae_url)
    urara = ShowroomDownload(urara_url)
    sally = ShowroomDownload(sally_url)
    chiharu = ShowroomDownload(chiharu_url)
    nagomi = ShowroomDownload(nagomi_url)

    p1 = Process(target=aina.livedownload)
    p2 = Process(target=mizuha.livedownload)
    p3 = Process(target=kawaseuta.livedownload)
    p4 = Process(target=moe.livedownload)
    p5 = Process(target=reina.livedownload)
    p6 = Process(target=ruri.livedownload)
    p7 = Process(target=kanae.livedownload)
    p8 = Process(target=urara.livedownload)
    p9 = Process(target=sally.livedownload)
    p10 = Process(target=chiharu.livedownload)
    p11 = Process(target=nagomi.livedownload)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()