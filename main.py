import urllib.request
from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree

server='http://openapi.kepco.co.kr/service/evInfoService/getEvSearchList'
serviceKey="4lmWp814ERUDuydXPhoe%2FcCMA8%2BAdBGDoCEnTrCRixmHXdNe63pJDHI9NJueNefS729hoLtHk67YiFbm6rOzEw%3D%3D"


def urlBuilder(server, key):
    data='?'+'serviceKey='+key+'&numOfRows='+str(10)+'&pageNo='+str(1)
    request=server+data
    return request

url=urlBuilder(server, serviceKey)

data=urllib.request.urlopen(url).read()

tree=ElementTree.fromstring(data)
itemElement=list(tree.iter("item"))

dic={}

for item in itemElement:
    a1=item.find("addr").text
    dic[a1]=1

for i in dic:
    print(i)