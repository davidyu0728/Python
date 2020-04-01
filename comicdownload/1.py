import urllib
from urllib import request
import re
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# %%
class comic_page_download:
    def __init__(self, url):  # path):
        """
        if not os.path.exists(path):
            print("Exists File")
            exit(0)
        """
        self.url = url

        # self.path = path

    def get_content(self, url):
        try:
            req = request.Request(url)
            res = request.urlopen(req, timeout=50)
            content = res.read().decode("utf-8")
            return content
        except Exception as e:
            print(e)
            return None

    def get_page_url(self, content):
        # id="chapter-list-1"
        pattern = re.compile('\'chapter-list-1\'.*?>(.*?)</div>')
        result = re.search(pattern, content)
        result = result.group(1)
        # <a href="/comic/23270/391984.html" title="第74回" class="status0" target="_blank">
        pattern = re.compile('<a href="(.*?)" title="(.*?)" class="status0" target="_blank">')
        result = re.findall(pattern, result)
        list_url = []
        for item in result:
            html = item[0]
            name = item[1]
            name = name.replace("话", "回")
            if "第" in name:
                name = name.replace("第", "")
                name = name.replace("回", "")
                list_url.append([html, int(name)])
            list_url = sorted(list_url, key=lambda x:x[1])
        return list_url


mainpage_url = "https://www.manhuagui.com/comic/23270/"
comic_mainpage = comic_page_download(mainpage_url)
content = comic_mainpage.get_content(comic_mainpage.url)
html_list = comic_mainpage.get_page_url(content)

comic_eachpage_url = mainpage_url.split("/comic")[0] + html_list[0][0]
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_driver_path = "chromedriver.exe"
webbrowser = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_option)
# class="img_info"
webbrowser.get(comic_eachpage_url)
sleep(10)
page = webbrowser.page_source

print(page)

#pattern = re.compile('<img alt="(.*?)" id="(.*?)" scr="(.*?)"(.*?)>')
#result = re.search(pattern, comic_eachpage_content)
#print(result.group(0))

