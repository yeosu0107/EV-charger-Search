# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

import Data

stationList=[]
searchList=[]
station=Data.ChargingStation(stationList)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 31, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(690, 30, 75, 23))
        self.search.setObjectName("search")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 80, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(560, 130, 201, 401))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.editingFinished.connect(self.search.click)
        self.search.clicked.connect(self.Search)
        self.comboBox.currentIndexChanged.connect(self.printInfo)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.search)
        MainWindow.setTabOrder(self.search, self.comboBox)

        self.textEdit.setReadOnly(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "검색"))

    def Search(self):
        add = self.lineEdit.text()
        station.searchList(stationList, add, searchList)
        #station.printList(searchList)
        self.setComboBox()
        self.printInfo()

    def setComboBox(self):
        self.comboBox.clear()
        for item in searchList:
            self.comboBox.addItem(item["충전소 명"])

    def printInfo(self):
        index=self.comboBox.currentIndex()
        if index is -1:
            return
        tmpData=searchList[index]
        stationData="충전소 명 : {0}\n" \
                    "주소 : {1}\n" \
                    "충전기 타입 : {2}\n" \
                    "위도 : {3}\n" \
                    "경도 : {4}\n" \
                    "현재상태 : {5}\n" \
                    "갱신시간 : {6}\n".format(tmpData["충전소 명"], tmpData["주소"], tmpData["충전기 타입"],
                                        tmpData["위도"], tmpData["경도"], tmpData["현재 상태"], tmpData["시간"])
        print(stationData)
        self.textEdit.setText(stationData)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

