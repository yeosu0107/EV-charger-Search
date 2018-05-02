addr1=['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', \
    '경기', '강원', '제주',\
    '충청북도', '충청남도', '전라남도', '전라북도', '경상남도', '경상북도', \
    '충북', '충남', '전남', '전북', '경남', '경북']

seoul=['종로', '중', '용산', '성동', '광진', '동대문', '중랑', '성북', '강북', '도봉', \
    '노원', '은평', '서대문', '마포', '양천', '강서', '구로', '금천', '영등포', '동작', '관악', \
    '서초', '강남', '송파', '강동']

Busan = ['중','서','동','영도','부산진','동래','남','북','강서','해운대','사하',
    '금정','연제','수영','사상','기장']

Daegu=['중','동','서','남','북','수성','달서','달성']

Incheon=['중','동','남','연수','남동','부평','계양','서','강화','옹진']

Gwangju=['동','서','남','북','광산']


Daejeon=['동','중','서','유성','대덕']


Ulsan=['중','남','동','북','울주']


Saejong=['세종특별']

Gweonggi=['수원','성남','안양','안산','용인','광명','평택',
           '과천','오산','시흥','군포','의왕','하남','이천','안성','김포',
           '화성','광주','여주','부천','양평','고양','의정부','동두천','구리',
           '남양주','파주','양주','포천','연천','가평']

Gangwon=['춘천','원주','강릉','동해','태백','속초','삼척','홍천','횡성',
           '영월','평창','정선','철원','화천','양구','인제','고성','양양']

ChungCheongBukdo=['청주','충주','제천','보은','옥천','영동','진천','괴산',
                  '괴산','음성','단양','증평']

ChungCheongNamdo=['천안','공주','보령','아산','서산','논산','계룡','당진',
                  '금산','부여','서천','청양','홍성','예산','태안']


JeollaBukdo = ['전주','군산','익산','정읍','남원','김제','완주','진안','무주',
               '장수','임실','순창','고창','부안']

JeollaNamdo=['목포','여수','순천','나주','광양','담양','곡성','구례','고흥','보성',
             '화순','장흥','강진','해남','영암','무안','함평','영광','장성','완도',
             '진안','ㄴ신안']

        
GyeongSangBukdo = ['포항','경주','김천','안동','구미','영주','영천','상주','문경','경산',
                   '경산','군위','의성','청송','영양','영덕','청도','고령','성주','칠곡',
'예천','봉화','울진','울릉']

GyeongSangNamdo=['창원','진주','통영','사천','김해','밀양','거제','양산','의령',
                 '함안','창녕','고성','남해','하동','산청','함양','거창','합천']

Jeju=['제주']

def addrSearch(addr, text):
    tmp = "none"
    if(addr == "서울"):
        tmp = searchSystem(text, seoul)
    elif(addr == "부산"):
        tmp = searchSystem(text, Busan)
    elif(addr == "대구"):
        tmp = searchSystem(text, Daegu)
    elif(addr == "인천"):
        tmp = searchSystem(text, Incheon)
    elif(addr == "광주"):
        tmp = searchSystem(text, Gwangju)
    elif(addr == "대전"):
        tmp = searchSystem(text, Daejeon)
    elif(addr == "울산"):
        tmp = searchSystem(text, Ulsan)
    elif(addr == "세종"):
        #tmp = searchSystem(text, Saejong)
        tmp = "세종특별"
    elif(addr == "경기"):
        tmp = searchSystem(text, Gweonggi)
    elif(addr == "강원"):
        tmp = searchSystem(text, Gangwon)
    elif(addr == "제주"):
        tmp = searchSystem(text, Jeju)
    elif(addr == "충북" or addr == "충청북도"):
        tmp = searchSystem(text, ChungCheongBukdo)
    elif(addr == "충남" or addr == "충청남도"):
        tmp = searchSystem(text, ChungCheongNamdo)
    elif(addr == "전남" or addr == "전라남도"):
        tmp = searchSystem(text, JeollaNamdo)
    elif(addr == "전북" or addr == "전라북도"):
        tmp = searchSystem(text, JeollaBukdo)
    elif(addr == "경남" or addr == "경상남도"):
        tmp = searchSystem(text, GyeongSangNamdo)
    elif(addr == "경북" or addr == "경상북도"):
        tmp = searchSystem(text, GyeongSangBukdo)

    return tmp

def searchSystem(text, list):
    for i in list:
        if i in text:
            return i
    return "none"

def additionalSearch(addr):
    if(addr == "충남"):
        return "충청남도"
    elif(addr == "충북"):
        return "충청북도"
    elif(addr == "충청남도"):
        return "충남"
    elif(addr == "충청북도"):
        return "충북"

    elif(addr == "경남"):
        return "경상남도"
    elif(addr == "경북"):
        return "경상북도"
    elif(addr == "경상남도"):
        return "경남"
    elif(addr == "경상북도"):
        return "경북"

    elif(addr == "전남"):
        return "전라남도"
    elif(addr == "전북"):
        return "전라북도"
    elif(addr == "전라북도"):
        return "전북"
    elif(addr == "전라남도"):
        return "전남"
    else:
        return "none"