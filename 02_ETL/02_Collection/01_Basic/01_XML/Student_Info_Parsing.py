from xml.etree.ElementTree import parse

menu=0
tree = parse('students_info.xml')
note = tree.getroot()
print('학생정보 XML데이터 분석 시작')
menu = int(input('1. 요약정보\n2. 전체 데이터 조회\n3. 종료\n메뉴 입력: '))
count_students = len(note)
count_male = 0
count_female=0
count_major=0
count_programming=0
count_level=0
count_python=0
age_20=0
age_20_list=[]
age_30=0
age_30_list=[]
age_40=0
age_40_list=[]
tag_students = note.findall('student')
def print_age_list(age_list):
    print('[ ',end='')
    for list in age_list:
        in_name,in_age = list.split(' ')
        print('%s:%s '%(in_name,in_age),end='')
    print(']')
if menu==1:
    for student in range(count_students):
        if tag_students[student].get('sex')=='남':
            count_male+=1
        elif tag_students[student].get('sex')=='여':
            count_female+=1
        if tag_students[student].findtext('major')=='컴퓨터 공학':
            count_major+=1
        elif tag_students[student].findtext('major').find('통계')!=-1:
            count_major+=1
        if tag_students[student].find('practicable_computer_languages').text:
            count_programming+=1
        if tag_students[student].find('practicable_computer_languages').text:
            for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                if lang.get('level')=='상':
                    count_level+=1
                if lang.get('name')=='Python':
                    count_python+=1
        age = int(tag_students[student].findtext('age'))
        if age>=20 and age<30:
            age_20+=1
            age_20_list.append('%s %s'%(tag_students[student].get('name'),tag_students[student].findtext('age')))
        elif age>=30 and age<40:
            age_30+=1
            age_30_list.append('%s %s' % (tag_students[student].get('name'), tag_students[student].findtext('age')))
        elif age>=40 and age<50:
            age_40+=1
            age_40_list.append('%s %s' % (tag_students[student].get('name'), tag_students[student].findtext('age')))
        student+=1
    print('<요약 정보>')
    print('* 전체 학생수: %d 명'%count_students)
    print('* 성별')
    print('- 남학생: %d명 (%0.1f%%)'%(count_male,(count_male/count_students)*100))
    print('- 여학생: %d명 (%0.1f%%)'%(count_female,(count_female/count_students)*100))
    print('* 전공여부')
    print('- 전공자(컴퓨터 공학, 통계): %d명 (%0.1f%%)'%(count_major,(count_major/count_students)*100))
    print('- 프로그래밍 언어 경험자: %d명 (%0.1f%%)'%(count_programming,(count_programming/count_students)*100))
    print('- 프로그래밍 언어 상급자: %d명 (%0.1f%%)'%(count_level,(count_level/count_students)*100))
    print('- 파이썬 경험자: %d명 (%0.1f%%)'%(count_python,(count_python/count_students)*100))
    print('* 연령대')
    print('- 20대: %d명 (%0.1f%%)'%(age_20,(age_20/count_students)*100),end=' ')
    print_age_list(age_20_list)
    print('- 30대: %d명 (%0.1f%%)'%(age_30,(age_30/count_students)*100),end=' ')
    print_age_list(age_30_list)
    print('40대: %d명 (%0.1f%%)'%(age_40,(age_40/count_students)*100),end=' ')
    print_age_list(age_40_list)
elif menu==2:
    for student in range(count_students):
        print('* %s'%tag_students[student].get('name'))
        print(' - 성별: %s'%tag_students[student].get('sex'))
        print(' - 나이: %s'%tag_students[student].findtext('age'))
        print(' - 전공: %s'%tag_students[student].findtext('major'))
        print(' - 사용 가능한 컴퓨터 언어:',end=' ')
        if tag_students[student].find('practicable_computer_languages').text:
            for lang in tag_students[student].find('practicable_computer_languages').findall('language'):
                print('\n > %s (학습기간: %s, Level:%s)'%(lang.get('name'), lang.find('period').get('value'),lang.get('level')),end='')
            print()
        else:
            print('없음')
        student+=1
elif menu==3:
    print('학생 정보 분석 완료!')
    exit()