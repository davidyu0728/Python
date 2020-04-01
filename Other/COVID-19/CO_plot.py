#%%
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
path = 'E:\\CO_DE\\'
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
        data = pd.read_csv(path + filename,encoding='iso-8859-1')
        if 'Baden-Württemberg' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Baden-Württemberg']
            BW.append(tmp['infizierte'].tolist()[0])
        else:
            BW.append(0)

        if 'Bayern' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Bayern']
            BY.append(tmp['infizierte'].tolist()[0])
        else:
            BY.append(0)

        if 'Berlin' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Berlin']
            BE.append(tmp['infizierte'].tolist()[0])
        else:
            BE.append(0)

        if 'Brandenburg' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Brandenburg']
            BB.append(tmp['infizierte'].tolist()[0])
        else:
            BB.append(0)

        if 'Bremen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Bremen']
            HB.append(tmp['infizierte'].tolist()[0])
        else:
            HB.append(0)        
    
        if 'Hamburg' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Hamburg']
            HH.append(tmp['infizierte'].tolist()[0])
        else:
            HH.append(0)       

        if 'Hessen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Hessen']
            HE.append(tmp['infizierte'].tolist()[0])
        else:
            HE.append(0)       

        if 'Mecklenburg-Vorpommern' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Mecklenburg-Vorpommern']
            MV.append(tmp['infizierte'].tolist()[0])
        else:
            MV.append(0)        

        if 'Niedersachsen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Niedersachsen']
            NI.append(tmp['infizierte'].tolist()[0])
        else:
            NI.append(0) 

        if 'Nordrhein-Westfalen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Nordrhein-Westfalen']
            NW.append(tmp['infizierte'].tolist()[0])
        else:
            NW.append(0) 

        if 'Rheinland-Pfalz' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Rheinland-Pfalz']
            RP.append(tmp['infizierte'].tolist()[0])
        else:
            RP.append(0)

        if 'Saarland' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Saarland']
            SL.append(tmp['infizierte'].tolist()[0])
        else:
            SL.append(0)

        if 'Sachsen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Sachsen']
            SN.append(tmp['infizierte'].tolist()[0])
        else:
            SN.append(0)

        if 'Sachsen-Anhalt' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Sachsen-Anhalt']
            ST.append(tmp['infizierte'].tolist()[0])
        else:
            ST.append(0)        

        if 'Schleswig-Holstein' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Schleswig-Holstein']
            SH.append(tmp['infizierte'].tolist()[0])
        else:
            SH.append(0) 

        if 'Thüringen' in data['Bundesland'].tolist():
            tmp = data[data['Bundesland']=='Thüringen']
            TH.append(tmp['infizierte'].tolist()[0])
        else:
            TH.append(0)
        tmp = data[data['Bundesland']=='Gesamt']
        DE.append(tmp['infizierte'].tolist()[0])
t = [i for i in range(len(BW))]
fig, ax = plt.subplots(1, 1)
#ax.plot(BW,BY,BE,BB,HB,HH,HE,MV,NI,NW,RP,SL,SN,ST,SH,TH)
ax.plot(t,BW,t,BY,t,BE,t,BB,t,HB,t,HH,t,HE,t,MV,t,NI,t,NW,t,RP,t,SL,t,SN,t,ST,t,SH,t,TH)
ax.grid(True)
plt.show()
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
plt.savefig(path + 'SARS-CoV-2_BW_DE_' + date + '.jpg',dpi=300)
plt.show()
# %%
