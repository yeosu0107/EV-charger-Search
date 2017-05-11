from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #table 쓰기위한 import 형식
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
# "http://maps.google.com":http://maps.google.com
maphtml = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>지도 생성하기</title>
    
</head>
<body>
<!-- 지도를 표시할 div 입니다 -->
<div id="map" style="width:100%;height:700px;"></div>

<script type="text/javascript" src="http://apis.daum.net/maps/maps3.js?apikey=86b3d296fd406d6de445c8b66d2479c8"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new daum.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new daum.maps.Map(mapContainer, mapOption); 
</script>
</body>
</html>
'''
class Browser(QApplication):
    def __init__(self):
        QApplication.__init__(self, [])
        self.window = QWidget()
        self.window.setWindowTitle("Daum Map Api");

        self.web = QWebView(self.window)
        self.web.setMinimumSize(800,800)
        self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.web.setHtml(maphtml)

        self.text = QTextEdit(self.window)

        self.layout = QVBoxLayout(self.window)
        self.layout.addWidget(self.web)
        self.layout.addWidget(self.text)

        self.window.show()
        self.exec_()

    @pyqtSlot(float, float, int)
    def polygoncomplete(self, lat, lng, i):
        if i == 0:
            self.text.clear()
        self.text.append("Point #{} ({}, {})".format(i, lat, lng))

Browser()