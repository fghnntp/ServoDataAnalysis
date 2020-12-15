import numpy as np
import matplotlib.pyplot as plt

def plot_data_chan(filename, row, col, data_chans, plot_setting, locate, plot_info):
    #获取合适的横轴长度
    x = min([len(data) for data in data_chans])
    sampletime = float(plot_setting['sampletime'])
    x = [sampletime*i for i in range(x)]
    count = 0
    #当全部绘制在一个位置时
    if row == 1 and col == 1:
        fig, axs = plt.subplots()
        for chn in plot_info:
            if chn != '':
                plt.plot(x, data_chans[int(chn[1])-1], label=chn)
        plt.legend()
        plt.title(filename)
        plt.show()
        return
    else:
        fig, axs = plt.subplots(row, col)
    
    for i in range(1, row+1):
        for j in range(1, col+1):
            for _ in locate:
                if _[0]==i and _[1]==j:
                    axs[i-1][j-1].plot(x, data_chans[int(plot_info[count][1])], label=data_chans[count])
                    count += 1
    
    for i in range(row):
        for j in range(col):
            axs[i][j].legend()
    plot.show()

    