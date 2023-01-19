import pandas as pd
import statsmodels.api as sm
import numpy as np
import warnings
from itertools import combinations, permutations
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

warnings.filterwarnings('ignore')

heart = pd.read_csv('heart.csv', sep=',', header=0)

feature = heart[heart.columns.difference(['target'])]
label = heart['target']

len = len(heart.columns.difference(['target']))

best = []

max = 0

for num in range(1, len + 1) :
    combi = list(combinations(heart.columns.difference(['target']), num))

    for tup in combi :
        try :
            feature = heart[list(tup)]
            train_input, test_input, train_target, test_target = train_test_split(
                feature, label,stratify=label, random_state=300)

            mean = np.mean(train_input, axis=0)
            std = np.std(train_input, axis=0)

            train_scaled=(train_input-mean)/std

            test_scaled = ((test_input) - mean) / std

            kn = KNeighborsClassifier()

            kn.fit(train_input, train_target)

            kn.score(train_input, train_target)

            kn.fit(train_scaled, train_target)

            if kn.score(test_scaled, test_target) > max :
                max = kn.score(test_scaled, test_target)
                best = feature
                print(max)
        except:
            pass

print(max)
print(best)