import sys
import os 
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from mainWindow import Ui_transferFile
from transferFile import set_settings, add_data, add_data_pvt

class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_transferFile()
        self.ui.setupUi(self)
        self.show()
        self.filename_src = ""
        self.filename_des = ""
        self.ui.pushButtonSelectFile.clicked.connect(self.open_file)
        self.ui.pushButtonTransferRDI.clicked.connect(self.transfer_file_rdi)
        self.ui.pushButtonTransferPVT.clicked.connect(self.transfer_file_pvt)

    def open_file(self):
        """
            获取文件位置以及文件名称
        """
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "std Files(*.std);;ALL Files(*)")
        self.filename_src = fileName
        self.filename_des = fileName[fileName.rfind("/")+1:fileName.rfind(".")]+".dat"

    def transfer_file_rdi(self):
        """
            对文件进行转换
        """
        set_settings("setting.json", self.filename_des)
        add_data(self.filename_src, self.filename_des)
        print("tranfer "+self.filename_src+" to "+self.filename_des+" complete")

    def transfer_file_pvt(self):
        add_data_pvt(self.filename_src, self.filename_des[:-4]+'.pvt') 
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainWindowStance = mainWindow()
    sys.exit(app.exec_())