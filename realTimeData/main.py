import sys
import os 
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from mainWindow import Ui_Dialog
from get_data import get_data_dat
from plot_data import plot_data_chan

class mainWindow(QDialog):
    def __init__(self):
        """
            对转化文件的界面进行显示
        """
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #设置显示行和列的最大最小值
        self.ui.spinBox_num_set_row.setMinimum(1)
        self.ui.spinBox_num_set_row.setMaximum(2)
        self.ui.spinBox_num_set_col.setMinimum(1)
        self.ui.spinBox_num_set_col.setMaximum(2)
        self.ui.spinBox_data1_row.setMinimum(1)
        self.ui.spinBox_data1_row.setMaximum(2)
        self.ui.spinBox_data1_col.setMinimum(1)
        self.ui.spinBox_data1_col.setMaximum(2)
        self.ui.spinBox_data2_row.setMinimum(1)
        self.ui.spinBox_data2_row.setMaximum(2)
        self.ui.spinBox_data2_col.setMinimum(1)
        self.ui.spinBox_data2_col.setMaximum(2)
        self.ui.spinBox_data3_row.setMinimum(1)
        self.ui.spinBox_data3_row.setMaximum(2)
        self.ui.spinBox_data3_col.setMinimum(1)
        self.ui.spinBox_data3_col.setMaximum(2)
        self.ui.spinBox_data4_row.setMinimum(1)
        self.ui.spinBox_data4_row.setMaximum(2)
        self.ui.spinBox_data4_col.setMinimum(1)
        self.ui.spinBox_data4_col.setMaximum(2) 
        #初始化内部变量
        self.row = self.ui.spinBox_num_set_row.value()
        self.col = self.ui.spinBox_num_set_col.value()
        self.filename_src = ''
        self.plot_setting = {}
        self.data_chan_num = 0
        self.data_src = None
        self.plot_locate = [[1, 1], [1, 1], [1, 1], [1, 1]]
        self.plot_info = ['', '', '', '']
        #信号，槽绑定
        self.ui.spinBox_num_set_row.valueChanged.connect(self.plot_row_change)
        self.ui.spinBox_num_set_col.valueChanged.connect(self.plot_col_change)
        self.ui.pushButton_open.clicked.connect(self.open_file)
        self.ui.spinBox_data1_row.valueChanged.connect(self.chan1_locate1_change)
        self.ui.spinBox_data1_col.valueChanged.connect(self.chan1_locate2_change)
        self.ui.spinBox_data2_row.valueChanged.connect(self.chan2_locate1_change)
        self.ui.spinBox_data2_col.valueChanged.connect(self.chan2_locate2_change)
        self.ui.spinBox_data3_row.valueChanged.connect(self.chan3_locate1_change)
        self.ui.spinBox_data3_col.valueChanged.connect(self.chan3_locate2_change)
        self.ui.spinBox_data4_row.valueChanged.connect(self.chan4_locate1_change)
        self.ui.spinBox_data4_col.valueChanged.connect(self.chan4_locate2_change)
        self.ui.comboBox_data_se1.currentIndexChanged.connect(self.comboBox_data_se1_change)
        self.ui.comboBox_data_sel2.currentIndexChanged.connect(self.comboBox_data_sel2_change)
        self.ui.comboBox_data_se3.currentIndexChanged.connect(self.comboBox_data_se3_change)
        self.ui.comboBox_data_se4.currentIndexChanged.connect(self.comboBox_data_se4_change)
        self.ui.pushButton_plot.clicked.connect(self.plot_data)
        
    def plot_row_change(self):
        """
            改变绘制行
        """
        row = self.ui.spinBox_num_set_row.value()
        self.row = row
    
    def plot_col_change(self):
        """
            改变绘制列
        """
        col = self.ui.spinBox_num_set_col.value()
        self.col = col
    
    def chan1_locate1_change(self):
        """
            通道1数据横坐标位置改变
        """
        self.plot_locate[0][0] = self.ui.spinBox_data1_row.value()

    def chan1_locate2_change(self):
        """
            通道1数据纵坐标位置改变
        """
        self.plot_locate[0][1] = self.ui.spinBox_data1_col.value()

    def chan2_locate1_change(self):
        """
            通道2数据横坐标位置改变
        """
        self.plot_locate[1][0] = self.ui.spinBox_data2_row.value()

    def chan2_locate2_change(self):
        """
            通道2数据纵坐标位置改变
        """
        self.plot_locate[1][1] = self.ui.spinBox_data2_col.value()

    def chan3_locate1_change(self):
        """
            通道3数据横坐标位置改变
        """
        self.plot_locate[2][0] = self.ui.spinBox_data3_row.value()

    def chan3_locate2_change(self):
        """
            通道3数据纵坐标位置改变
        """
        self.plot_locate[2][1] = self.ui.spinBox_data3_col.value()

    def chan4_locate1_change(self):
        """
            通道4数据横坐标改变
        """
        self.plot_locate[3][0] = self.ui.spinBox_data4_row.value()

    def chan4_locate2_change(self):
        """
            通道4数据纵坐标位置改变
        """
        self.plot_locate[3][1] = self.ui.spinBox_data4_col.value()

    def comboBox_data_se1_change(self):
        """
            通道1数据名称改变
        """
        self.plot_info[0] = self.ui.comboBox_data_se1.currentText()

    def comboBox_data_sel2_change(self):
        """
            通道2数据名称改变
        """
        self.plot_info[1] = self.ui.comboBox_data_sel2.currentText()

    def comboBox_data_se3_change(self):
        """
            通道3数据名称改变
        """
        self.plot_info[2] = self.ui.comboBox_data_se3.currentText()
    
    def comboBox_data_se4_change(self):
        """
            通道4数据名称改变
        """
        self.plot_info[3] = self.ui.comboBox_data_se4.currentText() 

    def open_file(self):
        """
            获取文件位置,类型以及文件名称,并获得数据通道
        """
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "dat Files(*.dat);;ALL Files(*)")
        self.filename_src = fileName
        #get chan_num and plot_setting and data_src
        if self.filename_src != '':
            self.data_chan_num, self.data_src = get_data_dat(self.filename_src, self.plot_setting)
        #add data to plot
        if self.data_chan_num != 0:
            #clear all comboBox
            self.ui.comboBox_data_se1.clear()
            self.ui.comboBox_data_sel2.clear()
            self.ui.comboBox_data_se3.clear()
            self.ui.comboBox_data_se4.clear()
            #将comboBox中的所有数据清空，并且将打开文件所获得的数据加入
            for i in range(1, self.data_chan_num+1):
                self.ui.comboBox_data_se1.addItem(self.plot_setting['ch'+str(i)+'title'])
                self.ui.comboBox_data_sel2.addItem(self.plot_setting['ch'+str(i)+'title'])
                self.ui.comboBox_data_se3.addItem(self.plot_setting['ch'+str(i)+'title'])
                self.ui.comboBox_data_se4.addItem(self.plot_setting['ch'+str(i)+'title'])
            #为每个comboBox添加一个空白选项
            self.ui.comboBox_data_se1.addItem('')
            self.ui.comboBox_data_sel2.addItem('')
            self.ui.comboBox_data_se3.addItem('')
            self.ui.comboBox_data_se4.addItem('')
                
    def plot_data(self):
        """绘制图形"""
        plot_data_chan(self.filename_src, self.row, self.col, self.data_src, self.plot_setting, self.plot_locate, self.plot_info)
          
if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainWindowStance = mainWindow()
    mainWindowStance.show()
    sys.exit(app.exec_())