#%%
import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import matplotlib.pyplot as plt
import os
url='https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
strhtml = requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
list_data = []
infi_sum = 0
for i in range(1,14):
    Bundesland_Name = '#main > div.text > table:nth-child(4) > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1)'
    AZ =              '#main > div.text > table:nth-child(4) > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(2)'
    pattern = re.compile(r'(<td colspan="1" rowspan="1">)(.*?)(</td>)')
    Bundesland_Name = pattern.match(str(soup.select(Bundesland_Name)[0])).group(2)
    AZ = pattern.match(str(soup.select(AZ)[0])).group(2)
    list_data.append([Bundesland_Name,AZ])
pattern = re.compile(r'(<strong>)(.*?)(</strong>)')
GS_AZ = str(soup.select('#main > div.text > table:nth-child(4) > tbody > tr:nth-child(16) > td:nth-child(2) > strong')[0])
GS_AZ =  pattern.match(GS_AZ).group(2)
list_data.append(["Gesamt",GS_AZ])
date = time.strftime("%Y-%m-%d", time.localtime())
label = ['Bundesland','Anzahl']
df_data = pd.DataFrame(columns=label,data=list_data)
save_file_name = 'E:\\RKI\\' + date + '.csv'
df_data.to_csv(save_file_name,index=None,encoding='iso-8859-1')
#main > div.text > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(1)
#main > div.text > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(1)
#main > div.text > table:nth-child(4) > tbody > tr:nth-child(16) > td:nth-child(2) > strong
# %%
