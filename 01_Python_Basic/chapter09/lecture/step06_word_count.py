'''
1. pickle.load()
2. text 전처리 : 함수 이용
3. word count
'''

import pickle

# 1. pickle.load()
# load
file = open("chapter09/data/data.pickle", mode='rb')
news_data2 = pickle.load(file)
print(news_data2)

# 2. text 전처리
import re

def clean_text(text_string):
    # 문장부호 제거 : 따옴표 추가(\'\")
    text_string_re = re.sub('[,.?!:\'\";]', '', text_string)
    # 특수문자, 숫자 제거
    text_string_re = re.sub('[!@#$%^&*()]|[0-9]', '', text_string_re)
    # 영문 소문자 -> 영문 제거
    text_string_re = text_string_re.lower()
    text_string_re = re.sub('[a-z]', '', text_string_re)
    # 공백 제거
    text_string_re = ' '.join(text_string_re.split()) # '우리나라 대한민국'

    return text_string_re

# 텍스트 전처리
clean_texts = [clean_text(row) for row in news_data2]

print('>>텍스트 전처리 결과<<')
print(clean_texts)

# 3. word count
word_count = {}

for text in clean_texts : # 문장
    for word in text.split() : # 문장 -> 단어
        # {'word' : count}
        word_count[word] = word_count.get(word, 0) + 1

print('>>워드 카운트<<')
print(word_count)

# 4. 단어 전처리
# 불용 단어 제거
del word_count['[바로잡습니다]']

# 3회 이상 출현 단어 & 2~4자 단어 선정
new_word_count = {}
for word, cnt in word_count.items(): # (단어:빈도수)
    if cnt >=3 and len(word) >=2 and len(word) <=3 :
        print(word, '->', word_count[word])
        new_word_count[word] = new_word_count.get(word, cnt)

print('>>단어 전처리<<')
new_word_count
# {'정경심': 4, '조국': 10, '장관': 3, '서울대': 4, '복직': 3, '지하철': 4, '막판': 3, '설리': 3, '축구': 3}

# 5. top word Counter
from collections import Counter

counter = Counter(new_word_count) # 생성자 -> object
top5_word = counter.most_common(5) # top10
print('>>top 5 단어<<')
print(top5_word)
# [('조국', 10), ('정경심', 4), ('서울대', 4), ('지하철', 4), ('장관', 3)]


words = [] # 단어
counts = [] # 출현빈도수
for word, count in top5_word : # ('성장률', 5)
    words.append(word)
    counts.append(count)

print(words)
print(counts)


'''
pip install matplotlib
'''

import matplotlib.pyplot as plt

# 차트에서 한글 지원
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 선 그래프
plt.plot(words, counts)  # 그리기
plt.show()  # 보이기

# 막대 그래프
plt.bar(words, counts)
plt.show()

