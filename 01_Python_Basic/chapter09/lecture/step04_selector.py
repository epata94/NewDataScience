'''
- 선택자(selector) 이용 내용 추출하기
  -> 웹 문서 디자인(css)용으로 사용
  -> 선택자 : id(#), class(.) 
  -> soup.select_one('#id') : 하나의 요소 추출 
  -> soup.select('.class') : 여러 개의 요소 추출 
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기 
file = open('chapter09/data/html03.html', mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')

# 3. 선택자 이용 태그 내용 가져오기 
# 1) id 선택자
print('>> table 선택자 <<') 
table = html.select_one('#tab') # <table id='tab'>
print(table) # 1개 element 

# [문제] th 내용 출력 
ths = table.find_all('th')
for th in ths :
    print(th.string)
     
print('>> 선택자 & 계층 <<')
ths = html.select('#tab > tr > th')
print(ths) # list
# [<th id="id"> 학번 </th>, <th id="name"> 이름 </th>, <th id="major"> 학과 </th>, <th id="email"> 이메일 </th>]

for th in ths :
    print(th.string)

# 2) class 선택자 : tr tag class='odd'
trs = html.select("#tab > .odd")  # 홀수 행
print(trs)

print('### tr > td 출력 ### ')
for tr in trs : # 행 : 2회 반복 
    #print(tr)
    tds = tr.find_all('td')
    for td in tds : # 열 
        print(td.string)
        
# 4) 태그[속성=값] 찾기 
trs = html.select("tr[class=odd]")
print(trs)

print('### tr > td 출력 ### ')
for tr in trs : # 행 : 2회 반복 
    #print(tr)
    tds = tr.find_all('td')
    for td in tds : # 열 
        print(td.string)
        
    
'''
examp02
'''

