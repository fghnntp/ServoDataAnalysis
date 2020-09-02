import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['MicroSoft YaHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def get_data(filename, list_ch1, list_ch2, list_ch3):
    with open(filename1, 'r') as f:
        for line in f.readlines():
            _ = line[:-1].split(',')
            if _[0][:-5] == 'DataTrace1-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    list_ch1.append(e_c)
            elif _[0][:-5] == 'DataTrace2-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    list_ch2.append(e_c)
            elif _[0][:-5] == 'DataTrace3-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    list_ch3.append(e_c)

def plot_f_av_aav(filename1, filename2):
    pass

"""
    维宏, WHDataTrace1, 指令速度
    维宏, WHDataTrace2, 反馈速度
    维宏, WHDataTrace3, 转矩指令
    LYNUC, LDataTrace1, 指令速度
    LYNUC, LDataTrace2, 反馈速度
    LYNUC, LDataTrace3, 转矩速度
"""
WHdata_trace_1 = []
WHdata_trace_2 = []
WHdata_trace_3 = []
filename1 = '麦迪克加工问题调查\采样数据-LYNUC\L-1ms-斜边X2-V1.std'

with open(filename1, 'r') as f:
    for line in f.readlines():
        _ = line[:-1].split(',')
        if _[0][:-5] == 'DataTrace1-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                WHdata_trace_1.append(e_c)
        elif _[0][:-5] == 'DataTrace2-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                WHdata_trace_2.append(e_c)
        elif _[0][:-5] == 'DataTrace3-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                WHdata_trace_3.append(e_c)
WHx1 = [0.001*i for i in range(len(WHdata_trace_1))]
WHx2 = [0.001*i for i in range(len(WHdata_trace_2))]
WHx3 = [0.001*i for i in range(len(WHdata_trace_3))]

Ldata_trace_1 = []
Ldata_trace_2 = []
Ldata_trace_3 = []
filename2 = '麦迪克加工问题调查\采样数据-维宏\W-1ms-斜边X-V1.std'
with open(filename2, 'r') as f:
    for line in f.readlines():
        _ = line[:-1].split(',')
        if _[0][:-5] == 'DataTrace1-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                Ldata_trace_1.append(e_c)
        elif _[0][:-5] == 'DataTrace2-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                Ldata_trace_2.append(e_c)
        elif _[0][:-5] == 'DataTrace3-TraceData':
            for e in _[1:]:
                e_c = eval(e)
                Ldata_trace_3.append(e_c)
Lx1 = [0.001*i for i in range(len(Ldata_trace_1))]
Lx2 = [0.001*i for i in range(len(Ldata_trace_2))]
Lx3 = [0.001*i for i in range(len(Ldata_trace_3))]


fig, axs = plt.subplots(2, 3, figsize=(9, 3))
axs[0][0].plot(WHx1, WHdata_trace_1, label='cmdV',color='red')
axs[0][1].plot(WHx2, WHdata_trace_2, label='V')
axs[0][2].plot(WHx3, WHdata_trace_3, label='F')
axs[1][0].plot(Lx1, Ldata_trace_1, label='cmdV')
axs[1][1].plot(Lx2, Ldata_trace_2, label='V')
axs[1][2].plot(Lx3, Ldata_trace_3, label='cmdV')
axs[0][0].legend()
axs[0][1].legend()
axs[0][2].legend()
axs[1][0].legend()
axs[1][1].legend()
axs[1][2].legend()

plt.show()