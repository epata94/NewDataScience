# 데이터 출처 : https://archive.ics.uci.edu/ml/datasets/Travel+Reviews
# 데이터 필드의 의미
# User : 사용자 ID
# Category 1 : 교회에 대한 평균 평점
# Category 2 : 리조트에 대한 평균 평점
# Category 3 : 해변에 대한 평균 평점
# Category 4 : 공원에 대한 평균 평점
# Category 5 : 극장에 대한 평균 평점
# Category 6 : 박물관에 대한 평균 평점
# Category 7 : 쇼핑몰에 대한 평균 평점
# Category 8 : 동물원에 대한 평균 평점
# Category 9 : 레스토랑에 대한 평균 평점
# Category 10 : 펍/바에 대한 평균 평점
# Category 11 : 지역 서비스에 대한 평균 평점
# Category 12 : 버거/피자 상점에 대한 평균 평점
# Category 13 : 호텔/기타 숙박 시설에 대한 평균 평점
# Category 14 : 주스 바에 대한 평균 평점
# Category 15 : 미술관에 대한 평균 평점
# Category 16 : 댄스 클럽에 대한 평균 평점
# Category 17 : 수영장에 대한 평균 평점
# Category 18 : 체육관에 대한 평균 평점
# Category 19 : 빵집에 대한 평균 평점
# Category 20 : 미용 & 스파에 대한 평균 평점
# Category 21 : 카페에 대한 평균 평점
# Category 22 : 전망 포인트에 대한 평균 평점
# Category 23 : 기념비에 대한 평균 평점
# Category 24 : 정원에 대한 평균 평점

# 학습 목표: 비지도 학습용 데이터 셋 선별 및 의미 해석
# 머신러닝 모델: K-중심 군집화 (K-centroid clustering, K-medoid clustering) => KMeans
# 머신러닝 모델 선정 사유: 특별한 종속변수가 없으며 가장 일반적인 Clustering시
#                        사용하는 모델 적용
# 목표 성능: 클러스터 개수에 따른 엘보우 메소드를 보고 적절한 클러스터 개수 선정.


import time
import pandas as pd
from pandas import DataFrame
import operator
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


def revision(attractions, sorted_row, i, up_down):
    while True:
        if sorted_row[i][1] == sorted_row[i+up_down][1]:
            attractions[sorted_row[i + up_down][0]] += up_down
            i = i + up_down
        else:
            return attractions

def check_rank(data, group_dic, key):
    columns_list = data.columns[1:-1]
    attractions = {}
    for i in range(len(columns_list)):
        attractions.setdefault(columns_list[i], 0)
    data_dic = data[columns_list].to_dict('records')
    for row in data_dic:
        sorted_row = sorted(row.items(), key=operator.itemgetter(1), reverse=True)
        for top in range(0,3):
            attractions[sorted_row[top][0]] += 1
        attractions = revision(attractions, sorted_row, top, 1)
        for bottom in range(len(columns_list)-3, len(columns_list)):
            attractions[sorted_row[bottom][0]] -= 1
        attractions = revision(attractions, sorted_row, len(columns_list)-3, -1)
    sorted_attractions = sorted(attractions.items(), key=operator.itemgetter(1), reverse=True)

    group_dic[key]['like'] += sorted_attractions[:3]
    group_dic[key]['hate'] += list(reversed(sorted_attractions[-3:]))
    print(f'''\n[ {key}군 ]
Best 3: {group_dic[key]["like"]}
 static of no.1 : {stats.describe(data[group_dic[key]['like'][0][0]])}
Worst 3: {group_dic[key]["hate"]}
 static of no.1 : {stats.describe(data[group_dic[key]['hate'][0][0]])}''')
    return group_dic

print("Step1] 빅데이터 로딩 완료")
# 파일을 읽어 위에 정의한 데이터구조를 채움
G_review = pd.read_csv('google_review_ratings.csv', sep=',', header=0)
change_name = ['user', 'churches', 'resorts', 'beaches', 'parks', 'theatres',
                'museums', 'malls','zoo', 'restaurants', 'pubs_bars', 'local_services',
                'burger_pizza_shops', 'hotels_other_lodgings', 'juice_bars',
                'art_galleries', 'dance_clubs', 'swimming_pools', 'gyms', 'bakeries',
                'beauty_spas', 'cafes', 'view_points', 'monuments', 'gardens']
G_review.columns = change_name
G_review['local_services'] = G_review['local_services'].str.replace('\t','')
G_review = G_review.fillna(0)

G_review[change_name[1:]] = G_review[change_name[1:]].astype(float)

print("\nStep2] 엘보우 메소드를 이용하여 클러스터 개수 선정")
# 엘보우 메소드 : 클러스터의 개수에 따른 데이터의 SSE(오차제곱합) 값을 그래프로 그려주는 함수.
# k의 변화에 따른 SSE의 변화가 줄어드는 (기울기가 완만해지는) 경계에 있는 k를 이용하는 것이 적합.
# 실루엣 계수로 클러스터의 개수를 선정하기에는 할 때마다 결과에 차이가 있어 엘보우 메소드 이용.
Sum_of_squared_distances = []
K = range(1, 12)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(G_review[change_name[1:]])
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

# -> k=6 부터 완만하기 때문에 그 직전인 5개로 선정.


print("\nStep3] K-평균 군집화 기법을 적용하여 실루엣 계수 구하기")
# 실루엣 계수: 생성된 클러스터 안의 데이터가 얼마나 밀접하게 모여 있는지를 계산
# 클러스터 안의 샘플이 자신이 속한 클러스터 안의 다른 샘플과 얼마나 유사한지 평가
# -1 ~ 1 사이의 값을 가지며 1에 가까울 수록 유사.
k = 5
km = KMeans(n_clusters=k, n_init=10).fit(G_review[change_name[1:]])
print("score for %d clusters:%.3f" % (k, silhouette_score(G_review[change_name[1:]],km.labels_)))

# 실루엣 계수로 클러스터를 선정할 경우
# for k in range(2,len(G_review[change_name[1:]])):
#     km = KMeans(n_clusters=k).fit(G_review[change_name[1:]])
#     print("score for %d clusters:%.3f" % (k, silhouette_score(G_review[change_name[1:]],km.labels_)))

label_data = DataFrame(km.labels_, columns=['group'])
combine_data = pd.merge(G_review, label_data, left_index=True, right_index=True)

print("\nStep4] 군집의 특성 키워드 구하기")
# 각 유형별 관광명소 top 3 와 bottom 3 표시
group_dic = {}
for i in range(k):
    group_dic.setdefault(i, {'like':[], 'hate':[]})

for group in range(k):
    group_dic = check_rank(combine_data[combine_data['group'].isin([group])], group_dic, group)

print("\n Step6] 분석결과에 대하여 해석하고 발표하기")
# 쇼핑몰, 극장과 같은 번화가를 좋아하는 유형은 체육관, 수영장 같은 곳을 극단적으로 싫어한다.
# 주스바, 갤러리 같은 감성적인 곳을 좋아하는 유형도 체육관, 수영장 같은 곳을 싫어한다.
# 리조트, 뷰포인트, 정원 같은 자연친화적인 풍경을 보는 것을 좋아하는 유형은
# 댄스클럽이나 수영장 같은 활기 넘치는 곳을 싫어한다.
# 뷰포인트, 공원, 극장 같은 서정적인 곳을 좋아하는 유형은 극단적으로 빵집, 뷰티 스파 같은
# 일상적이고 좁은 공간에 갇혀 있는 곳을 싫어한다.
# 레스토랑이나 펍바 같은 음식점을 좋아하는 유형은 빵집, 체육관, 수영장 같은 곳을 싫어한다.

# 전체적으로 체육관이나 수영장 같은 갇힌 곳에서 즐기는 운동을 좋아하지 않는다.
# 번화가를 좋아하는 유형과 서정적인 곳을 좋아하는 유형은 싫어하는 곳의 성향이 확고하기 때문에
# 싫어할 가능성이 높은 곳은 권하지 않는 것이 좋다.

