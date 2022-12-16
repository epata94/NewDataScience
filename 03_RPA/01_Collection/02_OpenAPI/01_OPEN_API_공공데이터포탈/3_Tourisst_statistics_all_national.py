import urllib.request
import datetime
import json

# access_key= "aYk%2Fi2dkJ5CTB7ehuSJRPFPDwT3U96r25b%2B6MjwCrJJwGywnLR4qcln4%2BSR75IVpuNXbJLhrGiY2IedUR8A%2B4A%3D%3D"
access_key="VQI9j2eNsHPRzD9e%2BHNeiZ8hglSX6LYOQU5AuyvvJkOuB%2Bp9aMSEwYofVpWI0PmQInEHCpdZyo5GgzecUFJkWw%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" %(datetime.datetime.now(), url))
        return None

    #[CODE 1]
def getNatVisitor(yyyymm, nat_cd, ed_cd):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    # parameters = "?_type=json&serviceKey=" + access_key[2]
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def read_code_file():
    f = open('national_code_selected.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    code_list = []
    for line in lines:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        line = line.replace('\ufeff', '')
        code_list.append({'national_code': line.split("=")[0], 'KrName': line.split("=")[1]})
    f.close()
    return code_list

def main():
    jsonResult = []

    code_list = read_code_file()
    for code in code_list:
        national_code = code['national_code']
        krName = code['KrName']
        ed_cd = "E"
        nStartYear = 2015
        nEndYear = 2016

        total_Visit_num = 0
        for year in range(nStartYear, nEndYear):
            for month in range(11,13):
                yyyymm = "{0}{1:0>2}".format(str(year), str(month))
                jsonData = getNatVisitor(yyyymm, national_code, ed_cd)

                if(jsonData['response']['header']['resultMsg'] == 'OK' ):
                    iTotalVisit = jsonData['response']['body']['items']['item']['num']
                    total_Visit_num += int(iTotalVisit)

                    print('%s_%s:%s' %(krName, yyyymm, iTotalVisit))

        jsonResult.append({'nat_name': krName, 'nat_cd': national_code, 'total_Visit_cnt': total_Visit_num})
        jsonResult = sorted(jsonResult, key=lambda aa: aa['total_Visit_cnt'], reverse=True)

    with open('해외방문객정보_%d_%d_국가별 합.json' %(nStartYear, nEndYear-1), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()