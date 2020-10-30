import sys
import os 
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from mainWindow import Ui_transferFile
from transferFile import set_settings, add_data2RDI, add_data2pvt

class mainWindow(QDialog):
    def __init__(self):
        """
            对转化文件的界面进行显示
        """
        super().__init__()
        self.ui = Ui_transferFile()
        self.ui.setupUi(self)
        self.show()
        #定义源文件位置和输出文件位置
        self.filename_src = ""
        self.filename_des = ""
        #将三个按钮对应三个槽
        self.ui.pushButtonSelectFile.clicked.connect(self.open_file)
        self.ui.pushButtonTransferRDI.clicked.connect(self.transfer_file2RDI)
        self.ui.pushButtonTransferPVT.clicked.connect(self.transfer_file2pvt)

    def open_file(self):
        """
            获取文件位置,类型以及文件名称
            *.std   安川文件
            *.csv   汇川文件
            *.dat   RDI文件
            *.pvt   LySmNC文件
        """
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "std Files(*.std);;csv Files(*.csv);;ALL Files(*)")
        self.filename_src = fileName
        self.filename_des = fileName[fileName.rfind("/")+1:fileName.rfind(".")]+".dat"

    def transfer_file2RDI(self):
        """
            将伺服数据文件转换为RDI支持文件
        """
        set_settings("setting.json", self.filename_des)
        add_data2RDI(self.filename_src, self.filename_des)
        #在控制台输出提示信息
        print("tranfer "+self.filename_src+" to "+self.filename_des+" complete")

    def transfer_file2pvt(self):
        """
            将伺服数据文件转换为PVT文件,LySmNC支持文件
        """
        add_data2pvt(self.filename_src, self.filename_des[:-4]+'.pvt') 
        print("tranfer "+self.filename_src+" to "+self.filename_des+" complete")
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainWindowStance = mainWindow()
    sys.exit(app.exec_())