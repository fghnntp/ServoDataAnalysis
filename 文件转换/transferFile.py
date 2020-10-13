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
    with open(file_des, "w") as f:
        f.write(setting)

def get_data(filename, data_trace_v, data_trace_t):
    """
        获取源数据文件的数据，并对应通道
        1:反馈速度
        2:转矩指令
        3:位置指令速度
    """
    with open(filename, 'r', encoding='gbk') as f:
        #找到位置指令速度和力矩所对应的通道
        count = 0
        data_relate = {"data_trace_v":"", "data_trace_t":""}
        for line in f.readlines():
            count += 1
            _ = line[:-1].split(',')
            if count == 39 or count == 40 or count == 41:
                if _[-2] == "\"位置指令速度\"":
                    data_relate["data_trace_v"] = _[0]
                if _[-2]== "\"转矩指令\"":
                    data_relate["data_trace_t"] = _[0]
            if _[0][:-5] == data_relate["data_trace_v"]+'-TraceData':
                for e in _[1:]:
                    e_c = e
                    data_trace_v.append(e_c)
            elif _[0][:-5] == data_relate["data_trace_t"]+'-TraceData':
                for e in _[1:]:
                    e_c = e
                    data_trace_t.append(e_c)
        print(data_relate)

def add_data(file_src, file_des):
    data_trace_v = []
    data_trace_t = []
    get_data(file_src, data_trace_v, data_trace_t)
    data_trace_cmdv = data_trace_v
    data_trace_cmda = []
    for i in range(len(data_trace_cmdv)-1):
        data_trace_cmda.append(str((eval(data_trace_cmdv[i+1])-eval(data_trace_cmdv[i]))/0.002))
    data_trace_cmdj = []
    for i in range(len(data_trace_cmda)-1):
        data_trace_cmdj.append(str((eval(data_trace_cmda[i+1])-eval(data_trace_cmda[i]))/0.002))
    data_trace_cmdt = data_trace_t
    with open(file_des, 'a') as f:
        length = min(len(data_trace_cmdv), len(data_trace_cmda), len(data_trace_cmdj), len(data_trace_cmdt))
        for i in range(length):
            f.write(data_trace_cmdv[i]+','+data_trace_cmda[i]+','+data_trace_cmdj[i]+","+data_trace_cmdt[i]+'\n')
    
def main():
    set_settings("setting.json", "new_data.dat")
    add_data("新代规划分析\XD-X-斜边-2ms-v1.std", "new_data.dat")
    

if __name__ == "__main__":
    main()

    
