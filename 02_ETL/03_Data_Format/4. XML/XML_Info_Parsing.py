from xml.etree.ElementTree import parse
import pandas as pd

def get_record_column_names(items):
    for item in items.iter("record"):
        column_list = []
        is_first = True
        for column_data in item.iter():
            if is_first:
                is_first = False
                continue
            column_list.append(column_data.tag)

        return column_list

def get_all_records(items):

    all_records = []
    for item in items.iter("record"):

        simple_row_list=[] # 행 데이터

        is_first = True
        for column_data in item.iter():
            if is_first:
                is_first = False
                continue
            simple_row_list.append(column_data.text)
        all_records.append(simple_row_list)

    return all_records


tree = parse("전국공공시설개방정보표준데이터.xml")
root = tree.getroot()
records = root.find('records')
print(records.tag)

print(get_record_column_names(records))

all_records = get_all_records(records)
column_list = get_record_column_names(records)
# print(all_records)
# print(column_list)
df = pd.DataFrame(all_records, columns=column_list)
print(df.head())
print(df.shape)
# df.to_csv('12월13일_시도별_코로나백신_접종현황.csv', encoding='utf-8', index=False)