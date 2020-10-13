import json

def set_settings(file_src, file_des):
    """
        配置.dat文件的设置列表，并将其写入data文件
    """
    #获取配置文件
    date = {}
    with open(file_src, 'r') as f:
        date = json.load(f)
    #将配置文件变成字符串形式写入data文件
    setting = "[setting]\n"
    for key, val in  date["setting"].items():
        setting += key+"="+val+"\n"
    setting += "[data]\n"
    print(setting)
    with open(file_des, "w") as f:
        f.write(setting)

def get_data(filename, data_trace_1, data_trace_2, data_trace_3):
    """
        获取源数据文件的数据，并对应通道
        1:反馈速度
        2:转矩指令
        3:指令速度
    """
    with open(filename, 'r', encoding='gbk') as f:
        for line in f.readlines():
            _ = line[:-1].split(',')
            if _[0][:-5] == 'DataTrace1-TraceData':
                for e in _[1:]:
                    e_c = e
                    data_trace_1.append(e_c)
            elif _[0][:-5] == 'DataTrace2-TraceData':
                for e in _[1:]:
                    e_c = e
                    data_trace_2.append(e_c)
            elif _[0][:-5] == 'DataTrace3-TraceData':
                for e in _[1:]:
                    e_c = e
                    data_trace_3.append(e_c)
def add_data(file_src, file_des):
    data_trace_1 = []
    data_trace_2 = []
    data_trace_3 = []
    get_data(file_src, data_trace_1, data_trace_2, data_trace_3)
    data_trace_cmdv = data_trace_3
    data_trace_cmda = []
    for i in range(len(data_trace_cmdv)-1):
        data_trace_cmda.append(str((eval(data_trace_cmdv[i+1])-eval(data_trace_cmdv[i]))/0.002))
    data_trace_cmdj = []
    for i in range(len(data_trace_cmda)-1):
        data_trace_cmdj.append(str((eval(data_trace_cmda[i+1])-eval(data_trace_cmda[i]))/0.002))
    data_trace_cmdt = data_trace_2
    with open("new_data.dat", 'a') as f:
        length = min(len(data_trace_cmdv), len(data_trace_cmda), len(data_trace_cmdj), len(data_trace_cmdt))
        for i in range(length):
            f.write(data_trace_cmdv[i]+','+data_trace_cmda[i]+','+data_trace_cmdj[i]+","+data_trace_cmdt[i]+'\n')
    
def main():
    set_settings("文件转换/setting.json", "new_data.dat")
    add_data("文件转换/铼钠克-X-MDIF10000-99.std", "new_data.dat")
    

if __name__ == "__main__":
    main()

    
