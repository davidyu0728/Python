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
                #time.sleep(10)
                #pass
                print(name + "record not start")
if __name__ == '__main__':
    start = time.clock()

    aina_url ="https://www.showroom-live.com/miyu_miyu_miyu"
    mizuha_url = "https://www.showroom-live.com/rumi_afilia"
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

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    end = time.clock()
    print(end-start)

    """
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
    pool = Pool(processes = 6)
    pool.apply(aina.livedownload)
    pool.apply(mizuha.livedownload)
    pool.apply(kawaseuta.livedownload)
    pool.apply(moe.livedownload)
    pool.apply(reina.livedownload)
    pool.apply(ruri.livedownload)
    pool.apply(kanae.livedownload)
    pool.apply(urara.livedownload)
    pool.apply(sally.livedownload)
    pool.apply(chiharu.livedownload)
    pool.apply(nagomi.livedownload)
    pool = Pool(processes = 6)
    pool.apply_async(aina.islivestart)
    pool.apply_async(mizuha.islivestart)
    pool.apply_async(kawaseuta.islivestart)
    pool.apply_async(moe.islivestart)
    pool.apply_async(reina.islivestart)
    pool.apply_async(ruri.islivestart)
    pool.apply_async(kanae.islivestart)
    pool.apply_async(urara.islivestart)
    pool.apply_async(sally.islivestart)
    pool.apply_async(chiharu.islivestart)
    pool.apply_async(nagomi.islivestart)
    pool = Pool(processes = 6)
    pool.apply_async(aina.livedownload)
    pool.apply_async(mizuha.livedownload)
    pool.apply_async(kawaseuta.livedownload)
    pool.apply_async(moe.livedownload)
    pool.apply_async(reina.livedownload)
    pool.apply_async(ruri.livedownload)
    pool.apply_async(kanae.livedownload)
    pool.apply_async(urara.livedownload)
    pool.apply_async(sally.livedownload)
    pool.apply_async(chiharu.livedownload)
    pool.apply_async(nagomi.livedownload)
    """
