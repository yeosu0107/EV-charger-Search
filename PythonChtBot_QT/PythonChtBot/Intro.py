import sys
import data
import time

import InputCity_ui
import LocationEVInform_ui

import pyttsx3
import speech_recognition as sr
import detailInform_ui

#from gtts import gTTS

from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #table 쓰기위한 import 형식 
from PyQt5 import sip 



stationList=[]
searchList=[]
searchList2=[]

namedic={}
nameLists=[]

textList = []

station = data.ChargingStation(stationList)

#현재 사용자 상태
#none / 충전소검색 / 충전소검색2
userState='none'

g_location=""
g_ChargeStationName=[]
g_stationData={}

locationEVinform = []
stationEVInform = []


class LocationEVInform(QMainWindow):
    def __init__(self):
        super().__init__();
        self.EV_LocationEVinform_ui = LocationEVInform_ui.Ui_MainWindow()
        self.column_headers = ['충전소명','지역']
        self.column_idx_lookup = {'충전소명': 0, '지역': 1}

        self.EV_LocationEVinform_ui.setupUi(self);
        self.EV_LocationEVinform_ui.tableWidget.setHorizontalHeaderLabels(self.column_headers)
        self.EV_LocationEVinform_ui.tableWidget.setRowCount(len(g_ChargeStationName))
        self.dictionary={}

    def maketablewithdict(self):
        for L in g_ChargeStationName:
            self.dictionary[L]=g_location
        
        for i in range(len(g_ChargeStationName)):
                self.EV_LocationEVinform_ui.tableWidget.setItem(i,0,QTableWidgetItem(g_ChargeStationName[i]))
        for i in range(len(g_ChargeStationName)):
                self.EV_LocationEVinform_ui.tableWidget.setItem(i,1,QTableWidgetItem(g_location))
       
            
        self.EV_LocationEVinform_ui.tableWidget.resizeColumnsToContents()
        self.EV_LocationEVinform_ui.tableWidget.resizeRowsToContents()



        
class StationEVInform(QMainWindow):
    def __init__(self,parent=None):
        super(StationEVInform,self).__init__(parent);

        self.EV_detailInform_ui = detailInform_ui.Ui_MainWindow()
        self.EV_detailInform_ui.setupUi(self)

    def ShowDetailInform(self):

        self.EV_detailInform_ui.label_ch_naem.setText("충전소명: %s" %g_stationData["충전소 명"]);
        self.EV_detailInform_ui.label_ads.setText("주소: %s" %g_stationData["주소"]);
        
        self.EV_detailInform_ui.label_ch_type.setText("충전기 타입: %s" %g_stationData["충전기 타입"]);
        self.EV_detailInform_ui.label_nowstate.setText("현재상태: %s" %g_stationData["현재상태"]);
        self.EV_detailInform_ui.label_updateT.setText("갱신시간: %s" %g_stationData["갱신시간"]);

   



class InputCity(QMainWindow):


    def __init__(self):
        super().__init__()
        self.EV_ui = InputCity_ui.Ui_MainWindow()
        self.EV_ui.setupUi(self)
        self.EV_ui.pushButton.clicked.connect(self.InputCitybyKeyoardWriting_btn_clicked)
        self.EV_ui.pushButton_2.clicked.connect(self.voice_btn_clicked)

        global locationEVinform
        global stationEVInform
        locationEVinform = LocationEVInform()
        stationEVInform = StationEVInform()
        #self.EV_LocationEVinform_ui.show();
        
    def VoicetoText(self):
        r = sr.Recognizer() 
        r.energy_threshold = 500
        
        QMessageBox.question(self, 'Speaking', '찾고자하는 지역을 말하세요',  QMessageBox.Yes, QMessageBox.Yes)
        with sr.Microphone() as source:
            audio = r.record(source,duration=5)



        try:  
           clientSpeakLocation_str=r.recognize_google(audio,language='ko-KR');
          #a= r.recognize_google(audio,language='ko-KR')
           self.handleText(clientSpeakLocation_str)
         
        except sr.UnknownValueError:  
           QMessageBox.question(self, 'SpeakingError', '무슨 말인지 못 알아 들었습니다.',  QMessageBox.Yes, QMessageBox.Yes)
           #print("Google could not understand audio")  
    
        except sr.RequestError as e:  
           print("Google error; {0}".format(e)) 

        #return clientSpeakLocation_str


    def makeVoiceFile(self,text):

        #tts = gTTS(text, lang = 'ko')
        ##생성한 음성파일을 mp3파일로 저장
        #tts.save("tts_test.mp3")

        self.EV_ui.pushButton.setEnabled(False);   
        self.EV_ui.pushButton_2.setEnabled(False)
        engine = pyttsx3.init();
        engine.say(text);
        engine.runAndWait() ;
        self.EV_ui.pushButton.setEnabled(True);
        self.EV_ui.pushButton_2.setEnabled(True)
        
        return
    def InputCitybyKeyoardWriting_btn_clicked(self):
        self.handleText(self.EV_ui.lineEdit.text())

    def voice_btn_clicked(self):
        self.EV_ui.pushButton_2.setEnabled(False)
        self.EV_ui.pushButton.setEnabled(False);   
        self.VoicetoText();
        self.EV_ui.pushButton_2.setEnabled(True)
        self.EV_ui.pushButton.setEnabled(True);

    def pushText(self,text):
        textList.append(text)
        return

    def getChargerInfo(self,list, text):
        for i in list:
            tmp = text.split()
            for j in tmp:
                j = j.replace('의','')
                j = j.replace('에','')
                if j in i["충전소 명"]:
                     tmpData = i
                     if tmpData["현재 상태"] is 0 or 40:
                        state = "충전 대기"
                     elif tmpData["현재 상태"] < 16:
                        state = "충전중"
                     else:
                        state = "고장"
    
                     if tmpData["충전기 타입"] is 1:
                        pin = "완속"
                     else:
                        pin = "급속"
    
                     stationData = "\t-충전소 정보-\n\n"\
                                "충전소 명 : {0}\n" \
                                "주소 : {1}\n" \
                                "충전기 타입 : {2}\n" \
                                "현재상태 : {3}\n" \
                                "갱신시간 : {4}\n".\
                                format(tmpData["충전소 명"], tmpData["주소"], pin, state, tmpData["시간"])

                    
                     g_stationData["충전소 명"]         = tmpData["충전소 명"]
                     g_stationData["주소"]                = tmpData["주소"]
                     g_stationData["충전기 타입"]      = pin
                     g_stationData["현재상태"]          = state
                     g_stationData["갱신시간"]          = tmpData["시간"]
                     #mymap=mapHttp
                     #mymap+=str(tmpData["위도"]) + "," + str(tmpData["경도"])
                     tmptxt = "다음은 "+tmpData["충전소 명"]+"의 정보 입니다"
                     self.makeVoiceFile(tmptxt);
                     #self.pushText(stationData)
                     print(stationData)
                     
                     stationEVInform.ShowDetailInform()
                     stationEVInform.show()
                     
                     #self.EV_LocationEVinform_ui.show()
                     return 1

        return 0

    def handleText(self,msg): 
        import loc
        global userState
        global textList
        global g_location
        global g_ChargeStationName       
        global locationEVinform

        locationEVinform.destroy()
        stationEVInform.destroy()

        if(userState == '충전소검색'):
            result = self.getChargerInfo(searchList, msg)
            userState = 'none'
            if(result == 1):
               return
        elif(userState == '충전소검색2'):
            result = self.getChargerInfo(searchList2, msg)
            userState = 'none'
            if(result == 1):    
               return

        if(userState == 'none'):
            for i in loc.addr1:
                g_location = i;
                if i in msg:
                    tmp = loc.addrSearch(i, msg)
                    if(tmp == 'none'):
                        txt01 = "구 군까지 입력해야 더 정확한 검색이 가능합니다."
                        self.makeVoiceFile(txt01);
                        #self.pushText(txt01)
                        
                    txt02 = "검색 중입니다"
                        #self.pushText(txt02)
                    self.makeVoiceFile(txt02);
                    namedic = station.searchList(stationList, i, searchList)
                    
                    addition = loc.additionalSearch(i)
                    if(addition != "none"):
                        station.addSearchList(stationList, addition, searchList, namedic)
                    
                    if(tmp != "none"):
                        namedic = station.searchList(searchList, tmp, searchList2)
                        
                    g_ChargeStationName = list(namedic.keys())
                    tmplist = ''
                    if len(g_ChargeStationName) == 0:
                        txt03 = "이 지역에는 충전소가 없습니다."
                        #self.pushText(txt03)
                        self.makeVoiceFile(txt03);
                        return
                    #else:
                     #   self.makeVoiceFile("찾은충전소");

                    for name in g_ChargeStationName:
                        tmplist += '충전소 명 : ' + name + '\n'
                    

                    print(tmplist)

                    #검색한 지역들의 모든 충전소들을 보여줍시다
                    locationEVinform = LocationEVInform()
                    locationEVinform.maketablewithdict()

                    locationEVinform.show()
                    
                    txt04 = "말씀하신 지역에 있는 모든 충전소를 조회했습니다. 더 자세한 정보를 원하면 충전소 명을 입력해 주세요"
                    self.makeVoiceFile(txt04);
                    
                    
                    if(tmp == 'none'):
                        userState = '충전소검색'
                    else:
                        userState = '충전소검색2'
                    return
            txt00 = "지역을 검색할 수 없습니다"       
            #QMessageBox.question(self, 'Search Error', txt00,  QMessageBox.No, QMessageBox.No)
            self.makeVoiceFile(txt00);  