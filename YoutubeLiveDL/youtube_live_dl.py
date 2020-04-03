from __future__ import unicode_literals
import youtube_dl
import os
import sys
import time
import datetime
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
ts = time.gmtime()
re_time = time.strftime("%Y-%m-%d-%H-%M-%S", ts)
print(re_time)

ydl_opts = {
    'format': 'best',
    'outtmpl': re_time +'_'+'%(uploader)s-%(re_time)s-%(title)s.%(ext)s',
    #'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def video_download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=1XDT-APgkfc'])
    #print(result)


video_download()



