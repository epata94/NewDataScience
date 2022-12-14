from xml.etree.ElementTree import parse
import pandas as pd

from xml.etree.ElementTree import parse
import pandas as pd

def covid_xml_to_df():
    tree = parse("12월14일_코로나_예방접종현황.xml")
    response = tree.getroot()
    # 한꺼 번에 메서드 체이닝 하지 않는 이유는 추후에 item 노드에서 자동완성을 하기 위함이다.
    items = response.find('body').find('items')
    item_list=[]
    for item in items.iter("item"):

        simple_row_list=[]
        simple_row_list.append(item.find('tpcd').text)
        simple_row_list.append(item.find('firstCnt').text)
        simple_row_list.append(item.find('secondCnt').text)
        simple_row_list.append(item.find('thirdCnt').text)
        simple_row_list.append(item.find('fourCnt').text)
        simple_row_list.append(item.find('winCnt').text)
        simple_row_list.append(item.find('vrate').text)
        simple_row_list.append(item.find('wrate').text)

        item_list.append(simple_row_list)

    column_list = ['tpcd','firstCnt','secondCnt','thirdCnt','fourCnt','winCnt','vrate','wrate']
    return pd.DataFrame(item_list, columns=column_list)

df = covid_xml_to_df()
print(df)

df.to_csv('12월14일_코로나_예방접종현황_v1.csv', encoding='utf-8', index=False)