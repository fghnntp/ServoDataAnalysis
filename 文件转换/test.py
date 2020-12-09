import numpy as np
import matplotlib.pyplot as plt
 
plt.ion()
plt.figure(1)
t_list = []
result_list = []
t = 0
"""/c/Users/liuleyong/AppData/Roaming/Python/Python39/Scripts"""
while True:
    if t >= 100 * np.pi:
        plt.clf()
        t = 0
        t_list.clear()
        result_list.clear()
    else:
        t += np.pi / 4
        t_list.append(t)
        result_list.append(np.sin(t))
        plt.plot(t_list, result_list,c='r',ls='-', marker='o', mec='b',mfc='w')  ## 保存历史数据
        #plt.plot(t, np.sin(t), 'o')
        plt.pause(0.1)