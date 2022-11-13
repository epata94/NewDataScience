'''
1. tag 이름으로 찾기 
2. find('tag')함수 찾기 
'''

from bs4 import BeautifulSoup

# 1. 로컬 서버 파일 읽기 
file = open('chapter09/data/html01.html', mode='r', encoding='utf-8')
text = file.read()
print(text)

# 2. html 파싱
html = BeautifulSoup(text, 'html.parser')
print(html)

# 3. 태그 내용 가져오기 

# 1) tag 이용 
h1 = html.html.body.h1 # 계층 접근
print('h1 : ', h1.string) # h1 :   시멘틱 태그 ?

# 2) find()함수 : 태그 찾기 
h2 = html.find('h2')
print('h2 : ', h2.string) # h2 :   주요 시멘틱 태그

# 3) find_all('tag')
lis = html.find_all('li') # list 반환
print(lis) 
# [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>, <li> section : 웹 문서를 장(chapter)을 볼 때 절을 구분하는 태그</li>, <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>, <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>]

for li in lis :
    print(li.string)
'''
header : 문서의 머리말(사이트 소개, 제목, 로그 )
nav : 네이게이션(메뉴) 
section : 웹 문서를 장(chapter)을 볼 때 절을 구분하는 태그
aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) 
footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) 
'''    

'''
examp01
'''