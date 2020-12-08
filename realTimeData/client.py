# -*- coding:utf-8 -*-
import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 42683             # 设置端口好

s.connect((host, port))
print (s.recv(1024).decode())
s.close()