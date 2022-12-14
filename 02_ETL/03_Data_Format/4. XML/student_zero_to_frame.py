import pandas as pd
from xml.etree.ElementTree import parse

tree = parse("students_zero.xml")
student_list = tree.getroot()

student_list_to_frame = []
for student in student_list:
    student_temp = []
    student_temp.append(student.get('name'))
    student_temp.append(student.get('sex'))
    student_temp.append(student.find('age').text)
    student_temp.append(student.find('major').text)

    student_list_to_frame.append(student_temp)

# print(student_list_to_frame)
columns = ['name','sex','age','major']

df = pd.DataFrame(student_list_to_frame, columns=columns)
print(df)
