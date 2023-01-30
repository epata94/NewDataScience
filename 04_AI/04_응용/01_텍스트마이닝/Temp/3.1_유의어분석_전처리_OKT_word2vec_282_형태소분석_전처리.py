# py -m pip install gensim
import codecs
from konlpy.tag import Twitter
from konlpy.tag import Okt
from gensim.models import word2vec # word2vec: 문장 내부의 단어를 벡터로 변환하는 도구
# utf-16 인코딩으로 파일을 열고 글자를 출력하기 --- (※1)
# fp = codecs.open("박근혜_국정연설문_2016.txt", "r", encoding="utf-8")
fp = codecs.open("문재인_국정연설문_2017.txt", "r", encoding="utf-8")
text = fp.read()
# 텍스트를 한 줄씩 처리하기 --- (※2)
# twitter = Twitter()
okt = Okt()
results = []
lines = text.split("\r\n")
for line in lines:
    # 형태소 분석하기 --- (※3)
    # 단어의 기본형 사용
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외 
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)
# 파일로 출력하기  --- (※4)
# wakati_file = 'hong.wakati'
# wakati_file = 'park.wakati'
wakati_file = 'moon.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
# Word2Vec 모델 만들기 --- (※5)
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, 
    size=200, window=10, hs=1, min_count=2, sg=1)
# size=200: 200차원 짜리 벡터스페이스
# sg=1, 0이면 CBOW, 1이면 skip-gram을 사용한다.
# The parameters:
# min_count = int - Ignores all words with total absolute frequency lower than this - (2, 100)
# window = int - The maximum distance between the current and predicted word within a sentence. E.g. window words on the left and window words on the left of our target - (2, 10)
# size = int - Dimensionality of the feature vectors. - (50, 300)
# sample = float - The threshold for configuring which higher-frequency words are randomly downsampled. Highly influencial. - (0, 1e-5)
# alpha = float - The initial learning rate - (0.01, 0.05)
# min_alpha = float - Learning rate will linearly drop to min_alpha as training progresses. To set it: alpha - (min_alpha * epochs) ~ 0.00
# negative = int - If > 0, negative sampling will be used, the int for negative specifies how many "noise words" should be drown. If set to 0, no negative sampling is used. - (5, 20)
# workers = int - Use these many worker threads to train the model (=faster training with multicore machines)

# model.save("park.model")
model.save("moon.model")
print("\n\n================= 분석 완료 ==================")


