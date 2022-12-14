from xml.etree.ElementTree import parse
import pandas as pd

def get_record_column_names(items):
    for item in items.iter("item"):
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
    for item in items.iter("item"):

        simple_row_list=[] # 행 데이터

        is_first = True
        for column_data in item.iter():
            if is_first:
                is_first = False
                continue
            simple_row_list.append(column_data.text)
        all_records.append(simple_row_list)

    return all_records


tree = parse("12월14일_코로나_예방접종현황.xml")
response = tree.getroot()
items = response.find('body').find('items')



print(get_record_column_names(items))

all_records = get_all_records(items)
column_list = get_record_column_names(items)
print(all_records)
print(column_list)
df = pd.DataFrame(all_records, columns=column_list)
df.to_csv('12월14일_코로나_예방접종현황_v2.csv', encoding='utf-8', index=False)