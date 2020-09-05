import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def plot_f_av_aav(filename1, filename2):
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
    #filename1 = '铼钠克-X-MDIF10000.std'

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
    #filename2 = '铼钠克-X-MDIF10000-99.std'
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
    axs[0][0].plot(WHx1, WHdata_trace_1, label='cmdV',color='r')
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

def get_data(filename, data_trace_1, data_trace_2, data_trace_3):
    with open(filename, 'r') as f:
        for line in f.readlines():
            _ = line[:-1].split(',')
            if _[0][:-5] == 'DataTrace1-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    data_trace_1.append(e_c)
            elif _[0][:-5] == 'DataTrace2-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    data_trace_2.append(e_c)
            elif _[0][:-5] == 'DataTrace3-TraceData':
                for e in _[1:]:
                    e_c = eval(e)
                    data_trace_3.append(e_c)
    

def ACTV_CMDT_CMDV_55(filename1, filename2, filename3, filename4, filename5):
    """
        CH1: 反馈速度
        CH2: 转矩指令
        CH3：指令速度
    """
    A_data_trace_1 = []
    A_data_trace_2 = []
    A_data_trace_3 = []
    get_data(filename1, A_data_trace_1, A_data_trace_2, A_data_trace_3)
    Ax1 = [0.001*i for i in range(len(A_data_trace_1))]
    Ax2 = [0.001*i for i in range(len(A_data_trace_2))]
    Ax3 = [0.001*i for i in range(len(A_data_trace_3))]

    C_data_trace_1 = []
    C_data_trace_2 = []
    C_data_trace_3 = []
    get_data(filename2, C_data_trace_1, C_data_trace_2, C_data_trace_3)
    Cx1 = [0.001*i for i in range(len(C_data_trace_1))]
    Cx2 = [0.001*i for i in range(len(C_data_trace_2))]
    Cx3 = [0.001*i for i in range(len(C_data_trace_3))]

    U_data_trace_1 = []
    U_data_trace_2 = []
    U_data_trace_3 = []
    get_data(filename3, U_data_trace_1, U_data_trace_2, U_data_trace_3)
    Ux1 = [0.001*i for i in range(len(U_data_trace_1))]
    Ux2 = [0.001*i for i in range(len(U_data_trace_2))]
    Ux3 = [0.001*i for i in range(len(U_data_trace_3))]

    X_data_trace_1 = []
    X_data_trace_2 = []
    X_data_trace_3 = []
    get_data(filename4, X_data_trace_1, X_data_trace_2, X_data_trace_3)
    Xx1 = [0.001*i for i in range(len(X_data_trace_1))]
    Xx2 = [0.001*i for i in range(len(X_data_trace_2))]
    Xx3 = [0.001*i for i in range(len(X_data_trace_3))]
    
    Z_data_trace_1 = []
    Z_data_trace_2 = []
    Z_data_trace_3 = []
    get_data(filename5, Z_data_trace_1, Z_data_trace_2, Z_data_trace_3)
    Zx1 = [0.001*i for i in range(len(Z_data_trace_1))]
    Zx2 = [0.001*i for i in range(len(Z_data_trace_2))]
    Zx3 = [0.001*i for i in range(len(Z_data_trace_3))]

    A_data_trace_1 = []
    C_data_trace_1 = []
    U_data_trace_1 = []
    X_data_trace_1 = []
    Z_data_trace_1 = []

    for i in range(len(A_data_trace_3)-1):
        A_data_trace_1.append((A_data_trace_3[i+1]-A_data_trace_3[i])/0.001)
    Ax1 = [0.001*i for i in range(len(A_data_trace_1))]

    for i in range(len(C_data_trace_3)-1):
        C_data_trace_1.append((C_data_trace_3[i+1]-C_data_trace_3[i])/0.001)
    Cx1 = [0.001*i for i in range(len(C_data_trace_1))]

    for i in range(len(U_data_trace_3)-1):
        U_data_trace_1.append((U_data_trace_3[i+1]-A_data_trace_3[i])/0.001)
    Ux1 = [0.001*i for i in range(len(U_data_trace_1))]

    for i in range(len(X_data_trace_3)-1):
        X_data_trace_1.append((X_data_trace_3[i+1]-X_data_trace_3[i])/0.001)
    Xx1 = [0.001*i for i in range(len(X_data_trace_1))]

    for i in range(len(Z_data_trace_3)-1):
        Z_data_trace_1.append((Z_data_trace_3[i+1]-Z_data_trace_3[i])/0.001)
    Zx1 = [0.001*i for i in range(len(Z_data_trace_1))]
    
    fig, axs = plt.subplots(5, 3, figsize=(10,10))
    axs[0][1].plot(Ax1, A_data_trace_1, label='CMDA', color='r')
    axs[0][2].plot(Ax2, A_data_trace_2, label='CMDT', color='g')
    axs[0][0].plot(Ax3, A_data_trace_3, label='CMDV', color='b')
    axs[0][0].set_title('A axis')

    axs[1][1].plot(Cx1, C_data_trace_1, label='CMDA', color='r')
    axs[1][2].plot(Cx2, C_data_trace_2, label='CMDT', color='g')
    axs[1][0].plot(Cx3, C_data_trace_3, label='CMDV', color='b')
    axs[1][0].set_title('C axis')
    
    axs[2][1].plot(Ux1, U_data_trace_1, label='CMDA', color='r')
    axs[2][2].plot(Ux2, U_data_trace_2, label='CMDT', color='g')
    axs[2][0].plot(Ux3, U_data_trace_3, label='CMDV', color='b')
    axs[2][0].set_title('U axis')

    axs[3][1].plot(Xx1, X_data_trace_1, label='CMDA', color='r')
    axs[3][2].plot(Xx2, X_data_trace_2, label='CMDT', color='g')
    axs[3][0].plot(Xx3, X_data_trace_3, label='CMDV', color='b')
    axs[3][0].set_title('X axis')

    axs[4][1].plot(Zx1, Z_data_trace_1, label='CMDA', color='r')
    axs[4][2].plot(Zx2, Z_data_trace_2, label='CMDT', color='g')
    axs[4][0].plot(Zx3, Z_data_trace_3, label='CMDV', color='b')
    axs[4][0].set_title('Z axis')

    for i in range(5):
        for j in range(3):
            axs[i][j].legend()

    #plt.show()

def ACTV_CMDT_CMDV_33(filename1, filename2, filename3):
    """
        CH1: 反馈速度
        CH2: 转矩指令
        CH3：指令速度
    """
    A_data_trace_1 = []
    A_data_trace_2 = []
    A_data_trace_3 = []
    get_data(filename1, A_data_trace_1, A_data_trace_2, A_data_trace_3)
    Ax1 = [0.001*i for i in range(len(A_data_trace_1))]
    Ax2 = [0.001*i for i in range(len(A_data_trace_2))]
    Ax3 = [0.001*i for i in range(len(A_data_trace_3))]

    C_data_trace_1 = []
    C_data_trace_2 = []
    C_data_trace_3 = []
    get_data(filename2, C_data_trace_1, C_data_trace_2, C_data_trace_3)
    Cx1 = [0.001*i for i in range(len(C_data_trace_1))]
    Cx2 = [0.001*i for i in range(len(C_data_trace_2))]
    Cx3 = [0.001*i for i in range(len(C_data_trace_3))]

    U_data_trace_1 = []
    U_data_trace_2 = []
    U_data_trace_3 = []
    get_data(filename3, U_data_trace_1, U_data_trace_2, U_data_trace_3)
    Ux1 = [0.001*i for i in range(len(U_data_trace_1))]
    Ux2 = [0.001*i for i in range(len(U_data_trace_2))]
    Ux3 = [0.001*i for i in range(len(U_data_trace_3))]

    A_data_trace_1 = []
    C_data_trace_1 = []
    U_data_trace_1 = []

    for i in range(len(A_data_trace_3)-1):
        A_data_trace_1.append((A_data_trace_3[i+1]-A_data_trace_3[i])/0.001)
    Ax1 = [0.001*i for i in range(len(A_data_trace_1))]

    for i in range(len(C_data_trace_3)-1):
        C_data_trace_1.append((C_data_trace_3[i+1]-C_data_trace_3[i])/0.001)
    Cx1 = [0.001*i for i in range(len(C_data_trace_1))]

    for i in range(len(U_data_trace_3)-1):
        U_data_trace_1.append((U_data_trace_3[i+1]-U_data_trace_3[i])/0.001)
    Ux1 = [0.001*i for i in range(len(U_data_trace_1))]

    fig, axs = plt.subplots(3, 3, figsize=(10,10))
    axs[0][1].plot(Ax1, A_data_trace_1, label='CMDA', color='r')
    axs[0][2].plot(Ax2, A_data_trace_2, label='CMDT', color='g')
    axs[0][0].plot(Ax3, A_data_trace_3, label='CMDV', color='b')
    axs[0][0].set_title(filename1[:-4])

    axs[1][1].plot(Cx1, C_data_trace_1, label='CMDA', color='r')
    axs[1][2].plot(Cx2, C_data_trace_2, label='CMDT', color='g')
    axs[1][0].plot(Cx3, C_data_trace_3, label='CMDV', color='b')
    axs[1][0].set_title(filename2[:-4])

    axs[2][1].plot(Ux1, U_data_trace_1, label='CMDA', color='r')
    axs[2][2].plot(Ux2, U_data_trace_2, label='CMDT', color='g')
    axs[2][0].plot(Ux3, U_data_trace_3, label='CMDV', color='b')
    axs[2][0].set_title(filename3[:-4])
    
    for i in range(3):
        for j in range(3):
            axs[i][j].legend()

    plt.show()

def main():
    filename_5 = ['木工加工数据可视化\\A-MDI下执行F10000.std', '木工加工数据可视化\\C-运行加工程序采集.std', '木工加工数据可视化\\U-运行加工程序采集.std', 
                '木工加工数据可视化\\X-运行加工程序采集.std', '木工加工数据可视化\\Z-MDI下执行F10000.std']
    ACTV_CMDT_CMDV_55(filename_5[0], filename_5[1], filename_5[2], filename_5[3], filename_5[4])
    filename_3 = ['木工加工数据可视化\\铼钠克-X-MDIF10000.std', '木工加工数据可视化\\铼钠克-X-MDIF10000-99.std', '木工加工数据可视化\\欧赛-x-MDI-F10000.std']
    ACTV_CMDT_CMDV_33(filename_3[0], filename_3[1], filename_3[2])

if __name__ == "__main__":
    main()