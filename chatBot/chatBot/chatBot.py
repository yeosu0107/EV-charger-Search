import telepot

import data
import time
#gTTS 라이브러리 다운 후 임포트 해야함
from gtts import gTTS

stationList=[]
searchList=[]
searchList2=[]

namedic={}
nameLists=[]
station=data.ChargingStation(stationList)

bot=telepot.Bot('516302969:AAF-sYkOIWeIzvGFNzcDritqRmg9f4sNwZ8')

userList=[]


#mapHttp = 'https://maps.apple.com/maps?||='
mapHttp = 'http://mygeoposition.com/?q='
def getUserInfo(chat_id):
    userTable={}
    userTable['id']=chat_id
    userTable['state']='none'
    return userTable

def searchUserInfo(chat_id):
    if len(userList) is 0:
         tmp = getUserInfo(chat_id)
         userList.append(tmp)

    count=0
    index=0

    for i in userList:
        if chat_id == i['id']:
            count+=1
            break
        index+=1

    if(count==0):
        tmp = getUserInfo(chat_id)
        userList.append(tmp)

    return index

def getChargerInfo(list, chat_id, text):
    for i in list:
        tmp = text.split()
        for j in tmp:
            j=j.replace('의','')
            j=j.replace('에','')
            if j in i["충전소 명"]:
                 tmpData=i
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
    
                 stationData = "\t-충전소 정보-\n\n"\
                            "충전소 명 : {0}\n" \
                            "주소 : {1}\n" \
                            "충전기 타입 : {2}\n" \
                            "현재상태 : {3}\n" \
                            "갱신시간 : {4}\n".\
                            format(tmpData["충전소 명"], tmpData["주소"], pin, state, tmpData["시간"])
    
                 mymap=mapHttp
                 mymap+=str(tmpData["위도"]) + "," + str(tmpData["경도"])
    
                 bot.sendMessage(chat_id, stationData)
                 bot.sendMessage(chat_id, mymap)
                 return 1

    return 0

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    index = searchUserInfo(chat_id)

    import loc

    print(msg)

    if(content_type) == 'text':
        text=msg["text"]
        if(userList[index]['state']=='충전소검색'):
            result = getChargerInfo(searchList, chat_id, text)
            userList[index]['state']='none'
            if(result == 1):    
                return
        elif(userList[index]['state']=='충전소검색2'):
            result = getChargerInfo(searchList2, chat_id, text)
            userList[index]['state']='none'
            if(result == 1):    
                return

            #bot.sendMessage(chat_id, '입력한 충전소가 없습니다.')
        
        if(userList[index]['state']=='none'): 
            for i in loc.addr1:
                if i in text:
                    tmp=loc.addrSearch(i, text)
                    inputfi
                    if(tmp == "none"):
                        bot.sendMessage(chat_id, "구/군 까지 적어주셔야 더 정확한 검색이 가능합니다.")
                        #텍스트를 음성파일로 변환
                        tts = gTTS(text = tmptext, lang = 'ko')
                        #생성한 음성파일을 mp3파일로 저장
                        tts.save("tts_test.mp3")
                        #전송은 못함...
                        #bot.sendAudio(chat_id,"tts_test.mp3")

                    bot.sendMessage(chat_id, '검색 중...')

                    namedic=station.searchList(stationList, i, searchList)
                    
                    addition = loc.additionalSearch(i)
                    if(addition!="none"):
                        station.addSearchList(stationList, addition, searchList, namedic)

                    if(tmp != "none"):
                        namedic=station.searchList(searchList, tmp, searchList2)
                    
                    nameLists=list(namedic.keys())
                    tmplist=''
                    if len(nameLists) == 0:
                        bot.sendMessage(chat_id, '이 지역에는 충전소가 없습니다.')
                        return

                    for i in nameLists:
                        tmplist+='충전소 명 : ' + i + '\n'

                    bot.sendMessage(chat_id, tmplist)
                    bot.sendMessage(chat_id, '더 자세한 정보를 원하면 충전소 명을 입력해주세요.')

                    if(tmp == 'none'):
                        userList[index]['state']='충전소검색'
                    else:
                        userList[index]['state']='충전소검색2'

                    return
            bot.sendMessage(chat_id, '지역을 검색할 수 없습니다.')

    elif(content_type)=='location':
        mymap=mapHttp
        loc=msg["location"]
        mymap+=str(loc["latitude"]) + ',' + str(loc["longitude"])
        bot.sendMessage(chat_id, '위치기반 검색 명령은 아직 구현되지 않았습니다.')
        bot.sendMessage(chat_id, '입력한 위치 입니다.')
        bot.sendMessage(chat_id, mapHttp)
    elif(content_type) =='voice':
        bot.sendMessage(chat_id, '음성입력이 들어왔습니다')
    else:
        bot.sendMessage(chat_id, '텍스트와 위치만 처리할 수 있습니다.')
    

print(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)