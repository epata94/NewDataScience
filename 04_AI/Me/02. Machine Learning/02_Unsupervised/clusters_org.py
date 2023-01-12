import matplotlib, matplotlib.pyplot as plt
import pandas as pd
import sklearn.cluster, sklearn.preprocessing

alco2009 = pd.read_csv("niaaa-report2009.csv",index_col="State")
# 주 약칭 데이터를 읽어온다.
states = pd.read_csv("states2.csv",
                     names=("State", "Standard", "Postal", "Capital"))
columns = ["Wine", "Beer"]
# 클러스터링 객체를 생성하고 모델을 학습시킨다.
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009["Clusters"] = kmeans.labels_
centers = pd.DataFrame(kmeans.cluster_centers_, columns=columns)

# 플로팅 스타일을 선택한다.
matplotlib.style.use("ggplot")

# 주와 centroid를 플롯에 그린다.
ax = alco2009.plot.scatter(columns[0], columns[1], c="Clusters", 
                           cmap=plt.cm.Accent, s=100)
centers.plot.scatter(columns[0], columns[1], color="red", marker="+", 
                     s=200, ax=ax)

# 주 약칭을 플롯에 추가한다.
def add_abbr(state):
    _ = ax.annotate(state["Postal"], state[columns], xytext=(1, 5), 
                    textcoords="offset points", size=8,
                    color="darkslategrey")

# alco2009withStates = pd.concat([alco2009, states.set_index("State")],
#                                axis=1 )
alco2009withStates = pd.concat([alco2009, states.set_index("State")],
                               axis=1, sort=False)
alco2009withStates.apply(add_abbr, axis=1)

# 플롯에 제목을 붙이고 저장한다.
plt.title("US States Clustered by Alcohol Consumption")
plt.savefig("clusters.pdf")
