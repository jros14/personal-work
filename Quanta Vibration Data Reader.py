from os import getenv, path
from sqlalchemy import create_engine
from multiprocessing import cpu_count, Pool
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import os
import datetime

minute = "12" #input("What minute would you like to view the data from?")
quanta_data_path = r"C:\Users\jrosenburg\Desktop\Mom's Spaghetti\Learning\Python Studying\Sample Quanta Data\Durability Runs 5-8\06 Dura 15  30min.xlsx"
quanta_df = pd.read_excel(quanta_data_path, sheet_name=0, index_col=0)
#quanta_df = quanta_df.transpose()
quanta_data_list = quanta_df.columns.values.tolist()
"""quanta_series = pd.Series(quanta_data_list)
print(quanta_series)
print(str(type(quanta_data_list[0])))"""
print("Start *******************************")
index = quanta_df.index
column = quanta_df.columns.values
for column_text in quanta_data_list:
    number_to_check = column_text[2:5]
    if(number_to_check[2] == ')'):
        number_to_check[2] = ' '
#    print(column_text[2:5])
    if number_to_check.strip() == str(minute):
        print("It's minute " + str(minute) + "!!")
        break
x_axis = index
y_column = "Z=" + minute + " (EWaterfall_control(f))"
print(y_column)
"""y_axis = quanta_df.loc[y_column]
plt.plot(x_axis, y_axis)
plt.xlabel('Frequency')
plt.ylabel('G^2/Hz')
plt.title("PSD")
plt.show() """