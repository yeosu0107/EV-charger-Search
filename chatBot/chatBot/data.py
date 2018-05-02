#-*- coding: utf-8 -*-
import urllib.request

from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree

server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"

def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(864)+'&pageNo='+str(1) +'&addr='
    request=server+data

    print(request)
    return request


def LoadPoint(item):
    dic = {}
    dic["충전소 명"] = item.find("csNm").text
    dic["주소"]=item.find("addr").text
    dic["충전기 타입"]=item.find("chargeTp").text
    #dic["cpName"]=item.find("cpNm").text
    dic["현재 상태"]=item.find("cpStat").text
    #dic["type2"]=item.find("cpTp").text
    dic["위도"]=item.find("lat").text
    dic["경도"]=item.find("longi").text
    dic["시간"]=item.find("statUpdateDatetime").text
    return dic


class ChargingStation:
    def __init__(self, station):
        url = urlBuilder(server, serviceKey)
        data = urllib.request.urlopen(url).read()


        #print(data)
        u = data.decode('utf-8',"replace")
        #print(u)
        #import re
        #trash=re.findall('\r\n.{0,10}\r\n', u)
        #print(trash)
        #for i in trash:
            #u=u.replace(i, "")
        #u=u.replace('\r\n',"")

        #u=u[4:]
        #print(u)


        tree = ElementTree.fromstring(u)
        # u = data.translate(None, b'\r\n')
        # print(u)
        # u=u.replace(m.,"")
        # u = u.replace("10000", "")
        # u = u.replace("c575", "")
        # print(data[6:32253])
        # tree = ElementTree.fromstring(data[6:32253])
        #tree=ElementTree.parse('tmpData.xml')


        itemElement = list(tree.iter("item"))

        for item in itemElement:
            item.find("addr").text
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