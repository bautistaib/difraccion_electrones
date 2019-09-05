# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


################ Fuente para espectros AES: https://www.cnyn.unam.mx/~wencel/XPS/MANAES2.pdf

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

def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]

for root2, dirs2, files2 in os.walk("C:/Users/Bautista/Desktop/difraccion electrones/espectros"):
    for file in files2:
             csvs.append(file)
print(csvs)

for file in csvs:
    if file=='22_08IvsVRVr=14_8v(200-600).txt':         #en este se detectó carbono en el pico de la derivada (274ev), ¿oxigeno(524ev)? y titanio (423ev y 390ev).
    #if file=='26_08IvsVRVr=2.5v(200-550)(950eV).txt':
        datas = csv.reader(file)
        print(datas)
        x=[]
        y=[]
        str=r'C:/Users/Bautista/Desktop/difraccion electrones/espectros/'+file
        with open(str) as csvfile: #esto abre cada archivo dentro de la carpeta y lo llama csvfile
            plots = csv.reader(csvfile, delimiter='\t') #esto separa las columnas por los tabs
            for row in plots:
                    x.append(float(row[0])) 
                    y.append(float(row[1])) 

            x2=np.array(x) #esto son las columnas
            y2=np.array(y) 
            plt.plot(x2,y2)
            y2=signal.savgol_filter(y2, 
                                    41, # window size used for filtering 
                                    3)
            dydx=np.diff(y2)/np.diff(x2)        #deriva
            plt.plot(x2,y2)
            picos=find_peaks(y2, prominence=0.003)[0]           #prominence: parametro turbio que tiene que ver con que tan alto es un pico respecto a los otros picos o algo asi, muy bueno para filtrar
            print('Sin corregir energia:',x2[picos],'\n', 'Corrigiendo energia', x2[picos])
            plt.plot(x2[picos], y2[picos], "x")
            plt.show()
            x2=x2[:-1]                          #ajusta el tamaño para que tenga el mismo que la derivada
            plt.plot(x2,dydx)
            plt.xlabel('x')
            #plt.xlim(350,450)
            #plt.ylim(0.4,0.55)
            plt.ylabel('Intensidad')
            plt.title('Espectro')
            picosD=find_peaks(-dydx, prominence=0.0003)[0]
            print('Sin corregir energia:',x2[picosD],'\n', 'Corrigiendo energia', x2[picosD])
            plt.plot(x2[picosD], dydx[picosD], "x")
            print(file)
            if file=='22_08IvsVRVr=14_8v(200-600).txt':
                print('Normalizo maximos respecto al primer pico del titanio\n','Carbono:', dydx[picosD[0]]/dydx[picosD[1]],'\n¿Oxigeno?:', dydx[picosD[4]]/dydx[picosD[1]], '\nSegundo pico del Ti:',dydx[picosD[2]]/dydx[picosD[1]])
            plt.show()

        
