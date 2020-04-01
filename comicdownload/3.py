# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
from urllib import request
import time
start = time.time()
for i in range(10):
    filename = str(i+50) + ".jpg"
    img_url = "https://search.pstatic.net/common?src=http://img001.eshanyao.com/images/comic/20/39958/155224405963939958054079fe1.jpg"
    with urllib.request.urlopen(img_url, timeout=30) as response, open(filename
            , 'wb') as f_save:
        f_save.write(response.read())
        f_save.flush()
        f_save.close()
    urllib.request.urlretrieve(img_url,filename=filename)
end = time.time()
print("runtime:" + str(end-start))
#url = "https://www.manhuafen.com/comic/421/39958.html"
#"""
#driver = webdriver.PhantomJS('phantomjs.exe')
#driver.get(url)
#page_text = driver.page_source
#print(page_text)
#"""
#chrome_option = Options()
#chrome_option.add_argument('--headless')
#chrome_driver_path = "chromedriver.exe"
#webbrowser = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_option)
## class="img_info"
#webbrowser.get(url)
#try:
#    element = WebDriverWait(webbrowser, 10).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "img_info"))
#    )
#finally:
#    page = webbrowser.page_source
#    webbrowser.quit()
#
#
## 显式等待
#"""
## class="img_info"
#webbrowser.get(url)
#try:
#    element = WebDriverWait(webbrowser, 1).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "img_info"))
#    )
#finally:
#    page = webbrowser.page_source
#    webbrowser.quit()
#if page:
#    print("OK")
## 若无，则:TimeoutException
##print(page)
##sleep(2)
#"""
## 隐式等待
#"""
#webbrowser.implicitly_wait(10) # seconds
#webbrowser.get(url)
#myDynamicElement = webbrowser.find_element_by_class_name("img_info")
#page = webbrowser.page_source
#webbrowser.quit()
#"""
#
#    
#"""
#<div id="images"><img src="https://search.pstatic.net/common?src=http://img001.eshanyao.com/images/comic/20/39958/155224405963939958054079fe1.jpg" data-index="1" style="display: inline;"><p class="img_info">(1/48)</p></div>
#        <a class="img_land_prev" onclick="SinTheme.prevPage()"></a>
#        <a class="img_land_next" onclick="SinTheme.nextPage()"></a>
#            </div>
#            
#            
#<div id="images"></div>
#<a class="img_land_prev" onclick="SinTheme.prevPage()"></a>
#<a class="img_land_next" onclick="SinTheme.nextPage()"></a>
#    </div>
#"""