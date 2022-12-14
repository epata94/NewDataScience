from xml.etree.ElementTree import Element, parse,dump

def whole_xml():
    tree = parse('students_zero.xml')
    note = tree.getroot()

    for parent in tree.iter():
        for child in parent:
            print(child.text)

while True:
    print("학생정보 XML 데이터 분석 시작")
    print("\n1. 요약정보\n2. 전체데이터 조회\n3. 종료")
    menu = int(input("메뉴입력 : "))

    if menu == 1:
        whole_xml()

    elif menu == 2:
        whole_xml()

    elif menu == 3:
        break