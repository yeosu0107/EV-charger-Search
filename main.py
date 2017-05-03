import urllib.request
from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree

server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"


def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(30)+'&pageNo='+str(1)
    request=server+data
    return request

def LoadPoint(item):
    dic = {}
    dic["name"] = item.find("csNm").text
    dic["addr"]=item.find("addr").text
    dic["type"]=item.find("chargeTp").text
    dic["cpName"]=item.find("cpNm").text
    dic["state"]=item.find("cpStat").text
    dic["type2"]=item.find("cpTp").text
    dic["lat"]=item.find("lat").text
    dic["longi"]=item.find("longi").text

    return dic

url=urlBuilder(server, serviceKey)

data=urllib.request.urlopen(url).read()

tree=ElementTree.fromstring(data)
itemElement=list(tree.iter("item"))


list=[]

for item in itemElement:
    a1=item.find("addr").text
    tmp = LoadPoint(item)
    list.append(tmp)

for i in list:
    print(i)