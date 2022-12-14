from xml.etree.ElementTree import parse
import pandas as pd

def covid_xml_to_df():
    tree = parse("12월14일_코로나_예방접종현황.xml")
    note = tree.getroot()
    student_list=[]
    for parent in note.iter("student"):

        simple_row_list=[] # 행 데이터
        name = parent.get("name")
        sex = parent.get("sex")
        age = parent.findtext("age")
        major = parent.findtext("major")

        simple_row_list.append(name)
        simple_row_list.append(sex)
        simple_row_list.append(age)
        simple_row_list.append(major)


        pcl_node = parent.find('practicable_computer_languages')
        if pcl_node:
            for language in pcl_node.iter("language"):
                all_data_row_list=simple_row_list.copy()
                all_data_row_list.append(language.get('name'))
                all_data_row_list.append(language.get('level'))
                all_data_row_list.append(language.find('period').get('value'))
                student_list.append(all_data_row_list)
        else:
            simple_row_list.append('N/A')
            simple_row_list.append('N/A')
            simple_row_list.append('N/A')
            student_list.append(simple_row_list)

    column_list = ['이름','성별','나이','전공','컴퓨터언어','레벨','사용기간']
    return pd.DataFrame(student_list, columns=column_list)


df = covid_xml_to_df()
print(df)
df.to_csv('covid_info_1213.csv', encoding='cp949', index=False)