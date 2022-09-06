# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:41:59 2022

@author: Nusrat
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2021():
    temp_i=0
    average=[]
    for rows in pd.read_csv('C:/Users/Nusrat/Desktop/CPCB_Stations/2021_PM2.5.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['Alipur_Delhi, AnandVihar_Delhi, AshokVihar_Delhi, AyaNagar_Delhi, Bawana_Delhi, BurariCrossing_Delhi, ChandniChowk_Delhi, CRRIMathuraRoad_Delhi, Dwarka_Sector_8_Delhi, IGIAirport_T3_Delhi, IHBAS_Dilshad_Garden_Delhi, Jahangirpuri_Delhi, JLNStadium_Delhi, LodhiRoad_IITM_Delhi, LodhiRoad_IMD_Delhi, MandirMarg_Delhi, MDCN_Stadium_Delhi'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

if __name__=="__main__":
    lst2021=avg_data_2021()
    plt.plot(range(0,365),lst2021,lable="2021 date")
    plt.show()