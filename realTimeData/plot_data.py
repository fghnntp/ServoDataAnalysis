import numpy as np
import matplotlib.pyplot as plt

def plot_data_chan(row, col, data_chan_num, data_chans, plot_setting, locate):
    if row == 1 and col == 1:
        fig, axs = plt.subplots()
    else:
        fig, axs = plt.subplots(row, col)
    x = eval(plot_setting[numbers])
    sampletime = eval(plot_setting[sampletime])
    x = [sampletime*i for i in x]
    for i in range(row):
        for j in range(col):
            for _ in locate[::2]:
                if _[0]==i and _[1]==j:
                    #axs[i][j].plot(x, data_chans[])
                    pass

    