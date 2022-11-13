'''
1. news Crawling
  url : http://media.daum.net
2. pickle save
  binary file save 
'''

import urllib.request as req
from bs4 import BeautifulSoup

url = "http://media.daum.net"

# (1) url 요청 -> html source
res = req.urlopen(url)
source = res.read()
        
# (2) 소스 디코딩
source = source.decode("utf-8") # charset="utf-8"

# (3) html 파싱
html = BeautifulSoup(source, 'html.parser')
#print(soup)

# (4) tab[속성=값] 요소 추출
atags = html.select('a[class=link_txt]')
#print(atags)
print('a tag 수 =', len(atags)) # 104

# (5) a 태그 내용 수집
crawling_data = [] # 빈 list

cnt = 0
for atag in atags :
    cnt += 1
    atagStr = str(atag.string) # string 변환 
    #print(cnt, '->', atagStr)
    crawling_data.append(atagStr.strip())
    '''
    string.strip() : 문단 끝 부분 공백, tab, \n\r 불용어 제거 
    '''
    
# 수집한 자료 확인
print('crawling result')
print(crawling_data)
print(type(crawling_data)) # <class 'list'>

# text save : object -> file(string) -> load(string) 
'''
file = open('../data/crawling_data.txt', mode='w', encoding='utf-8')
file.write(str(crawling_data))  # save
file.close()
print('text file 확인')
'''

# 5) pickle save/load
import pickle # object -> file(binary) -> load(object)
'''
picle 
- list, dict 객체를 binary형태로 저장(저용량)
save : pickle.dump(data, file)
laod : pickle.load(file)
'''
# save
file = open('chapter09/data/data.pickle', mode='wb') # binary save
pickle.dump(crawling_data, file)
print('pickle save')

# load
file = open('chapter09/data/data.pickle', mode='rb') # binary save
crawling_data = pickle.load(file)
print(crawling_data)






