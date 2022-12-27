import cx_Oracle
import time
import datetime
from datetime import datetime,timedelta

def get_update_time_info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수

    day_hour = time.strftime("%H")
    day_min = time.strftime("%M")

    day_min_int = int(day_min)
    if 40 <= day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 40분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M")
        print("\n<<실시간 정보 업데이트를 실시합니다!!>>\n".center(30))

    else:
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 시간은 60분 단위 이므로 30분 미만은 30분을 빼고 60을 더한다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신정보 업데이트를 실시합니다!!>>\n".center(30))
    return day_time

def get_update_time_info2():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    now = datetime.now()

    if now.minute >= 40 and now.minute < 60:
        print(f"실시간: {now}")
        return now
    else:
        update_cycle_min = timedelta(minutes=40)
        lastest_time = now - update_cycle_min
        print(f"최신정보: {lastest_time}")
        return lastest_time

date_time = get_update_time_info2()

yyyymmdd = date_time.strftime('%Y%m%d')
hhmm = date_time.strftime('%H%M')

print(yyyymmdd, hhmm)
