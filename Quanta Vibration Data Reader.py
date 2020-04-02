from os import getenv, path
from sqlalchemy import create_engine
from multiprocessing import cpu_count, Pool
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import os
import datetime
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

quanta_data_path = filedialog.askopenfilename()
#quanta_data_path = r"C:\Users\jrosenburg\Desktop\Mom's Spaghetti\Learning\Python Studying\Sample Quanta Data\Durability Runs 5-8\06 Dura 15  30min.xlsx"


which_input = input('Which input would you like to view? Type a number or "control"')
which_input = which_input.lower().strip()
minute = input('What minute would you like to view the data from?')
if which_input == "control":
    input_and_minute = minute + which_input
else:
    input_and_minute = minute + "input" + which_input

df = pd.read_excel(quanta_data_path, sheet_name=0, header=0, index_col=0)
df = df.drop(df.index[[0, 1]])
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('_ewaterfall_','').str.replace('z=','').str.replace('f','')

column_to_plot = df[input_and_minute]
y_scale_max = column_to_plot.max() + 1
peak_resonance_frequency = pd.to_numeric(column_to_plot).idxmax()

column_to_plot.plot()
plt.yscale('log')
plt.xscale('log')
plt.axis([1, 1125, .00001, y_scale_max])
plt.xlabel('Frequency      Peak Resonance @ ' + str(peak_resonance_frequency) + " Hz")
plt.ylabel('G^2/Hz')
plt.tight_layout()
plt.title("PSD")
plt.show()