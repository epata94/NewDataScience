from flask import Flask
# pip install flask-restful
from flask_restful import Resource, Api
from flask import Flask, render_template
import pandas as pd
import numpy as np
import cx_Oracle
from datetime import datetime
cx_Oracle.init_oracle_client(lib_dir=r"D:\util\instantclient_21_8")

app = Flask(__name__)

app.debug = True
api = Api(app)


class Recommand(Resource):
    def get(self,num):
        result=find_simi_place(num)
        return {'result1':result[0],
                'result2':result[1],
                'result3':result[2],
                'result4':result[3],
                'result5':result[4]}
def return_store_df(store_id_input): #반환함수
    connection = cx_Oracle.connect(user='admin', password='Qlalfqjsgh12wkfl', dsn='finalproject_high')
    cur=connection.cursor()
    sql = """
    select store_info.store_id, store_info.store_name, store_info.addr, store_info.category, review_sum.content from 
(select store_id,store_name, addr,category, sqrt(power(lat-(select lat from naver_store where store_id=:input1),2)+power(lon-(select lon from naver_store where store_id=:input3),2)) distance from(
select k_store_info.store_id, k_store_info.store_name, k_store_info.addr,k_store_info.lon,k_store_info.lat, k_store_info.category 
    from 
    (select store_id,store_name,addr,lon,lat,replace(concat(concat(cate_b,' '),cate_c),'/',' ') category from kakao_store 
            where instr(addr,(select substr(addr,INSTR(addr,' ',1),INSTR(addr,' ',2)) from kakao_store where store_id= :input2))>0 and kakao_star_avg>3) k_store_info
union

select n_store_info.store_id, n_store_info.store_name, n_store_info.addr,n_store_info.lon,n_store_info.lat, n_store_info.category 
    from 
    (select store_id,store_name,addr,lon,lat,replace(concat(concat(cate_b,' '),cate_c),'/',' ') category from naver_store 
            where instr(addr,(select substr(addr,INSTR(addr,' ',1),INSTR(addr,' ',2)) from naver_store where store_id= :input4))>0 and naver_star_avg>3) n_store_info)
            where rownum<50
            order by distance) store_info,
(select STORE_ID,listagg(content,' ') content from (select STORE_ID,NAVER_NICKNAME nickname,NAVER_DATE written_date,NAVER_CONTENT content,NAVER_STAR star,'naver' as site
FROM test_review_naver n
union (select STORE_ID,KAKAO_NICKNAME nickname,KAKAO_DATE written_date,KAKAO_CONTENT content,KAKAO_STAR star,'kakao' as site
FROM test_review_kakao)) group by store_id) review_sum
where store_info.store_id=review_sum.store_id
    """
    store_info = cur.execute(sql,(store_id_input,store_id_input,store_id_input,store_id_input))

    column_name=store_info.description # column 불러오기
    columns=[]
    for i in column_name:
        columns.append(i[0])

    row=store_info.fetchall()
    connection = cx_Oracle.connect(user='admin', password='Qlalfqjsgh12wkfl', dsn='finalproject_high')
    cur=connection.cursor()
    return pd.DataFrame(row,columns=columns).drop_duplicates('STORE_ID')

def cosine_similarity(df):
    from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
    from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도
    #서로 카테고리 텍스트가 얼마나 유사한지를 따져줌
    count_vect_category = CountVectorizer(min_df=0, ngram_range=(1,2))
    place_category = count_vect_category.fit_transform(df['CATEGORY'])
    place_simi_cate = cosine_similarity(place_category, place_category)
    place_simi_cate_sorted_ind = place_simi_cate.argsort()[:, ::-1]
        #서로 지역 텍스트가 얼마나 유사한지를 따져줌
    count_vect_location = CountVectorizer(min_df=0, ngram_range=(1,2))
    place_location = count_vect_location.fit_transform(df['ADDR'])
    place_simi_location = cosine_similarity(place_location, place_location)
    place_simi_location_sorted_ind = place_simi_location.argsort()[:, ::-1]

    # 리뷰 텍스트 데이터 간의 텍스트 피쳐 벡터라이징
    count_vect_review = CountVectorizer(min_df=2, ngram_range=(1,2))
    df['CONTENT']=[str(item) for item in df['CONTENT']]
    place_review = count_vect_review.fit_transform(df['CONTENT'])
    place_simi_review = cosine_similarity(place_review, place_review)
    place_simi_review_sorted_ind = place_simi_review.argsort()[:, ::-1]

    #전체가중치
    place_simi_co = (
                     + place_simi_cate * 0.01 # 공식 1. 카테고리 유사도
                     + place_simi_location * 0.2
                     + place_simi_review * 0.3 # 공식 2. 리뷰 텍스트 유사도
                     )
    place_simi_co_sorted_ind = place_simi_co.argsort()[:, ::-1]
    return place_simi_co_sorted_ind

def find_simi_place(store_id):
    recommand=return_store_df(store_id)
    place_simi_co_sorted_ind=cosine_similarity(recommand)
    top_n=6
    place_id = recommand[recommand['STORE_ID'] == store_id]
    place_index = place_id.index.values
    similar_indexes = place_simi_co_sorted_ind[place_index, :(top_n)]
    similar_indexes = similar_indexes.reshape(-1)
    return recommand['STORE_ID'].iloc[similar_indexes[1:]].tolist()

api.add_resource(Recommand,'/recommand/<int:num>')
if __name__ == '__main__':
    app.run(host='localhost')
    # app.run(host='192.168.0.78')

