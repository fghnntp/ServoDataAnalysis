import numpy as np
import matplotlib.pyplot as plt
import os
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['MicroSoft YaHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def get_data(filename, list_ch1, list_ch2, list_ch3):
    """
        input filename, and excrat CH1, CH2, CH3 data to list_ch1, list_ch2 and list_ch3

        CH1: 指令速度 CMDV
        CH2: 反馈速度 ACTV
        CH3: 转矩指令 CMDT
    """
    with open(filename, 'r') as f:
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

def plot_func(filename1, filename2, ratio):
    """
        input could be a tuple
        input two name, one is Lynuc, another is weihong
        and plot their data in one figure, which includes 
        2 × 3 's grid
        维宏, WHDataTrace1, 指令速度
        维宏, WHDataTrace2, 反馈速度
        维宏, WHDataTrace3, 转矩指令
        LYNUC, LDataTrace1, 指令速度
        LYNUC, LDataTrace2, 反馈速度
        LYNUC, LDataTrace3, 转矩速度
    """
    ratio_inter = ratio
    WHdata_trace_1 = []
    WHdata_trace_2 = []
    WHdata_trace_3 = []
    get_data(filename1, WHdata_trace_1, WHdata_trace_2, WHdata_trace_3)
    WHx1 = [ratio_inter*i for i in range(len(WHdata_trace_1))]
    WHx2 = [ratio_inter*i for i in range(len(WHdata_trace_2))]
    WHx3 = [ratio_inter*i for i in range(len(WHdata_trace_3))]
    Ldata_trace_1 = []
    Ldata_trace_2 = []
    Ldata_trace_3 = []
    get_data(filename2, Ldata_trace_1, Ldata_trace_2, Ldata_trace_3)    
    Lx1 = [ratio_inter*i for i in range(len(Ldata_trace_1))]
    Lx2 = [ratio_inter*i for i in range(len(Ldata_trace_2))]
    Lx3 = [ratio_inter*i for i in range(len(Ldata_trace_3))]
    WHdata_trace_2 = []
    for i in range(len(WHdata_trace_1)-1):
        _ = (WHdata_trace_1[i+1]-WHdata_trace_1[i])/ratio_inter
        WHdata_trace_2.append(_)
    WHx2 = [ratio_inter*i for i in range(len(WHdata_trace_2))]
    Ldata_trace_2 = []
    for i in range(len(Ldata_trace_1)-1):
        _ = (Ldata_trace_1[i+1]-Ldata_trace_1[i])/ratio_inter
        Ldata_trace_2.append(_)
    Lx2 = [ratio_inter*i for i in range(len(Ldata_trace_2))]
    
    left_edge1 = filename1.rfind('\\') + 1
    left_edge2 = filename2.rfind('\\') + 1
    right_edge1 = filename1.rfind('.')
    right_edge2 = filename2.rfind('.')
    print(filename1[left_edge1:right_edge1])
    print(filename2[left_edge2:right_edge2])
    print()

    fig, axs = plt.subplots(2, 3, figsize=(16, 9))
    #fig, axs = plt.subplots(2, 3)
    axs[0][0].plot(WHx1, WHdata_trace_1, label='CMDV', color='blue')
    axs[0][1].plot(WHx2, WHdata_trace_2, label='CMDA', color='green')
    axs[0][2].plot(WHx3, WHdata_trace_3, label='CMDT', color='red')
    axs[1][0].plot(Lx1, Ldata_trace_1, label='CMDV', color='blue')
    axs[1][1].plot(Lx2, Ldata_trace_2, label='CMDA', color='green')
    axs[1][2].plot(Lx3, Ldata_trace_3, label='CMDT', color='red')
    axs[0][0].set_title(filename1[left_edge1:right_edge1])
    axs[1][0].set_title(filename2[left_edge2:right_edge2])
    for i in range(2):
        for j in range(3):
            axs[i][j].legend()
    fig.canvas.manager.full_screen_toggle() # toggle fullscreen mode
    plt.show()
    #plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.png',dpi=365, format='png') 
    #plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.svg', format='svg') 

def plot_func_add_j(filename1, filename2, ratio):
    """
        plot CMDV, CMDA, CMDJ, CMDT
    """
    ratio_inter = ratio
    WHdata_trace_1 = []
    WHdata_trace_2 = []
    WHdata_trace_3 = []
    get_data(filename1, WHdata_trace_1, WHdata_trace_2, WHdata_trace_3)
    WHx1 = [ratio_inter*i for i in range(len(WHdata_trace_1))]
    WHx2 = [ratio_inter*i for i in range(len(WHdata_trace_2))]
    WHx3 = [ratio_inter*i for i in range(len(WHdata_trace_3))]
    Ldata_trace_1 = []
    Ldata_trace_2 = []
    Ldata_trace_3 = []
    get_data(filename2, Ldata_trace_1, Ldata_trace_2, Ldata_trace_3)    
    Lx1 = [ratio_inter*i for i in range(len(Ldata_trace_1))]
    Lx2 = [ratio_inter*i for i in range(len(Ldata_trace_2))]
    Lx3 = [ratio_inter*i for i in range(len(Ldata_trace_3))]
    WHdata_trace_2 = []
    for i in range(len(WHdata_trace_1)-1):
        _ = (WHdata_trace_1[i+1]-WHdata_trace_1[i])/ratio_inter
        WHdata_trace_2.append(_)
    WHx2 = [ratio_inter*i for i in range(len(WHdata_trace_2))]
    Ldata_trace_2 = []
    for i in range(len(Ldata_trace_1)-1):
        _ = (Ldata_trace_1[i+1]-Ldata_trace_1[i])/ratio_inter
        Ldata_trace_2.append(_)
    Lx2 = [ratio_inter*i for i in range(len(Ldata_trace_2))]
    
    WHdata_trace_4 = []
    for i in range(len(WHdata_trace_2)-1):
        _ = (WHdata_trace_2[i+1]-WHdata_trace_2[i])/ratio_inter
        WHdata_trace_4.append(_)
    WHx4 = [ratio_inter*i for i in range(len(WHdata_trace_4))]
    Ldata_trace_4 = []
    for i in range(len(Ldata_trace_2)-1):
        _ = (Ldata_trace_2[i+1]-Ldata_trace_2[i])/ratio_inter
        Ldata_trace_4.append(_)
    Lx4 = [ratio_inter*i for i in range(len(Ldata_trace_4))]
    
    left_edge1 = filename1.rfind('\\') + 1
    left_edge2 = filename2.rfind('\\') + 1
    right_edge1 = filename1.rfind('.')
    right_edge2 = filename2.rfind('.')
    print(filename1[left_edge1:right_edge1])
    print(filename2[left_edge2:right_edge2])
    print()

    fig, axs = plt.subplots(2, 4, figsize=(16, 9))
    #fig, axs = plt.subplots(2, 3)
    axs[0][0].plot(WHx1, WHdata_trace_1, label='CMDV', color='blue')
    axs[0][1].plot(WHx2, WHdata_trace_2, label='CMDA', color='green')
    axs[0][2].plot(WHx4, WHdata_trace_4, label='CMDJ', color='black')
    axs[0][3].plot(WHx3, WHdata_trace_3, label='CMDT', color='red')
    axs[1][0].plot(Lx1, Ldata_trace_1, label='CMDV', color='blue')
    axs[1][1].plot(Lx2, Ldata_trace_2, label='CMDA', color='green')
    axs[1][2].plot(Lx4, Ldata_trace_4, label='CMDJ', color='black')
    axs[1][3].plot(Lx3, Ldata_trace_3, label='CMDT', color='red')
    axs[0][0].set_title(filename1[left_edge1:right_edge1])
    axs[1][0].set_title(filename2[left_edge2:right_edge2])
    for i in range(2):
        for j in range(4):
            axs[i][j].legend()
    fig.canvas.manager.full_screen_toggle() # toggle fullscreen mode
    #plt.show()
    plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.png',dpi=365, format='png') 
    #plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.svg', format='svg') 
    

def get_filename(filepath, return_filenames):
    """
        get a relative filename path in the path given
    """
    main_dir_path = ''
    names = []
    for dirpath, dirnames, filenames in os.walk(filepath):
        main_dir_path = dirpath
        names = filenames
    for name in names:
        _ = os.path.join(main_dir_path, name)
        return_filenames.append(_)

def save_data_picture():
    WH_filenames = []
    L_filenames = []
    file_path1 = '麦迪克加工问题调查\采样数据-维宏'
    file_path2 = '麦迪克加工问题调查\采样数据-LYNUC'
    get_filename(file_path1, WH_filenames)
    get_filename(file_path2, L_filenames)
    for i in range(len(WH_filenames)):
        for j in range(len(L_filenames)):
            WH_left_edge = WH_filenames[i].rfind('\\') + 3
            WH_right_edge = WH_filenames[i].rfind('.')
            L_left_edge = L_filenames[j].rfind('\\') + 3
            L_right_edge = L_filenames[j].rfind('.')
            # print(WH_filenames[i][WH_left_edge:WH_right_edge])
            # print(L_filenames[j][L_left_edge:L_right_edge])
            if WH_filenames[i][WH_left_edge:WH_right_edge] == L_filenames[j][L_left_edge:L_right_edge]:
                print(WH_filenames[i])
                print(L_filenames[j])
                print()
                #print(WH_filenames[i][WH_left_edge:WH_right_edge][0])
                if WH_filenames[i][WH_left_edge:WH_right_edge][0] == '1':
                    plot_func_add_j(WH_filenames[i], L_filenames[j], 0.001)
                    #plot_func(WH_filenames[i], L_filenames[j], 0.001)
                elif WH_filenames[i][WH_left_edge:WH_right_edge][0] == '2':
                    plot_func_add_j(WH_filenames[i], L_filenames[j], 0.002)
                    #plot_func(WH_filenames[i], L_filenames[j], 0.002)

def main():
    """
        do main  function 
    """
    #麦迪克加工问题调查\采样数据-LYNUC\L-1ms-直边Y-V2.std
    #plot_func_add_j('麦迪克加工问题调查\采样数据-维宏\W-1ms-斜边X-V1.std', '麦迪克加工问题调查\采样数据-LYNUC\L-1ms-斜边X-V1.std')
    #plot_func_add_j('麦迪克加工问题调查\采样数据-维宏\W-1ms-直边Y-V2.std', '麦迪克加工问题调查\采样数据-LYNUC\L-1ms-直边Y-V2.std', 0.001)
    save_data_picture()


if __name__ == "__main__":
    main()
