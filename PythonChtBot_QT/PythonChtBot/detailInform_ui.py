# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailInform.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_ch_naem = QtWidgets.QLabel(self.centralwidget)
        self.label_ch_naem.setGeometry(QtCore.QRect(70, 50, 300, 31))
        self.label_ch_naem.setObjectName("label_ch_naem")
        self.label_ads = QtWidgets.QLabel(self.centralwidget)
        self.label_ads.setGeometry(QtCore.QRect(70, 90, 300, 31))
        self.label_ads.setObjectName("label_ads")
        self.label_ch_type = QtWidgets.QLabel(self.centralwidget)
        self.label_ch_type.setGeometry(QtCore.QRect(70, 140, 300, 31))
        self.label_ch_type.setObjectName("label_ch_type")
        self.label_nowstate = QtWidgets.QLabel(self.centralwidget)
        self.label_nowstate.setGeometry(QtCore.QRect(70, 190, 300, 31))
        self.label_nowstate.setObjectName("label_nowstate")
        self.label_updateT = QtWidgets.QLabel(self.centralwidget)
        self.label_updateT.setGeometry(QtCore.QRect(70, 240, 300, 31))
        self.label_updateT.setObjectName("label_updateT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Station Detail Inform"))
        self.label_ch_naem.setText(_translate("MainWindow", "충전소명"))
        self.label_ads.setText(_translate("MainWindow", "주소"))
        self.label_ch_type.setText(_translate("MainWindow", "충전기 타입"))
        self.label_nowstate.setText(_translate("MainWindow", "현재 상태"))
        self.label_updateT.setText(_translate("MainWindow", "갱신 시간"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

