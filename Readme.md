# 伺服数据转换和可视化
## 基于matplotlib,伺服数据的可视化
    使用matplotlib进行可视化，执行脚本需要环境，数据放映真实采集数据
## 文件转换
    将伺服文件转换为RDI可以接受的.dat文件格式，让后续分析可以通过RDI进行，只反应趋势
    必须要采集的参数：位置指令速度(指令速度)，转矩指令
    使用方法：
        1.设置setting.json,注意将numbers参数改为合适的数量
        2.打开支持进行转换的文件，现支持：安川、汇川
        3.点击需要转换文件的转换按钮
    将main.py转换为.exe文件的指令 pyinstaller -F main.py -i bitbug_favicon.ico 
