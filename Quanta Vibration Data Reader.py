from os import getenv, path
from sqlalchemy import create_engine
from multiprocessing import cpu_count, Pool
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import os
import datetime


def plot_data(quanta_df, column_name):
    y_values = quanta_df.loc[column_name]
    print("plotting....")
    plt.plot(y_values)
    plt.xlabel('Frequency')
    plt.ylabel('G^2/Hz')
    plt.title("PSD")
    plt.xscale("log")
    plt.show()


# def find_column():


input1 = input('Which input would you like to view? Type a number or "control"')
input1 = input1.lower()
minute = int(input('What minute would you like to view the data from?'))
quanta_data_path = r"C:\Users\jrosenburg\Desktop\Mom's Spaghetti\Learning\Python Studying\Sample Quanta Data\Durability Runs 5-8\06 Dura 15  30min.xlsx"
df = pd.read_excel(quanta_data_path, sheet_name=0, header=0, index_col=0)
df = df.drop(df.index[[0, 1]])
df.columns = df.columns.str.strip()
print("printing df....")
print(df)
if input1 != 'control':
    input1 = "Z=" + str(minute) + "(EWaterfall_input" + input1 + "(f))"
else:
    input1 = "Z=" + str(minute) + "(EWaterfall_control(f))"
print("Input1    :" + input1)
x = df.loc[input1]
print("printing x...")
print(x)
#plot_data(df, input1)





"""quanta_columns = quanta_data_original.columns.values.tolist()
for column_text in quanta_columns:
    number_to_check = column_text[2:5]
    if (number_to_check[2] == ')'):
        number_to_check[2] = ' '
    #    print(column_text[2:5])
    if number_to_check.strip() == str(minute):
        print("It's minute " + str(minute) + "!!")
        break"""

#


"""

print("Start *******************************")
for column_text in quanta_columns:
    number_to_check = column_text[2:5]
    if(number_to_check[2] == ')'):
        number_to_check[2] = ' '
#    print(column_text[2:5])
    if number_to_check.strip() == str(minute):
        print("It's minute " + str(minute) + "!!")
        break
y_column_name = "Z=" + minute + " (EWaterfall_control(f))"
y_column = quanta_df.filter(regex=y_column_name, axis=1)   <============**********
print(y_column_name)
print(y_column)"""

"""x_axis = quanta_df.index.values.tolist()
x_axis = x_axis[2:]
y_column = "Z=" + minute + " (EWaterfall_control(f))"
print("Y Column = " + y_column)
#print(str(type(x_axis)))
#print("X Axis = " + str(x_axis))
y_axis = quanta_df.loc[:, y_column]
print("Y Axis = " + y_axis)

plt.plot(x_axis, y_axis)
plt.xlabel('Frequency')
plt.ylabel('G^2/Hz')
plt.title("PSD")
plt.show()"""
