# -*- coding:utf-8 -*-
import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
print('当前主机名称为: ' +host)
port = 42683                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 监听连接,传入连接请求的最大数5
while True:
    c,addr = s.accept()     # 建立客户端连接。
    print ('连接地址：', addr)
    data='hello word,你好，世界！'
    c.send(data.encode())
    c.close()                # 关闭连接