#%%
import datetime
import time
import urllib
from urllib import request
import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from phantomjs import Phantom

"""
driver = webdriver.PhantomJS()
driver.get(url) # url associated with button click
page = driver.page_source
f = open('output.txt', 'a')
f.write(page)
f.close()
driver.quit()
"""
def get_page(url):
    path = "chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(path,options=options)
    driver.get(url)
    page = driver.page_source
    driver.quit()
    return page
def get_m3u8(page):
    page = get_m3u8(url)
    pattern = re.compile('<ul class="stream-variant-list"><li data-url="(.*?)">stable stream</li></ul>')
    result = re.search(pattern, page)
    m3u8_url = result.group(1)
    if "m3u8" in m3u8_url:
        print(m3u8_url)
        return m3u8_url
# %%
def restart():
    try:
        get_m3u8(get_page(url))
    except Exception as e:
        print(e)
        print("Live Stream not start")

url = "https://www.showroom-live.com/digital_idol_15"
cnt = 0
while True:
    cnt = cnt + 1
    if cnt == 20:
        print("time out")
        sys.exit(0)
    else:
        print(cnt)
        restart()
"""
page = get_m3u8(url)
pattern = re.compile('<ul class="stream-variant-list"><li data-url="(.*?)">stable stream</li></ul>')
result = re.search(pattern, page)
cnt = 0
try:
    m3u8_url = result.group(1)
    if "m3u8" in m3u8_url:
        print(m3u8_url)
    else:
        flag_stream_on = False
        print("Live Stream not start")
        cnt = cnt + 1
        if cnt == 20:
            sys.exit(0)
except Exception as e:
    print(e)
    page = get_m3u8(url)
    pattern = re.compile('<ul class="stream-variant-list"><li data-url="(.*?)">stable stream</li></ul>')
    result = re.search(pattern, page)
"""
    