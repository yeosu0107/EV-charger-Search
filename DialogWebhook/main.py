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
    else:
        returnVal["fulfillmentText"] = "SUCCESS"
        location = req.get("result").get("parameters").get("location")
        returnVal["result"] = HandleText(location)

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
            for name in namelist:
                tmptext += '충전소 명 : '+ name + '\n'

            return tmptext

    return ''


