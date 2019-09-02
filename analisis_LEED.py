# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:32:13 2019

@author: Bautista
"""

import scipy as sp
import matplotlib.pyplot as plt
import csv
import numpy as np
import math
from scipy import signal
from scipy.signal import find_peaks
csvs=[]
xxx=[]
yyy=[]
import os

def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]

#def find_nearest(array, value):
#    array = np.asarray(array)
#    idx = (np.abs(array - value)).argmin()
#    return array[idx]

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
xxx_processed = 1./np.sqrt(xxx)
xxxx=np.array(xxx_processed)
#yyyy=np.array(yyy)
primer_orden=np.zeros(len(xxx))
for i in range(len(yyy)):
    primer_orden[i]=find_nearest(yyy[i],1.23*xxxx[i]+0.068 )
    print(yyy[i], xxxx[i], 1.23*xxxx[i]+0.068, primer_orden[i] )
    
#pendiente 0.107
#origen 0.32
#for i in range(len(yyy)):
#    if(len(yyy)-1-i<4 or len(yyy)-1-i==19):
#        #print(yyy[i])
#        primer_orden.append(yyy[i][-1])
#    else:
#        if(i!=0):
#            #print(yyy[i])
#            primer_orden.append(yyy[i][-2])
#        else:
#            print(yyy[i])
#            primer_orden.append(yyy[i][-3])
#primer_orden.reverse()
    
yyyy=np.array(primer_orden)
plt.clf()
#for xe, ye in zip(xxxx, yyyy):
#    plt.scatter([xe] * len(ye), ye)
plt.scatter(xxxx,yyyy)
f=open('primer orden.dat', 'w')
for i in range(len(xxxx)):
    f.write("%f\t%f\n" %(xxxx[i], yyyy[i]))
#plt.plot(xxxx,yyyy, label='Loaded from file!', style='x')
plt.xlabel('Energia')
plt.ylabel('y')
plt.title('Interesting Graph/nCheck it out')
plt.legend()
plt.savefig('picos.jpeg')
plt.show()
f.close()
