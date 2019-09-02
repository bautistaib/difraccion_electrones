# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:32:13 2019

@author: Bautista
"""

import scipy as sp
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal
from scipy.signal import find_peaks
csvs=[]
xxx=[]
yyy=[]
import os
for root2, dirs2, files2 in os.walk("C:/Users/Bautista/Downloads/Fotos camara oscar 4.5 a 50.5 en jpg/text"):
    for file in files2:
        if file.endswith(".csv"):
             #print(os.path.join(root2, file))
             csvs.append(file)
print(csvs)
#data= open(r"C:/Users/usuario/Desktop/Difraccion de electrones/Fotos camara oscar 4.5 a 50.5 en jpg/perfil5.csv")
#datas = csv.reader(data)
for file in csvs:
    datas = csv.reader(file)
    print(datas)
    x=[]
    y=[]
    str=r'C:/Users/Bautista/Downloads/Fotos camara oscar 4.5 a 50.5 en jpg/text/'+file
    with open(str) as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if(row[0]!='X'):
                x.append(float(row[0]))
                y.append(float(row[1]))
        plt.plot(x,y, label='Loaded from file!')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interesting Graph/nCheck it out')
        plt.legend()
        plt.show()
        xx=np.array(x)
        yy=np.array(y)
        yy=signal.savgol_filter(yy, 
                                101, # window size used for filtering 
                                3)
        plt.plot(xx,yy, label='Loaded from file!')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interesting Graph/nCheck it out')
        plt.legend()
        
        picos=find_peaks(yy, width=50, height=10)[0]
        #print(np.where(picos > 1300))
        #if(picos[np.where(picos >1300)[0]]<1500):
        #    np.delete(np.where)
        #np.delete(picos, np.where(picos<1500 and picos > 1300)[0])
        #for element in picos:
        #    if(element<1500 and element>1300):
        #        np.delete(picos,np.where(element))
        print(picos)
        plt.plot(picos, yy[picos], "x")
        picos_processed = np.sin((101.*picos/2850. - 50.5)*2.*np.pi/360.)
        
        #for i in range(len(picos)):
        #    picos_processed.append(np.sin((101.*picos[i]/2850.-50.5)*2.*np.pi/360.))
        temp=file.split('l')
        for s in temp:
            tmp2=s.split('.')[0]
            if(tmp2.isdigit()):
                xxx.append(float(tmp2)+2.5)
                yyy.append(list(picos_processed))
        xxx_processed = np.sqrt(xxx)
xxxx=np.array(xxx_processed)
yyyy=np.array(yyy)



plt.clf()
for xe, ye in zip(xxxx, yyyy):
    plt.scatter([xe] * len(ye), ye)
#plt.xlim(0,30)
#plt.plot(xxxx,yyyy[:0], label='Loaded from file!')
plt.xlabel('Energia')
plt.ylabel('y')
plt.title('Interesting Graph/nCheck it out')
plt.legend()
plt.show()