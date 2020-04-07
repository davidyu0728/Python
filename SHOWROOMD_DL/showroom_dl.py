#%%
import datetime
import time
import urllib
from urllib import request
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = "https://www.showroom-live.com/tps_1016000"
path = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(path,options=options)
driver.get(url)
element = driver.find_element_by_xpath('//*[@id="choose-stream-variant-dialog"]/div/div/div/div/ul/li')



driver.close()
# %%