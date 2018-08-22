#-*- coding: utf-8 -*-
import urllib.request

from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree
from datetime import datetime

server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"

def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(864)+'&pageNo='+str(1) +'&addr='
    request=server+data

    print(request)
    return request


def LoadPoint(item):
    dic = {}

    if item.find("csNm") != None:
        dic["충전소 명"] = item.find("csNm").text
    else:
        dic["충전소 명"] = "UnknownName"

    if item.find("addr") != None:
       dic["주소"] = item.find("addr").text
    else:
        dic["주소"] = dic["충전소 명"]

    if item.find("chargeTp") != None:
        dic["충전기 타입"] = item.find("chargeTp").text
    else:
        dic["충전기 타입"] = 1

    if item.find("cpStat") != None:
        dic["현재 상태"] = item.find("cpStat").text
    else:
        dic["현재 상태"] = -1

    if item.find("lat") != None:
        dic["위도"] = item.find("lat").text
    else:
        dic["위도"] = -1

    if item.find("longi") != None:
        dic["경도"] = item.find("longi").text
    else:
        dic["경도"] = -1

    if item.find("statUpdateDatetime") !=None:
        dic["시간"] = item.find("statUpdateDatetime").text
    else:
        dic["시간"] = datetime.now()

    return dic


class ChargingStation:
    def __init__(self, station):
        url = urlBuilder(server, serviceKey)
        data = urllib.request.urlopen(url).read()

        u = data.decode('utf-8',"replace")

        tree = ElementTree.fromstring(u)
        #u = data.translate(None, b'\r\n')
        # print(u)
        #u=u.replace(m.,"")
        #u = u.replace("10000", "")
        #u = u.replace("c575", "")
        # print(data[6:32253])
        # tree = ElementTree.fromstring(data[6:32253])
        #tree=ElementTree.parse('tmpData.xml')


        itemElement = list(tree.iter("item"))

        for item in itemElement:
            tmp = LoadPoint(item)
            station.append(tmp)


    def printList(self, station):
        for i in station:
            print(i)

    def searchList(self, station, addr, list):
        list.clear()
        dic={}

        for i in station:
            if addr in i["주소"]:
                list.append(i)
                dic[i["충전소 명"]] = i

        return dic

    def addSearchList(self, station, addr, list, dic):
        for i in station:
            if addr in i["주소"]:
                list.append(i)
                dic[i["충전소 명"]] = i


    def searchList2(self, station, name, list):
        list.clear()

        for i in station:
            if name in i["충전소 명"]:
                list.append(i)

    def searchDic(self, station, addr):
        dic={}
        for i in station:
            if addr in i["주소"]:
                dic[i["충전소 명"]] = i

        return dic