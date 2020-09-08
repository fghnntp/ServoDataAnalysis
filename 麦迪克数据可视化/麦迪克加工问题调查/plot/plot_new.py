import csv
import matplotlib.pyplot as plt
import os
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

def get_filepath_filename(filepath, return_filenames):
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

def get_data(filename, data_time, data_v, data_cmdt, data_cmdv):
    with open(filename, 'r') as f:
        count = 0
        lines = csv.reader(f)
        for line in lines:
            count += 1
            if count >= 17:
                data_time.append(eval(line[0]))
                data_v.append(eval(line[1]))
                data_cmdt.append(eval(line[2]))
                data_cmdv.append(eval(line[3]))

def plot_v_a_j_t(filename, smaple_time=2, save_file=False):
    data_time = []
    data_v = []
    data_cmdt = []
    data_cmdv = []
    get_data(filename, data_time, data_v, data_cmdt, data_cmdv)

    data_time = [0.001*i for i in data_time]
    data_cmda = []
    for i in range(len(data_cmdv)-1):
        data = (data_cmdv[i+1] - data_cmdv[i])/smaple_time
        data_cmda.append(data)
    cmda_x = [smaple_time*i for i in range(len(data_cmda))]

    data_cmdj = []
    for i in range(len(data_cmda)-1):
        data = (data_cmda[i+1] - data_cmda[i]) / smaple_time
        data_cmdj.append(data)
    cmdj_x = [smaple_time*i for i in range(len(data_cmdj))]

    left_edge = filename.rfind('\\') + 1
    right_edge = filename.rfind('.')
    print(filename[left_edge:right_edge])
    fig, axs =  plt.subplots(4)
    axs[0].plot(data_time, data_cmdv, label='cmdv', color='red')
    axs[0].set_title(filename[left_edge:right_edge])
    axs[1].plot(cmda_x, data_cmda, label='cmda', color='black')
    axs[2].plot(cmdj_x, data_cmdj, label='cmdj', color='blue')
    axs[3].plot(data_time, data_cmdt, label='cmdt', color='orange')

    for i in range(4):
        axs[i].legend()
    if save_file:
        plt.savefig(filename[left_edge:right_edge] + '.png', dpi=600, format="png")
    else:
        plt.show()

def main():
    filepath = '麦迪克数据可视化\\麦迪克加工问题调查\\200907'
    filenames = []
    get_filepath_filename(filepath, filenames)
    for filename in filenames:
        sample_time = eval(filename[filename.rfind('\\')+3])
        if sample_time == 2:
            _ = 0.001 * sample_time
            plot_v_a_j_t(filename, smaple_time=_, save_file=True)

def get_WH_data(filename, list_ch1, list_ch2, list_ch3):
    """
        input filename, and excrat CH1, CH2, CH3 data to list_ch1, list_ch2 and list_ch3

        CH1: 反馈速度 CMDV
        CH2: 指定速度 ACTV
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

def plot_WH_L(save_file=False):
    filename_WH = '麦迪克数据可视化\\麦迪克加工问题调查\\采样数据-维宏\\W-2ms-圆Y-V3.std'
    filename_L = '麦迪克数据可视化\\麦迪克加工问题调查\\200907\\Y-2000us-圆形.csv'
    WH_data_cmdv = []
    WH_data_v = []
    WH_data_cmdt = []
    L_data_time = []
    L_data_v = []
    L_data_cmdt = []
    L_data_cmdv = []
    get_WH_data(filename_WH, WH_data_v, WH_data_cmdv, WH_data_cmdt)
    get_data(filename_L, L_data_time, L_data_v, L_data_cmdt, L_data_cmdv)

    # for i in WH_data_cmdv:
    #     print(i)

    WH_data_time = [0.001*i for i in L_data_time]
    WH_data_cmda = []
    for i in range(len(WH_data_cmdv)-1):
        data = (WH_data_cmdv[i+1] - WH_data_cmdv[i])/0.002
        WH_data_cmda.append(data)
    WH_cmda_x = [0.002*i for i in range(len(WH_data_cmda))]

    WH_data_cmdj = []
    for i in range(len(WH_data_cmda)-1):
        data = (WH_data_cmda[i+1] - WH_data_cmda[i]) / 2
        WH_data_cmdj.append(data)
    WH_cmdj_x = [0.002*i for i in range(len(WH_data_cmdj))]

    
    L_data_time = [0.001*i for i in L_data_time]
    L_data_cmda = []
    for i in range(len(L_data_cmdv)-1):
        data = (L_data_cmdv[i+1] - L_data_cmdv[i])/0.002
        L_data_cmda.append(data)
    L_cmda_x = [0.002*i for i in range(len(L_data_cmda))]

    L_data_cmdj = []
    for i in range(len(L_data_cmda)-1):
        data = (L_data_cmda[i+1] - L_data_cmda[i]) / 2
        L_data_cmdj.append(data)
    L_cmdj_x = [0.002*i for i in range(len(L_data_cmdj))]

    WH_data_ta = []
    for i in range(len(WH_data_cmdt) - 1):
        data = (WH_data_cmdt[i+1] - WH_data_cmdt[i]) / 0.002
        WH_data_ta.append(data)
    WH_ta_x = [0.002*i for i in range(len(WH_data_ta))]

    L_data_ta = []
    for i in range(len(L_data_cmdt) - 1):
        data = (L_data_cmdt[i+1] - L_data_cmdt[i]) / 0.002
        L_data_ta.append(data)
    L_ta_x = [0.002*i for i in range(len(L_data_ta))]


    # step_WH = 738
    # step_L = 738
    # print(step_WH,step_L)

    # WH_data_time = [0.002*i for i in range(step_WH)]
    # WH_cmda_x = [0.002*i for i in range(step_WH)]
    # WH_cmdj_x = [0.002*i for i in range(step_WH)]
    # WH_ta_x = [0.002*i for i in range(step_WH)]

    # left_WH = 110
    # right_WH = 848
    # print(right_WH, left_WH)
    # WH_data_cmdv = WH_data_cmdv[left_WH:right_WH]
    # WH_data_cmda = WH_data_cmda[left_WH:right_WH]
    # WH_data_cmdj = WH_data_cmdj[left_WH:right_WH]
    # WH_data_cmdt = WH_data_cmdt[left_WH:right_WH]
    # WH_data_ta = WH_data_ta[left_WH:right_WH]
    
    
    # L_data_time = [0.002*i for i in range(step_L)]
    # L_cmda_x = [0.002*i for i in range(step_L)]
    # L_cmdj_x = [0.002*i for i in range(step_L)]
    # L_ta_x = [0.002*i for i in range(step_L)]
    # left_L = 260
    # right_L = 998
    # print(right_L, left_L)
    # L_data_cmdv = L_data_cmdv[left_L:right_L]

    # L_data_cmda = L_data_cmda[left_L:right_L]
    # L_data_cmdj = L_data_cmdj[left_L:right_L]
    # L_data_cmdt = L_data_cmdt[left_L:right_L]
    # L_data_ta = L_data_ta[left_L:right_L]

    fig, axs = plt.subplots(5)
    axs[0].plot(WH_data_time, WH_data_cmdv, label='WH_cmdv', color='red')
    axs[0].plot(L_data_time, L_data_cmdv, label='L_cmdv', color='black')
    axs[1].plot(WH_cmda_x, WH_data_cmda, label='WH_cmda', color='red')
    axs[1].plot(L_cmda_x, L_data_cmda, label='L_cmda', color='black')
    axs[2].plot(WH_cmdj_x, WH_data_cmdj, label='WH_cmdj', color='red')
    axs[2].plot(L_cmdj_x, L_data_cmdj, label='L_cmdj', color='black')
    axs[3].plot(WH_data_time, WH_data_cmdt, label='WH_cmdt', color='red')
    axs[3].plot(L_data_time, L_data_cmdt, label='L_cmdt', color='black')
    axs[4].plot(WH_ta_x, WH_data_ta, color='red')
    axs[4].plot(L_ta_x, L_data_ta, color='black')


    for i in range(5):
        axs[i].legend()

    left_edge_L = filename_L.rfind('\\') + 1
    right_edge_L = filename_L.rfind('.')
    left_edge_WH = filename_WH.rfind('\\') + 1
    right_edge_WH = filename_WH.rfind('.')
    print(filename_WH[left_edge_WH:right_edge_WH]+'-'+filename_L[left_edge_L:right_edge_L])    

    if save_file:
        plt.savefig(filename_WH[left_edge_WH:right_edge_WH]+'-'+filename_L[left_edge_L:right_edge_L] + '.png', dpi=300, format="png")
    else:
        plt.show()
    

if __name__ == "__main__":
    plot_WH_L(save_file=True)
