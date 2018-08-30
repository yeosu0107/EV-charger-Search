import json
import data

#Google Cloud Function - DialogFlow 연동을 위한 기본 프레임
'''
def main(request):
    req = request.get_json(silent = True)

    returnVal = {}

    if req is None:
        returnVal["fulfillmentText"] = "ERROR"
    else:
        returnVal["fulfillmentText"] = "SUCCESS"
        action = req.get("result").get("parameters").get("location")
        returnVal["location"] = action

    return json.dumps(returnVal, ensure_ascii=False, indent="\t")
'''
stationList = []
searchList=[]
namedic = {}

station = data.ChargingStation(stationList)



def main(request):
    req = request.get_json(silent=True)

    returnVal = {}

    if req is None:
        returnVal["fulfillmentText"] = "ERROR"
        returnVal["fulfillmentMessages"] = "알수없는 메시지 입니다."
    else:
        location = req.get("queryResult").get("parameters").get("location")
        returnVal["fulfillmentText"] = HandleText(location)

    return json.dumps(returnVal, ensure_ascii=False, indent="\t")

def HandleText(msg):
    import loc
    for i in loc.addr1:
        if i in msg:
            tmp = loc.addrSearch(i, msg)

            namedic = station.searchList(stationList, i, searchList)
            addition = loc.additionalSearch(i)
            if (addition != "none"):
                station.addSearchList(stationList, addition, searchList, namedic)

            namelist = list(namedic.keys())

            tmptext = ''

            tmptext += "총 " + str(len(namelist)) + "개의 충전소가 검색되었습니다.\\n\\n"

            for name in namelist:
                tmptext += '충전소 명 : '+ name + '\\n'

            tmptext +="\\n"

            tmptext += "충전소 이름으로 검색을 하시면 더 자세한 정보를 얻을 수 있습니다."

            return tmptext

    return ''


