# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_transferFile(object):
    def setupUi(self, transferFile):
        transferFile.setObjectName("transferFile")
        transferFile.resize(400, 300)
        self.pushButtonSelectFile = QtWidgets.QPushButton(transferFile)
        self.pushButtonSelectFile.setGeometry(QtCore.QRect(140, 60, 112, 32))
        self.pushButtonSelectFile.setObjectName("pushButtonSelectFile")
        self.pushButtonTransferRDI = QtWidgets.QPushButton(transferFile)
        self.pushButtonTransferRDI.setGeometry(QtCore.QRect(140, 130, 112, 32))
        self.pushButtonTransferRDI.setObjectName("pushButtonTransferRDI")
        self.pushButtonTransferPVT = QtWidgets.QPushButton(transferFile)
        self.pushButtonTransferPVT.setGeometry(QtCore.QRect(140, 200, 112, 32))
        self.pushButtonTransferPVT.setObjectName("pushButtonTransferPVT")

        self.retranslateUi(transferFile)
        QtCore.QMetaObject.connectSlotsByName(transferFile)

    def retranslateUi(self, transferFile):
        _translate = QtCore.QCoreApplication.translate
        transferFile.setWindowTitle(_translate("transferFile", "Dialog"))
        self.pushButtonSelectFile.setText(_translate("transferFile", "选择文件"))
        self.pushButtonTransferRDI.setText(_translate("transferFile", "转换为.dat"))
        self.pushButtonTransferPVT.setText(_translate("transferFile", "转换为.pvt"))
