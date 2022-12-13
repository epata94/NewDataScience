from xml.etree.ElementTree import parse
import pandas as pd

def student_xml_to_df():
    tree = parse("students_info.xml")
    note = tree.getroot()
    student_list=[]
    for parent in note.iter("student"):

        simple_row_list=[]
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

def whole_data(df):

    pass

def sumup_data():
    pass

df = student_xml_to_df()
print(df)

while True:
    print("학생정보 XML데이터 분석 시작..")
    input_data=input("1.요약정보 \n2.전체데이터 조회 \n3.종료 \n메뉴입력: ")
    if input_data=='3':
        print("학생 정보 분석 완료!")
        quit()
    elif input_data=='2':
        whole_data(df)
    elif input_data == '1':
        sumup_data()