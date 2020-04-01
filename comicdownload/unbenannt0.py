# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:51:03 2019

@author: david
"""

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.manhuagui.com/comic/23270/290296.html"
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
driver.get(url)
page_text = driver.page_source
print(page_text)