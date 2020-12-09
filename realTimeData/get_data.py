def get_data_dat(file_src, plot_setting):
    with open(file_src, 'r') as f_obj:
        #get data chan data
        datas_list = f_obj.readlines()
        #get data chan
        chan_num = len(datas_list[-5].split(','))
        data_src = [[] for i in range(chan_num)]
        #if the datas is datas or the settings 
        data_flag = False
        #print(datas_list)
        for line in datas_list:
            #one line data
            datas = line.split(',')
            datas = [data.strip() for data in datas]
            count = 0
            for data in datas:
                if data_flag == True:
                    #get data
                    data_src[count].append(eval(data))
                    count += 1
                else:
                    #get the settings
                    if '=' in data:
                        plot_setting[data[:data.rfind('=')]] = data[data.rfind('=')+1:]
                if data == '[data]':
                    data_flag = True  
        return chan_num, data_src