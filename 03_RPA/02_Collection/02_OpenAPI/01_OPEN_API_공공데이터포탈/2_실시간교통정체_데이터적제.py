# 실시간 고속도로 정체상황
# http://data.ex.co.kr/openapi/basicinfo/openApiInfoM?apiId=0406&serviceType=OPENAPI&keyWord=%EC%8B%A4%EC%8B%9C%EA%B0%84&searchDayFrom=2014.12.01&searchDayTo=2022.12.16&CATEGORY=&GROUP_TR=

import urllib.request
import datetime
import json
import time

url ="http://data.ex.co.kr/openapi/odtraffic/trafficAmountByCongest?key=test&type=json"
def get_df_info(json_data, records_root_name):
    column_list = []
    all_data = []
    is_first = True
    for record in json_data[records_root_name]:
        row_data_list = []
        for key, value in record.items():
            if is_first:
                column_list.append(key)
            row_data_list.append(value)
        all_data.append(row_data_list)
        is_first = False

    return column_list, all_data
def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
response_data = get_request_url(url)
if (response_data == None):
    print('No response')
else:
    raw_data = json.loads(response_data)

column_list, all_data = get_df_info(raw_data,'list')

print(column_list)
# ['routeName', 'routeNo', 'trafficAmout', 'conzoneId', 'conzoneName', 'stdDate', 'stdHour', 'vdsId', 'speed', 'shareRatio', 'timeAvg', 'grade', 'updownTypeCode']
column_list = []
print(all_data )