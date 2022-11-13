'''
반복문(for)

형식)
for 변수 in 열거형data :
    실행문
    실행문
    
제너레이터식 : 변수 in 열거형data(object)  
열거형data(iterable) : string,list,tuple,set,dict  
'''

# 문자열 열거형객체 이용
string = "홍길동"

# 1문자 -> 변수 넘김 : 3회
print(len(string)) # 3

for s in string : 
    print(s)

print() # line skip

# split -> 변수 넘김 : 3회
string = "나는 홍길동 입니다."
for s in string.split() : # sep=' '
    print(s) # 나는 홍길동 입니다.
     
print()

# list 열거형객체 이용
lstset = [1,2,3,4,5] # 1차원(vector)

for e in lstset :
    print('원소 : ', e)

help(range)
'''
range(stop) : 0~stop-1 정수 
range(start, stop) : start~stop-1 정수
range(start, stop, step) : start ~ stop, step 단위 증감
'''
    
num1 = range(10) # 0~4
print('num1 : ', num1) # range(0, 10)

num2 = range(1, 10)
print('num2 : ', num2) # range(1, 10)

num3 = range(1, 10, 2)
print('num3 :', num3) # range(1, 10, 2)

for n in num1 :
    print(n, end = ' ')
print()

for n in num2 :
    print(n, end = ' ')
print()

for n in num3 :
    print(n, end = ' ')

num2 = range(1,5) # 1~4
print('num2 : ', num2) # num2 :  range(1, 5)

num2 = list(num2)
print(num2) # [1, 2, 3, 4]

lst = list(range(1,101)) # 1 ~ 100
print('lst :', lst)
lst2 = [] # 빈list

for i in lst : # 100회 
    if i % 5 == 0 :
        print(i, end = ' ') 
        lst2.append(i)   
# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
print()
print(lst2)
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]


# 문) lst(1~100) 중에서 3의 배수만  lst3 추가/출력 
lst3 = []

for i in lst :
    if i % 3 == 0 :
        lst3.append(i)
        
print(lst3, end = ' ')        

print()

y = [1,0,2,1,0]# 정답 
y_pred = [1,0,2,0,0] # 예측치

size = len(y) 
print('size =', size) # size = 5(0~4)
acc = 0 # 분류정확도 

for idx in range(size) : # (0~4)
    fit = int(y[idx] == y_pred[idx]) # True/False -> int(1/0)
    acc += fit * 20 # 계산식 

print('분류정확도 : ', acc)
# 분류정확도 :  80
        
# 난수 모듈 
import random  # 난수 실수,정수 

r = random.random() # 0~1 난수 실수
print('r=', r) # r= 0.16949612953459392
r2 = random.randint(1,10) # 1~10 난수 정수
print('r2= ', r2) # r2=  2

# list에 자료 저장하기
lst = []
for i in range(10) : # 0~9
    r = random.randint(1,10) # 난수 
    lst.append(r) # 난수 저장
    
print(lst) # [3, 3, 7, 6, 4, 8, 8, 3, 4, 7]  * 0.25

# list에 자료 참조하기
for i in range(10) : # 0~9
    print(lst[i] * 0.25) # 난수 * 0.25


# 중첩 반복문
# 구구단 출력(2, 3, 5)
for i in [2, 3, 5]:
    # 바깥쪽 영역
    print('~~~ {}단 ~~~'.format(i))
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        # 안쪽 영역
        print('%d * %d = %d' % (i, j, i * j))

# 구구단 출력 : range() 함수 이용
for i in range(2, 10):
    # 바깥쪽 영역
    print('~~~ {}단 ~~~'.format(i))
    for j in range(1, 10):
        # 안쪽 영역
        print('%d * %d = %d' % (i, j, i * j))

'''
for 변수 in data1 :  -> 문장
    실행문 -> 문장 저장  
    for 변수 in data2: ->  단어 
        실행문 -> 단어 저장 
'''

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = [] # 문장 저장
words = [] # 단어 저장

for sen in string.split(sep = "\n") : # 문단 -> 문장
    sents.append(sen)
    for word in sen.split() : # 문장 -> 단어
        words.append(word)

        
print('문장 :',  sents)
print('문장수 :', len(sents))
print('단어 :', words)
print('단어수 :', len(words))

'''
문장 : ['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 35세 입니다.']
단어 : ['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
단어수 : 9
문장:단어 [{'나는 홍길동 입니다.': '나는'}, {'나는 홍길동 입니다.': '홍길동'}, {'나는 홍길동 입니다.': '입니다.'}, {'주소는 서울시 입니다.': '주소는'}, {'주소는 서울시 입니다.': '서울시'}, {'주소는 서울시 입니다.': '입니다.'}, {'나이는 35세 입니다.': '나이는'}, {'나이는 35세 입니다.': '35세'}, {'나이는 35세 입니다.': '입니다.'}]
'''
        
    










