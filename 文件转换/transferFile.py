import json
import csv

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

def get_data_from_anchuan(filename, data_trace_v, data_trace_t):
    """
        从安川伺服数据采样采集信息
        获取源数据文件的数据，并对应通道输出
    """
    with open(filename, 'r', encoding='gbk') as f:
        #找到位置指令速度和力矩所对应的通道
        count = 0
        data_relate = {"data_trace_v":"", "data_trace_t":""}
        for line in f.readlines():
            count += 1
            _ = line[:-1].split(',')
            #安川采样文件39，40，41可以判断数据的通道对应
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

def get_data_from_huichuan(file_src, data_trace_cmdv, data_trace_cmdt):
    """
        解析汇川伺服采样所导出的csv文件
    """
    with open(file_src, 'r', encoding='gbk') as f:
        csv_change = csv.reader(f)
        count = 0
        v_flag = False
        t_flag = False
        for row in csv_change:
            count += 1
            if count == 41:
                #汇川41行判断通道对应关系
                if row[0] == '速度指令(rpm)':
                    v_flag = 0
                if row[0] == '转矩指令(%)':
                    t_flag = 0
                for i in range(len(row)):
                    if row[i][1:] == '速度指令(rpm)':
                        v_flag = i
                    if row[i][1:] == '转矩指令(%)':
                        t_flag = i
            if count > 41:
                #汇川41行之后为伺服采集数据
                data_trace_cmdv.append(eval(row[v_flag][1:]))
                data_trace_cmdt.append(eval(row[t_flag][1:]))

def add_data2RDI(file_src, file_des):
    #接受数据v：速度,t：力矩
    data_trace_v = []
    data_trace_t = []
    #根据文件名后缀选择获取文件数据函数,输出均为float类型的列表
    if(file_src[file_src.rfind('.'):]=='.std'):
        get_data_from_anchuan(file_src, data_trace_v, data_trace_t)
    if(file_src[file_src.rfind('.'):]=='.csv'):
        get_data_from_huichuan(file_src, data_trace_v, data_trace_t)
    #将接收用的列表名字进行转换
    data_trace_cmdv = data_trace_v
    #通过速度列表获取加速度列表
    data_trace_cmda = []
    for i in range(len(data_trace_cmdv)-1):
        data_trace_cmda.append((data_trace_cmdv[i+1]-data_trace_cmdv[i])/0.002)
    #通过加速度列表获取加加速度列表
    data_trace_cmdj = []
    for i in range(len(data_trace_cmda)-1):
        data_trace_cmdj.append((data_trace_cmda[i+1]-data_trace_cmda[i])/0.002)
    #将接收用的列表名字进行转换
    data_trace_cmdt = data_trace_t
    #对力矩列表进行一阶差分
    data_trace_cmdtdiff = []
    for i in range(len(data_trace_t)-1):
        data_trace_cmdtdiff.append((data_trace_t[i+1]-data_trace_cmdt[i])/0.002)
    #用最短的列表长队对数据进行写入
    with open(file_des, 'a') as f:
        length = min(len(data_trace_cmdv), len(data_trace_cmda), len(data_trace_cmdj), len(data_trace_cmdt), len(data_trace_cmdtdiff))
        for i in range(length):
            f.write(str(data_trace_cmdv[i])+','+str(data_trace_cmda[i])+','+str(data_trace_cmdj[i])+","+str(data_trace_cmdt[i])+","+str(data_trace_cmdtdiff[i])+'\n')

def add_data2pvt(file_src, file_des):
    """
        将伺服采集数据转换为pvt格式文件
    """
    #转换为pvt格式文件只依赖于v：速度
    data_trace_v = []
    if(file_src[file_src.rfind('.'):]=='.std'):
        get_data_from_anchuan(file_src, data_trace_v, [])
    if(file_src[file_src.rfind('.'):]=='.csv'):
        get_data_from_huichuan(file_src, data_trace_v, [])
    data_trace_cmdv = data_trace_v
    data_trace_cmdp = []
    for i in range(len(data_trace_cmdv)):
        _ = 0
        for j in data_trace_cmdv[:i]:
            _ += 0.002*j
        data_trace_cmdp.append(_)
    #将数据进行写入
    with open(file_des, 'w') as f:
        f.write('G01 I13=2 PVT2.0\n')
        length = min(len(data_trace_cmdp), len(data_trace_cmdv))
        for i in range(length):
            f.write('X'+str(data_trace_cmdp[i])+':'+str(data_trace_cmdv[i])+' '+'Y0:0'+' '+'Z0:0'+'\n')
    
def main():
    pass
    #get_data("W-1ms-斜边X-V1.std", [], [])
    #get_data_from_huichuan("hc30100.csv",[],[])
    #add_data_pvt("XD-X-斜边-2ms-v1.std", "new_data.dat")
    
if __name__ == "__main__":
    main()

    
