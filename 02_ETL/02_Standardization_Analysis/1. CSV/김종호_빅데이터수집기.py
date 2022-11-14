#김종호
import urllib.request
import json
import csv

access_key="OjVaWhKvKRU611576tYa84MVFG%2FER5aHq6b%2BjMgTula8AGzrXEZ4vJ%2Fw%2FYKMhB7AZjyAS%2B%2B9Z%2FG%2BccWH%2FceW4Q%3D%3D"
output_file = '대구상권면적조회.csv'

csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
header_list = ['signguNm','mainTrarNm','trarNo','trarArea']
filewriter.writerow(header_list)

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("Url Request Success")
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("Error for URL:%s"%(url))
        return None

def get_business_area(nPagenum):
    divId = "signguCd"
    key = "27140"
    end_point="http://apis.data.go.kr/B553077/api/open/sdsc/storeZoneInAdmi"

    parameters = "?divId="+divId
    parameters += "&key="+key
    parameters += "&type=json&ServiceKey="+access_key+"&numOfRows=20"

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    nPagenum = 1

    while True:
        jsonData = get_business_area(nPagenum)
        nTotal = jsonData['body']['items']


        for a in nTotal:
            signguNm = a['signguNm']
            mainTrarNm = a['mainTrarNm']
            trarNo = a['trarNo']
            trarArea = a['trarArea']
            if signguNm != None and mainTrarNm != None and trarNo != None and trarArea != None :
                alllist = [signguNm,mainTrarNm,trarNo,trarArea]
                filewriter.writerow(alllist)

        if (20 < len(nTotal)):
            break

        else:
            break


if __name__ == '__main__':
    main()
    csv_out_file.close()