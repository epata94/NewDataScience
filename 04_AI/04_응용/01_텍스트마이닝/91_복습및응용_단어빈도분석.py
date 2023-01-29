import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

f = open("트럼프취임연설문.txt", 'r')
lines = f.readlines()[0]
f.close()

lines[0:100]

tokenizer = RegexpTokenizer('[\w]+')
stop_words = stopwords.words('english')
words =  lines.lower()
tokens = tokenizer.tokenize(words)
# 불용어 처리
# stop_words에 있거나
stopped_tokens = [i for i in list((tokens)) if not i in stop_words]
# 1글자는 제외
stopped_tokens2 = [i for i in stopped_tokens if len(i)>1]

# 중첩 리스트 하나의 리스트로 변환하는 함수
def flatten(l):
    flatList = []
    for elem in l:
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList

pd.Series(stopped_tokens2).value_counts().head(10)

f = open("문재인대통령취임연설문.txt", 'r')
lines = f.readlines()
f.close()

from konlpy.tag import Hannanum

hannanum = Hannanum()

temp = []
for i in range(len(lines)):
    temp.append(hannanum.nouns(lines[i]))


def flatten(l):
    flatList = []
    for elem in l:
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList

word_list=flatten(temp)

# 두글자 이상인 단어만 추출
word_list=pd.Series([x for x in word_list if len(x)>1])
word_list.value_counts().head(10)

from wordcloud import WordCloud
from collections import Counter

font_path = 'NanumBarunGothic.ttf'

wordcloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white"
)

count = Counter(stopped_tokens2)
wordcloud = wordcloud.generate_from_frequencies(count)

def __array__(self):
    """Convert to numpy array.
    Returns
    -------
    image : nd-array size (width, height, 3)
        Word cloud image as numpy matrix.
    """
    return self.to_array()

def to_array(self):
    """Convert to numpy array.
    Returns
    -------
    image : nd-array size (width, height, 3)
        Word cloud image as numpy matrix.
    """
    return np.array(self.to_image())
array = wordcloud.to_array()

#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
plt.imshow(array, interpolation="bilinear")
plt.show()
fig.savefig('wordcloud.png')

count = Counter(word_list)

wordcloud = wordcloud.generate_from_frequencies(count)

array = wordcloud.to_array()

#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
plt.imshow(array, interpolation="bilinear")
plt.show()
fig.savefig('wordcloud.png')


from PIL import Image
import numpy as np
from wordcloud import ImageColorGenerator

moon_mask=np.array(Image.open("문재인대통령.PNG"))

plt.figure(figsize=(8,8))
plt.imshow(moon_mask,interpolation="bilinear")
plt.show()

count = Counter(word_list)

wc_moon = WordCloud(
    font_path = font_path,
    mask=moon_mask,
    background_color="white"
)
wc_moon = wc_moon.generate_from_frequencies(count)

plt.figure(figsize=(8,8))
plt.imshow(wc_moon,interpolation="bilinear")
plt.axis("off")
plt.show()

image_colors=ImageColorGenerator(moon_mask)

plt.figure(figsize=(8,8))
plt.imshow(wc_moon.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")
plt.show()

