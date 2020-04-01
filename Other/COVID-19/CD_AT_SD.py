#%%
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import pandas as pd
import os
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL
import smtplib
import datetime
import re
date = time.strftime("%Y-%m-%d", time.localtime())
path = os.getcwd() + '\\RKI\\'
def RKI_Plot(path):
    file_list = os.listdir(path)
    BW = [] # Baden-Württemberg
    BY = [] # Bayern
    BE = [] # Berlin
    BB = [] # Brandenburg
    HB = [] # Bremen
    HH = [] # Hamburg
    HE = [] # Hessen
    MV = [] # Mecklenburg-Vorpommern
    NI = [] # Niedersachsen
    NW = [] # Nordrhein-Westfalen	
    RP = [] # Rheinland-Pfalz	
    SL = [] # Saarland	
    SN = [] # Sachsen	
    ST = [] # Sachsen-Anhalt	
    SH = [] # Schleswig-Holstein	
    TH = [] # Thüringen	
    DE = []
    for filename in file_list:
        if filename.split('.')[1] == 'csv':
            data = pd.read_csv(path + filename,encoding='iso-8859-1',thousands='.')
            if 'Baden-Württemberg' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Baden-Württemberg']
                BW.append(tmp['Fälle'].tolist()[0])
            else:
                BW.append(0)

            if 'Bayern' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Bayern']
                BY.append(tmp['Fälle'].tolist()[0])
            else:
                BY.append(0)

            if 'Berlin' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Berlin']
                BE.append(tmp['Fälle'].tolist()[0])
            else:
                BE.append(0)

            if 'Brandenburg' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Brandenburg']
                BB.append(tmp['Fälle'].tolist()[0])
            else:
                BB.append(0)

            if 'Bremen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Bremen']
                HB.append(tmp['Fälle'].tolist()[0])
            else:
                HB.append(0)        
        
            if 'Hamburg' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Hamburg']
                HH.append(tmp['Fälle'].tolist()[0])
            else:
                HH.append(0)       

            if 'Hessen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Hessen']
                HE.append(tmp['Fälle'].tolist()[0])
            else:
                HE.append(0)       

            if 'Mecklenburg-Vorpommern' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Mecklenburg-Vorpommern']
                MV.append(tmp['Fälle'].tolist()[0])
            else:
                MV.append(0)        

            if 'Niedersachsen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Niedersachsen']
                NI.append(tmp['Fälle'].tolist()[0])
            else:
                NI.append(0) 

            if 'Nordrhein-Westfalen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Nordrhein-Westfalen']
                NW.append(tmp['Fälle'].tolist()[0])
            else:
                NW.append(0) 

            if 'Rheinland-Pfalz' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Rheinland-Pfalz']
                RP.append(tmp['Fälle'].tolist()[0])
            else:
                RP.append(0)

            if 'Saarland' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Saarland']
                SL.append(tmp['Fälle'].tolist()[0])
            else:
                SL.append(0)

            if 'Sachsen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Sachsen']
                SN.append(tmp['Fälle'].tolist()[0])
            else:
                SN.append(0)

            if 'Sachsen-Anhalt' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Sachsen-Anhalt']
                ST.append(tmp['Fälle'].tolist()[0])
            else:
                ST.append(0)        

            if 'Schleswig-Holstein' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Schleswig-Holstein']
                SH.append(tmp['Fälle'].tolist()[0])
            else:
                SH.append(0) 

            if 'Thüringen' in data['Bundesland'].tolist():
                tmp = data[data['Bundesland']=='Thüringen']
                TH.append(tmp['Fälle'].tolist()[0])
            else:
                TH.append(0)
            tmp = data[data['Bundesland']=='Gesamt']
            
            DE.append(str(tmp['Fälle'].tolist()[0]))
    t = [i for i in range(len(BW))]
    print(BW)
    print(DE)
    fig, ax = plt.subplots(1, 1)
    #ax.plot(BW,BY,BE,BB,HB,HH,HE,MV,NI,NW,RP,SL,SN,ST,SH,TH)
    #ax.plot(t,BW,t,BY,t,BE,t,BB,t,HB,t,HH,t,HE,t,MV,t,NI,t,NW,t,RP,t,SL,t,SN,t,ST,t,SH,t,TH)
    #ax.grid(True)
    #plt.show()
    fig, ax = plt.subplots(2, 1,figsize=(10, 5),dpi=300)
    #ax.plot(BW,BY,BE,BB,HB,HH,HE,MV,NI,NW,RP,SL,SN,ST,SH,TH)
    ax[0].plot(BW)
    ax[0].grid(True)
    ax[0].set_xlabel('Baden-Württemberg')
    ax[0].set_ylabel('Anzahl')

    ax[1].plot(DE)
    ax[1].grid(True)
    ax[1].set_xlabel('Deutschland')
    ax[1].set_ylabel('Anzahl')
    fig.tight_layout()
    date = time.strftime("%Y-%m-%d", time.localtime())
    plt.savefig(path + 'SARS-CoV-2_BW_DE_' + date  + '.jpg',dpi=300)

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def mailcontent(date):
    path_tmp = path + date + '.csv'
    df = pd.read_csv(path_tmp,encoding='iso-8859-1')
    BW_num = df[df['Bundesland'] == 'Baden-Württemberg']['Fälle'].to_list()[0]
    DE_num = df[df['Bundesland'] == 'Gesamt']['Fälle'].to_list()[0]
    gersten = datetime.date.today()  -  datetime.timedelta(days=1) 
    path_tmp = path + str(gersten) + '.csv'
    df = pd.read_csv(path_tmp,encoding='iso-8859-1')
    BW_num_y = df[df['Bundesland'] == 'Baden-Württemberg']['Fälle'].to_list()[0]
    DE_num_y = df[df['Bundesland'] == 'Gesamt']['Fälle'].to_list()[0]
    content = date +'\n'+ '今日新增：BW:' + str(int(BW_num-BW_num_y)) + ' DE:' + str(int(DE_num-DE_num_y)) \
              +'\n'+ '确诊总数：BW:' + str(int(BW_num)) + ' DE:' + str(int(DE_num)) +'\n'+ '图表见附件'
    return content

def get_datenstand(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    html = requests.get(url,headers=headers).text
    res_tr = r'<strong>(.*?)</strong>'
    m_tr =  re.findall(res_tr,html)
    for text in m_tr:
        if 'Stand' in text:
            neu_datenstand = text
    neu_datenstand.replace('(','')
    neu_datenstand.replace(')','')
    #print(neu_datenstand)
    rf = open('alt_datenstand.txt', 'r')
    alt_datenstand = rf.read()
    rf.close()
    #print(alt_datenstand)
    if alt_datenstand != neu_datenstand:
        flag = True
        wf = open('alt_datenstand.txt', 'w')
        wf.write(neu_datenstand)
        wf.close()
    else:
        flag = False
    return flag



url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
#is_act_daten = get_datenstand(url)


res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
tables = soup.select('table')
df_list = []
for table in tables:
    df_list.append(pd.concat(pd.read_html(table.prettify())))
df = pd.concat(df_list)
df = df[['Bundesland','Fälle']]
index = df[df['Bundesland'] == 'Gesamt'].index.to_list()[0]
df = df.iloc[:index+1]

label = ['Bundesland','Fälle']
save_file_name = path + date + '.csv'
df.to_csv(save_file_name,index=None,encoding='iso-8859-1',thousands='.')
RKI_Plot(path)
'''
date = time.strftime("%Y-%m-%d", time.localtime())
host_server = 'smtp.qq.com'
sender_qq = '695756079'
pwd = 'iwvdydnrwokebfba'
sender_qq_mail = '695756079@qq.com'
receiver = 'david.yu0728@gmail.com' #'15955188488@139.com'
mail_content = mailcontent(date)

smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEMultipart('related')
msg['From'] = _format_addr('Bochao Yu <%s>' % sender_qq_mail)
msg['To'] = _format_addr(receiver)
header = date + ' 最新消息'
msg['Subject'] = Header(header, 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
path_jpg = path + 'SARS-CoV-2_BW_DE_' + date + '.jpg'
name = 'SARS-CoV-2_BW_DE_' + date + '.jpg'
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(path, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename=name)
    mime.add_header('Content-Disposition', 'attachment', filename=name)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
smtp.sendmail(sender_qq_mail, receiver, str(msg))
smtp.quit()
'''
# %%
