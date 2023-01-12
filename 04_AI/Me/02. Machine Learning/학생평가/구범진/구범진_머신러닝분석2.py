# 데이터 출처 : http://https://www.kaggle.com/rajeevw/ufcdata
# 데이터 필드의 의미

# 학습 목표: 데이터 셋에 최적화된 머신러닝 모델 선택
# 머신러닝 모델: SVM.SVC
# 머신러닝 모델 선정 사유: 예측값을 범주형에도 적용가능하며 이에 다른 머신러닝 대비 최고의 정답률을 보임
# 교차 검증 K 값: 고려 안함
# 훈련데이터, 검증데이터 선정: N/A
# 성능평가: 1순위 => 정답률, 2순위 => 프로그램 수행 속도
# 목표 정답률: 선형회귀 통계 모델의 최고정답률(50.88%) 이상
# 측정 정답률
#  독립변수 최적화 분석 결과
# 총 조합 갯수: 159, 158개~159개의 독립변수 조합
# MAX 조합: B_Height_cms B_Reach_cms B_Stance_Open Stance B_Stance_Orthodox B_Stance_Sideways B_Stance_Southpaw B_Stance_Switch B_Weight_lbs B_age B_avg_BODY_att B_avg_BODY_landed B_avg_CLINCH_att B_avg_CLINCH_landed B_avg_DISTANCE_att B_avg_DISTANCE_landed B_avg_GROUND_att B_avg_GROUND_landed B_avg_HEAD_att B_avg_HEAD_landed B_avg_KD B_avg_LEG_att B_avg_LEG_landed B_avg_PASS B_avg_REV B_avg_SIG_STR_att B_avg_SIG_STR_landed B_avg_SUB_ATT B_avg_TD_att B_avg_TD_landed B_avg_TD_pct B_avg_TOTAL_STR_att B_avg_TOTAL_STR_landed B_avg_opp_BODY_att B_avg_opp_BODY_landed B_avg_opp_CLINCH_att B_avg_opp_CLINCH_landed B_avg_opp_DISTANCE_att B_avg_opp_DISTANCE_landed B_avg_opp_GROUND_att B_avg_opp_GROUND_landed B_avg_opp_HEAD_att B_avg_opp_HEAD_landed B_avg_opp_KD B_avg_opp_LEG_att B_avg_opp_LEG_landed B_avg_opp_PASS B_avg_opp_REV B_avg_opp_SIG_STR_att B_avg_opp_SIG_STR_landed B_avg_opp_SIG_STR_pct B_avg_opp_SUB_ATT B_avg_opp_TD_att B_avg_opp_TD_landed B_avg_opp_TD_pct B_avg_opp_TOTAL_STR_att B_avg_opp_TOTAL_STR_landed B_current_lose_streak B_current_win_streak B_draw B_longest_win_streak B_losses B_total_rounds_fought B_total_time_fought(seconds) B_total_title_bouts B_win_by_Decision_Majority B_win_by_Decision_Split B_win_by_Decision_Unanimous B_win_by_KO/TKO B_win_by_Submission B_win_by_TKO_Doctor_Stoppage B_wins R_Height_cms R_Reach_cms R_Stance_Open Stance R_Stance_Orthodox R_Stance_Southpaw R_Stance_Switch R_Weight_lbs R_age R_avg_BODY_att R_avg_BODY_landed R_avg_CLINCH_att R_avg_CLINCH_landed R_avg_DISTANCE_att R_avg_DISTANCE_landed R_avg_GROUND_att R_avg_GROUND_landed R_avg_HEAD_att R_avg_HEAD_landed R_avg_KD R_avg_LEG_att R_avg_LEG_landed R_avg_PASS R_avg_REV R_avg_SIG_STR_att R_avg_SIG_STR_landed R_avg_SIG_STR_pct R_avg_SUB_ATT R_avg_TD_att R_avg_TD_landed R_avg_TD_pct R_avg_TOTAL_STR_att R_avg_TOTAL_STR_landed R_avg_opp_BODY_att R_avg_opp_BODY_landed R_avg_opp_CLINCH_att R_avg_opp_CLINCH_landed R_avg_opp_DISTANCE_att R_avg_opp_DISTANCE_landed R_avg_opp_GROUND_att R_avg_opp_GROUND_landed R_avg_opp_HEAD_att R_avg_opp_HEAD_landed R_avg_opp_KD R_avg_opp_LEG_att R_avg_opp_LEG_landed R_avg_opp_PASS R_avg_opp_REV R_avg_opp_SIG_STR_att R_avg_opp_SIG_STR_landed R_avg_opp_SIG_STR_pct R_avg_opp_SUB_ATT R_avg_opp_TD_att R_avg_opp_TD_landed R_avg_opp_TD_pct R_avg_opp_TOTAL_STR_att R_avg_opp_TOTAL_STR_landed R_current_lose_streak R_current_win_streak R_draw R_longest_win_streak R_losses R_total_rounds_fought R_total_time_fought(seconds) R_total_title_bouts R_win_by_Decision_Majority R_win_by_Decision_Split R_win_by_Decision_Unanimous R_win_by_KO/TKO R_win_by_Submission R_win_by_TKO_Doctor_Stoppage R_wins no_of_rounds title_bout weight_class_Bantamweight weight_class_Catch Weight weight_class_Featherweight weight_class_Flyweight weight_class_Heavyweight weight_class_Light Heavyweight weight_class_Lightweight weight_class_Middleweight weight_class_Open Weight weight_class_Welterweight weight_class_Women's Bantamweight weight_class_Women's Featherweight weight_class_Women's Flyweight weight_class_Women's Strawweight >> 69.93 %
#           (69.93%의 총 정답률)
# 프로그램 소요 시간:  0:06:59.016000

import pandas as pd
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import operator
from itertools import combinations
from datetime import datetime

match_dic={}
start_combi = 158
end_combi = 159


print("최적의 독립변수 선정하기 (교차검증 적용) ")
csv = pd.read_csv('preprocessed_data.csv')

# 전체 독립변수 식별
csv_data = csv[csv.columns.difference(['Winner'])]
label = csv['Winner']

start_time = datetime.now()

# 최적의 독립변수 식별
for num in range(start_combi, end_combi):
    combi_list = list(combinations(csv_data,num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC(gamma='auto')
        train_data, test_data, train_label, test_label = \
        train_test_split(csv[data_header_list],label)
        clf.fit(train_data, train_label)
        pre = clf.predict(test_data)
        ac_score = metrics.accuracy_score(test_label, pre)
        data_header_name = ' '.join(data_header_list)
        accuracy_round = round(ac_score*100,4)
        match_dic[data_header_name] = accuracy_round
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> 정답률: {accuracy_round}%')

end_time = datetime.now()

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print(f'총 조합 갯수: {len(match_dic)}, {start_combi}개~{end_combi}개의 독립변수 조합')
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
print("프로그램 소요 시간: ", end_time-start_time)