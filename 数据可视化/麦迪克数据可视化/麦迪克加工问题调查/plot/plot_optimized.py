import numpy as np
import matplotlib.pyplot as plt
import os
from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['MicroSoft YaHei'] # 指定默认字体
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


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


def get_WH_threefile_data(WH_filename1, WH_filename2, WH_filename3,
                          WH_data_trace_1_1, WH_data_trace_1_2, WH_data_trace_1_3,
                          WH_data_trace_2_1, WH_data_trace_2_2, WH_data_trace_2_3,
                          WH_data_trace_3_1, WH_data_trace_3_2, WH_data_trace_3_3):
    get_data(WH_filename1, WH_data_trace_1_1, WH_data_trace_1_2, WH_data_trace_1_3)
    get_data(WH_filename2, WH_data_trace_2_1, WH_data_trace_2_2, WH_data_trace_2_3)
    get_data(WH_filename3, WH_data_trace_3_1, WH_data_trace_3_2, WH_data_trace_3_3)


def get_L_threefile_data(L_filename1, L_filename2, L_filename3,
                         L_data_trace_1_1, L_data_trace_1_2, L_data_trace_1_3,
                         L_data_trace_2_1, L_data_trace_2_2, L_data_trace_2_3,
                         L_data_trace_3_1, L_data_trace_3_2, L_data_trace_3_3):
    get_data(L_filename1, L_data_trace_1_1, L_data_trace_1_2, L_data_trace_1_3)
    get_data(L_filename2, L_data_trace_2_1, L_data_trace_2_2, L_data_trace_2_3)
    get_data(L_filename3, L_data_trace_3_1, L_data_trace_3_2, L_data_trace_3_3)


def plot_four_figure_func(filename1, filename2, filename3, filename4, filename5, filename6, ratio):
    inter_ratio = ratio
    WH_data_trace_1_1 = []
    WH_data_trace_1_2 = []
    WH_data_trace_1_3 = []
    WH_data_trace_2_1 = []
    WH_data_trace_2_2 = []
    WH_data_trace_2_3 = []
    WH_data_trace_3_1 = []
    WH_data_trace_3_2 = []
    WH_data_trace_3_3 = []
    L_data_trace_1_1 = []
    L_data_trace_1_2 = []
    L_data_trace_1_3 = []
    L_data_trace_2_1 = []
    L_data_trace_2_2 = []
    L_data_trace_2_3 = []
    L_data_trace_3_1 = []
    L_data_trace_3_2 = []
    L_data_trace_3_3 = []
    get_WH_threefile_data(filename1, filename2, filename3,
                          WH_data_trace_1_1, WH_data_trace_1_2, WH_data_trace_1_3,
                          WH_data_trace_2_1, WH_data_trace_2_2, WH_data_trace_2_3,
                          WH_data_trace_3_1, WH_data_trace_3_2, WH_data_trace_3_3)
    get_L_threefile_data(filename4, filename5, filename6,
                         L_data_trace_1_1, L_data_trace_1_2, L_data_trace_1_3,
                         L_data_trace_2_1, L_data_trace_2_2, L_data_trace_2_3,
                         L_data_trace_3_1, L_data_trace_3_2, L_data_trace_3_3)
    # WH指令速度 Y轴
    WH_data_trace_1 = WH_data_trace_1_1 + WH_data_trace_2_1 + WH_data_trace_3_1
    WH_data_trace_2 = WH_data_trace_1_2 + WH_data_trace_2_2 + WH_data_trace_3_2
    # WH指令力矩 Y轴
    WH_data_trace_3 = WH_data_trace_1_3 + WH_data_trace_2_3 + WH_data_trace_3_3
    # L指令速度 Y轴
    L_data_trace_1 = L_data_trace_1_1 + L_data_trace_2_1 + L_data_trace_3_1
    L_data_trace_2 = L_data_trace_1_2 + L_data_trace_2_2 + L_data_trace_3_2
    # L指令力矩 Y轴
    L_data_trace_3 = L_data_trace_1_3 + L_data_trace_2_3 + L_data_trace_3_3

    # WH速度指令 x轴
    WH_vx = [inter_ratio*i for i in range(len(WH_data_trace_1))]
    # L速度指令 y轴
    L_vx = [inter_ratio*i for i in range(len(L_data_trace_1))]

    # WH力矩指令 x轴
    WH_tx = [inter_ratio*i for i in range(len(WH_data_trace_3))]
    # L力矩指令 x轴
    L_tx = [inter_ratio*i for i in range(len(L_data_trace_3))]

    # WH加速度 y轴
    WH_a_data = []
    # L架速度 y轴
    L_a_data = []

    for i in range(len(WH_data_trace_1)-1):
        _ = (WH_data_trace_1[i+1]-WH_data_trace_1[i])/inter_ratio
        if abs(_)>10000:
            _ = 0
        WH_a_data.append(_)
    # WH 加速度 x轴
    WH_ax = [inter_ratio*i for i in range(len(WH_a_data))]

    for i in range(len(L_data_trace_1)-1):
        _ = (L_data_trace_1[i+1]-L_data_trace_1[i])/inter_ratio
        if abs(_)>10000:
            _ = 0
        L_a_data.append(_)
    # L 加速度 x轴
    L_ax = [inter_ratio*i for i in range(len(L_a_data))]

    # WH 加加速度 y轴
    WH_j_data = []
    # L 加加速度 y轴
    L_j_data = []
    for i in range(len(WH_a_data)-1):
        _ = (WH_a_data[i+1]-WH_a_data[i])/inter_ratio
        if abs(_) > 1e6:
            _ = 0
        WH_j_data.append(_)
    # WH 加加速度 x轴
    WH_jx = [inter_ratio*i for i in range(len(WH_j_data))]

    for i in range(len(L_a_data)-1):
        _ = (L_a_data[i+1]-L_a_data[i])/inter_ratio
        if abs(_) > 1e6:
            _ = 0
        L_j_data.append(_)
    # L 加加速度 x轴
    L_jx = [inter_ratio*i for i in range(len(L_j_data))]

    left_edge1 = filename1.rfind('\\') + 1
    left_edge2 = filename4.rfind('\\') + 1
    right_edge1 = filename1.rfind('.')-3
    right_edge2 = filename4.rfind('.')-3
    print(filename1[left_edge1:right_edge1])
    print(filename4[left_edge2:right_edge2])
    print()

    # print(WH_vx)
    # print(WH_data_trace_1)
    fig, axs = plt.subplots(4)
    #fig, axs = plt.subplots(2, 3)
    axs[0].plot(WH_vx, WH_data_trace_1, label='WH_CMDV', color='blue')
    axs[0].plot(L_vx, L_data_trace_1, label='L_CMDV', color='red')
    axs[0].set_title(filename1[left_edge1:right_edge1] +
                     '-'+filename4[left_edge2:right_edge2])
    axs[1].plot(WH_ax, WH_a_data, label='WH_CMDA', color='blue')
    axs[1].plot(L_ax, L_a_data, label='L_CMDA', color='red')
    axs[2].plot(WH_jx, WH_j_data, label='WH_CMDJ', color='blue')
    axs[2].plot(L_jx, L_j_data, label='L_CMDJ', color='red')
    axs[3].plot(WH_tx, WH_data_trace_3, label='WH_CMDT', color='blue')
    axs[3].plot(L_tx, L_data_trace_3, label='L_CMDT', color='red')

    for i in range(4):
        axs[i].legend()
    plt.savefig(filename1[left_edge1:right_edge1] +
                '-'+filename4[left_edge2:right_edge2]+'.png', dpi=600, format="png")
    #fig.canvas.manager.full_screen_toggle()  # toggle fullscreen mode
    #plt.show()


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
    #fig.canvas.manager.full_screen_toggle()  # toggle fullscreen mode
    #plt.show()
    plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.png',dpi=365, format='png')
    plt.savefig(filename1[left_edge1:right_edge1]+'-'+filename2[left_edge2:right_edge2]+'.svg', format='svg')


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
    filename = []
    file_path1 = '麦迪克数据可视化\麦迪克加工问题调查\维宏丝杆-32导程'
    file_path2 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-LYNUC'
    
    # file_path1 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-维宏'
    # file_path2 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-LYNUC'
    get_filename(file_path1, WH_filenames)
    get_filename(file_path2, L_filenames)
    in_list = []
    file_list = []
    for i in range(len(WH_filenames)//3):
        tuple_list = []
        count = 0
        for j in WH_filenames:
            if len(tuple_list) == 0 and j not in in_list:
                in_list.append(j)
                tuple_list.append(j)
                count += 1
                continue
            if len(tuple_list) > 0 and j[j.rfind('\\')+3:j.rfind('.')-3] == tuple_list[0][tuple_list[0].rfind('\\')+3:tuple_list[0].rfind('.')-3]:
                in_list.append(j)
                tuple_list.append(j)
                count += 1
            if count == 3:
                break
        for k in L_filenames:
            if len(tuple_list) > 0 and k[k.rfind('\\')+3:k.rfind('.')-3] == tuple_list[0][tuple_list[0].rfind('\\')+3:tuple_list[0].rfind('.')-3]:
                in_list.append(k)
                tuple_list.append(k)
                count += 1
            if count == 6:
                break
        file_list.append(tuple_list)
    for i in file_list:
        for j in i:
            print(j)
        print()

    for i in file_list:
        ratio = eval(i[0][i[0].rfind('\\')+3])
        plot_four_figure_func(i[0], i[1], i[2], i[3], i[4], i[5], ratio*0.001)



def main():
    filename1 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-维宏\W-1ms-斜边X-V1.std'
    filename2 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-维宏\W-1ms-斜边X-V2.std'
    filename3 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-维宏\W-1ms-斜边X-V3.std'
    filename4 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-LYNUC\L-1ms-斜边X-V1.std'
    filename5 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-LYNUC\L-1ms-斜边X-V2.std'
    filename6 = '麦迪克数据可视化\麦迪克加工问题调查\采样数据-LYNUC\L-1ms-斜边X-V3.std'
    plot_four_figure_func(filename1, filename2, filename3,
                           filename4, filename5, filename6, 0.001)

if __name__ == "__main__":
    save_data_picture()
    #main()
