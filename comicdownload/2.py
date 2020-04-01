# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:50:09 2019

@author: david
"""
import urllib
from urllib import request
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
start = time.time()
# %%
class comic_page_download():
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
            #<meta property="og:novel:book_name" content="Dr.STONE 石纪元">
            pattern = re.compile('<meta property="og:novel:book_name" content="(.*?)">')
            book_name = re.search(pattern, content).group(1).replace(" ","")
            
            return content, book_name
        except Exception as e:
            print(e)
            return None

    def get_page_url(self, content):
        #<a href="/comic/421/437105.html" title="132话" target="_blank">
        pattern = re.compile('<a href="(.*?)" title="(.*?)" target="_blank">')
        result = re.findall(pattern, content)
        list_url = []
        for item in result:
            html = item[0]
            name = item[1]
            pattern = re.compile('\d+')
            name_num = re.search(pattern,name)
            name_num = name_num.group(0)
            list_url.append([html,name,name_num])
        list_url = sorted(list_url,key=lambda x:x[2])
        return list_url

class use_webdriver():
    def __init__(self,path,driver,options):

        self.path = path
        self.driver = driver
        self.options = options
        
    def launch(self):
        driver = self.driver(options=self.options)
        return driver
    
class comic_download():
    def __init__(self, url):
        self.url = url

    def get_max_page_num(self, url):
        path = "chromedriver.exe"
        driver = webdriver.Chrome
        options = Options()
        options.add_argument('--headless')
        webbrowser = use_webdriver(path,driver,options)
        webbrowser = webbrowser.launch()
        webbrowser.get(url)
        try:
            WebDriverWait(webbrowser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "img_info"))
            )
        finally:
            page = webbrowser.page_source
            webbrowser.quit()
        pattern = re.compile('<option value="\d+">')
        page_num = re.findall(pattern, page)
        page_max = re.findall(re.compile('\d+'), page_num[-1])
        page_max = int(page_max[0])
        return page_max
    
    def download_image(self, page_num, img_path):
        path = "chromedriver.exe"
        driver = webdriver.Chrome
        options = Options()
        options.add_argument('--headless')
        webbrowser = use_webdriver(path,driver,options)
        webbrowser = webbrowser.launch()     
        for num in range(page_num):
            page_url = self.url + "?p=" + str(num + 1)
            webbrowser.get(page_url)
            try:
                WebDriverWait(webbrowser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "img_info"))
                )
            finally:
                page = webbrowser.page_source
            pattern = re.compile('<div id="images"><img src="(.*?)" (.*?)')
            img_url = re.search(pattern,page)
            img_url = img_url.group(1)
            img_name = img_path + "\\" + str(num+1) + ".jpg"
            urllib.request.urlretrieve(img_url,filename=img_name)
            

mainpage_url = "https://www.manhuafen.com/comic/421/"
comic_mainpage = comic_page_download(mainpage_url)
content = comic_mainpage.get_content(comic_mainpage.url)[0]
book_name = comic_mainpage.get_content(comic_mainpage.url)[1]
html_list = comic_mainpage.get_page_url(content)

comic_eachpage_url = mainpage_url.split("/comic")[0] + html_list[0][0]
hua_name = html_list[0][2]
path = os.getcwd() + "\\" + book_name + "\\" + hua_name
if not os.path.exists(path):
        print("not exists")
        os.makedirs(path)
else:
    print("exists")
    os.chmod(path,777)

comic_eachpage = comic_download(comic_eachpage_url)
max_page = comic_eachpage.get_max_page_num(comic_eachpage.url)
comic_eachpage.download_image(max_page, path)
end = time.time()
print("runtime:" + str(end-start))
#"""
#<div id="images"><img src="https://search.pstatic.net/common?
#src=http://img001.eshanyao.com/images/comic/20/39958/155224405963939958054079fe1.jpg"
# data-index="1" style="display: inline;"><p class="img_info">(1/48)</p></div>
#"""
#pattern = re.compile('<div id="images"><img src="(.*?)" (.*?)')
#img_url = re.search(pattern,page)
#img_url = img_url.group(1)
#urllib.request.urlretrieve(img_url,filename="01.jpg")
#print(img_url)
#
#"""
#
#comic_eachpage_content = comic_eachpage.get_content(comic_eachpage.url)
#print(comic_eachpage_content)
##pattern = re.compile('<img alt="(.*?)" id="(.*?)" scr="(.*?)"(.*?)>')
##result = re.search(pattern, comic_eachpage_content)
##print(result.group(0))
#"""
