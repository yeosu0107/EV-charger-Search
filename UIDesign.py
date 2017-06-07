# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic

import Data
#import webView as w


stationList=[]
searchList=[]
searchList2=[]
namedic={}
nameLists=[]
station=Data.ChargingStation(stationList)

qtCreatorFile = "UIDesign.ui"

#html=w.maphtml


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#map="http://map.daum.net/link/map/"
#basemap="http://www.ev.or.kr/portal/localMonitor?sido=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C"
map="http://mygeoposition.com/?q="
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        #self.webView.setHtml(html)

        #self.webView.setUrl(QtCore.QUrl(basemap))
        self.show()
        self.textEdit.setReadOnly(True)
        self.search.clicked.connect(self.Search)
        self.comboBox.currentIndexChanged.connect(self.setcomboIndex)
        self.comboBox2.currentIndexChanged.connect(self.printInfo)

    def Search(self):
        add = self.lineEdit.text()
        namedic = station.searchList(stationList, add, searchList)
        nameLists=list(namedic.keys())
        print(nameLists)

        self.setComboBox(nameLists)
        #self.setComboBox2()
        #self.printInfo()

    def SearchSList(self, name):
        searchList2.clear()
        for item in searchList:
            if name in item["충전소 명"]:
                searchList2.append(item)

    def setComboBox(self, nameLists):
        self.comboBox.clear()
        for item in nameLists:
            self.comboBox.addItem(item)

    def setComboBox2(self, name):
        self.comboBox2.clear()
        for item in searchList2:
            self.comboBox2.addItem(item["충전소 명"])

    def setcomboIndex(self):
        index = self.comboBox.currentIndex()
        if index is -1:
            return
        item = self.comboBox.itemText(index)
        self.SearchSList(item)
        self.setComboBox2(item)


    def printInfo(self):
        index = self.comboBox2.currentIndex()
        if index is -1:
            return
        tmpData = searchList2[index]

        if tmpData["현재 상태"] is 0 or 40:
            state="충전 대기"
        elif tmpData["현재 상태"] < 16:
            state="충전중"
        else:
            state="고장"

        if tmpData["충전기 타입"] is 1:
            pin="완속"
        else:
            pin="급속"


        stationData = "\t      - 충전소 정보 -\n\n"\
                      "충전소 명 : {0}\n" \
                      "주소 : {1}\n" \
                      "충전기 타입 : {2}\n" \
                      "위도 : {3}\n" \
                      "경도 : {4}\n" \
                      "현재상태 : {5}\n" \
                      "갱신시간 : {6}\n".format(tmpData["충전소 명"], tmpData["주소"], pin,
                                            tmpData["위도"], tmpData["경도"], state, tmpData["시간"])
        #tmap=map+tmpData["충전소 명"]+","+tmpData["위도"]+","+tmpData["경도"]
        tmap = map  + tmpData["위도"] + "," + tmpData["경도"]
        #print(tmap)
        self.webView.setUrl(QtCore.QUrl(tmap))
        #print(stationData)
        self.textEdit.setText(stationData)


app = QApplication(sys.argv)
xwin = MyApp()
app.exec()
