############################
### 한글 텍스트 전처리
############################

# 레이블(label) 분류
label = ['spam', 'ham', 'spam', 'ham', 'ham']
target = [ 1 if x == 'spam' else 0 for x in label] # dummy 변수
print('target : ', target)
# target :  [1, 0, 1, 0, 0]


# 한글 텍스트 전처리
from re import findall, sub

# 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

# 1. 소문자 변경
string = "ABCd"
print(string.lower())  # abcd
print(string.upper())  # ABCD
# print(texts.lower()) - list 사용 불가

# list 내포 : 변수 = [실행문 for 변수 in 열거형data]
texts_re1 = [t.lower() for t in texts]
print('texts_re1 :', texts_re1)

# 2. 숫자 제거
# list 내포 : [실행문 for 변수 in 열거형객체], 실행문(숫자 제외 -> 문자결합)
texts_re2 = [sub("[0-9]", '', text) for text in texts_re1]
print('texts_re2 :', texts_re2)

# 3. 문장부호 제거
texts_re3 = [sub('[,.?!:;]', '', text) for text in texts_re2]
print('texts_re3 :', texts_re3)

# 4. 특수문자 제거 : re.sub() 이용
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('texts_re4 :', texts_re4)

# 5. 영문 제거
texts_re5 = [''.join(findall("[^a-z]", text)) for text in texts_re4]
print('texts_re5 :', texts_re5)

# 6. 공백제거 제거 : 'abtta a' -> 'abtta', 'a' -> 'abttaa'
texts_re6 = [' '.join(text.split()) for text in texts_re5]  # 공백기준 split -> join
print('texts_re6 :', texts_re6)
# ['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
