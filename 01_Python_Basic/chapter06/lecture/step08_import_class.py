#import builtins

# (1) builtins모듈 내장 클래스
lst = [1,3,5]
for i, c in enumerate(lst) :
    print('색인 : ', i, end=', ')
    print('내용 :', c)

dit = {'name' : '홍길동', 'job': '회사원', 'addr':'서울시'}
for i, k in enumerate(dit) :
    print('색인 : ', i, end=', ')
    print('키 :', k, end=', ')
    print('값 :', dit[k])

# (2) datatime모듈 내장클래스
import  datetime
from datetime import date, time # from 모듈 import 내장 클래스

help(date)
'''
Help on class date in module datetime:
class date(builtins.object)
 |  date(year, month, day) --> date object
'''

today = date(2019, 10, 23) # 생성자 -> object
print(today) # 2019-10-23

# object.member : 변수
print(today.year) # 2019
print(today.month) # 10
print(today.day) # 23

# object.member() : 함수 
w = today.weekday() # Monday == 0 ... Sunday == 6
print('요일 정보 : ', w) # 요일 정보 :  0(월)~6(일)


help(time)
'''
Help on class time in module datetime:

class time(builtins.object)
 |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
'''

currTime = time(21,4,30)
'''
datetime.time(0, 0) ~ datetime.time(23, 59, 59, 999999)
'''
print(currTime) # 21:04:00

print(currTime.hour) # 21
print(currTime.minute) # 4
print(currTime.second) # 0

isoTime = currTime.isoformat() # HH:MM:SS
print(isoTime) # 21:04:00
