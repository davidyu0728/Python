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
re_time = time.localtime()
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(uploader)s\%(autonumber)s-%(title)s.%(ext)s',
    #'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def video_download():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=5aQYWTgxEoI'])
    #print(result)

def restart():
    try:
        video_download()
    except Exception as e:
        print(e)
    finally:
        print('waiting for restart')
        time.sleep(5)
        restart()

restart()

