import MySQLdb
import time
import csv


def sumup_db():
    count = 0
    sex = []
    lan_cnt = 0
    cnt_level = 0
    cnt_python = 0
    age_20 = []
    age_30 = []
    age_40 = []
    major_cnt = 0
    boy = 0
    girl = 0
    output_full = []

    mysql_set.execute("SELECT * FROM student;")
    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full.append(output)

    for parent in output_full:

        if parent[2].find('남') != -1:
            boy += 1
        elif parent[2].find('여') != -1:
            girl += 1

        if int(parent[3]) < 30:
            age_20.append(parent[1] + ':' + parent[3])
        elif int(parent[3]) < 40:
            age_30.append(parent[1] + ':' + parent[3])
        elif int(parent[3]) < 50:
            age_40.append(parent[1] + ':' + parent[3])

        if parent[4].find("컴퓨터") != -1 or parent[4].find("통계") != -1:
            major_cnt += 1
        if parent[5]:
            lan_cnt += 1
        if parent[5].find("python") != -1:
            cnt_python += 1
        if parent[6]:
            cnt_level += 1
        count += 1

    print("* 전체 학생수:%d" % count)
    print("* 성별\n - 남학생: %s명(%0.1f%%)\n - 여학생: %s명(%0.1f%%)" % (boy, (boy / count) * 100, girl, (girl / count) * 100))
    print('* 전공여부')
    print("- 전공자(컴퓨터 공학, 통계): %s명 (%0.1f%%)" % (major_cnt, (major_cnt / count) * 100))
    print("- 프로그래밍 언어 경험자: %s명 (%0.1f%%)" % (lan_cnt, (lan_cnt / count) * 100))
    print("- 프로그래밍 언어 상급자: %s명 (%0.1f%%)" % (cnt_level, (cnt_level / count) * 100))
    print("- 파이썬 경험자: %s명 (%0.1f%%)" % (cnt_python, (cnt_python / count) * 100))
    print('* 연령대')
    print('- 20대: %s명 (%0.1f%%) %s' % (len(age_20), (len(age_20) / count) * 100, age_20))
    print('- 30대: %s명 (%0.1f%%) %s' % (len(age_30), (len(age_30) / count) * 100, age_30))
    print('- 40대: %s명 (%0.1f%%) %s' % (len(age_40), (len(age_40) / count) * 100, age_40))
    print("")


def search_db():
    while True:
        print("<조회 서브 메뉴>")
        input_data = input("1.개별 학생 조회 \n2.전체 학생 조회 \n3.상위 메뉴 \n메뉴입력: ")
        if input_data == '3':
            break
        elif input_data == '2':
            whole_db()
        elif input_data == '1':
            individual_db()


def individual_db():
    while True:
        print("<검색 조건>")
        print("1.ID \n2.이름 \n3.나이 \n4.전공 \n5.컴퓨터 언어 명 \n6.컴퓨터 언어 레벨 \n7.상위 메뉴 \n")
        input_data = input("메뉴 입력: ")
        if input_data == '1' or input_data == '2' or input_data == '3' or input_data == '4' or input_data == '5' or input_data == '6':
            whole_search_db(input_data)
        elif input_data == '7':
            break


def whole_db():
    output_full = []

    mysql_set.execute("SELECT * FROM student;")
    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full.append(output)

    for parent in output_full:
        print("* %s" % parent[1], end='')
        print("(%s)" % parent[0])
        print("- 성별: %s" % parent[2])
        print("- 나이: %s" % parent[3])
        print("- 전공: %s" % parent[4])
        parent_language = parent[5].split(' ')
        level_hi = parent[6].split(' ')
        level_mi = parent[7].split(' ')
        level_lo = parent[8].split(' ')
        cnt = 0
        level = ''
        if parent_language[0] != '':
            for language_value in parent_language:
                try:
                    if language_value == level_hi[cnt]:
                        level = '상'
                    elif language_value == level_mi[cnt]:
                        level = '중'
                    elif language_value == level_lo[cnt]:
                        level = '하'
                except Exception:
                    pass
                print("> %s, 수준:%s" % (language_value, level))
                cnt += 1
    print("")


def insert_db():
    id = []
    id_append = ''
    value_count = 0
    language_value = []
    period_value = []
    language_level = []
    language_level_hi = []
    language_level_mid = []
    language_level_low = []

    while True:
        id = []
        language_value = []
        period_value = []
        language_level = []
        print("<신규 학생 정보 입력>")
        value_count = 0
        name_value2 = input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
        if name_value2 == "":
            break
        else:
            name_value = name_value2
        sex_value = input("- 성별을 입력하시요: ")
        age_value = int(input("- 나이를 입력하세요: "))
        major_value = input("- 전공을 입력하세요: ")
        print("- 사용 가능한 컴퓨터 언어를 입력하세요 ")
        while True:
            language_value2 = (str(input(" > 언어 이름(종료는 'Enter' 입력): ")))
            if language_value2 == "":
                break
            else:
                language_value.append(language_value2)
            language_levels = (str(input(" > 수준(상,중,하): ")))
            if language_levels == '상':
                language_level_hi.append(language_value[value_count])
            elif language_levels == '중':
                language_level_mid.append(language_value[value_count])
            elif language_levels == '하':
                language_level_low.append(language_value[value_count])

            value_count += 1

        try:
            mysql_set.execute("SELECT student_id FROM %s" % table_name)
            rows = mysql_set.fetchall()
            id_num = int(str(sorted(list(rows), reverse=True)[0])[5:8])
        except Exception:
            id_num = 0

        if id_num < 9:
            id_append = '00' + str(id_num + 1)
        elif id_num < 99:
            id_append = '0' + str(id_num + 1)
        elif id_num < 999:
            id_append = id_num + 1
        ID = "ITT" + id_append

        language_value = ' '.join(language_value)
        language_level_hi = ' '.join(language_level_hi)
        language_level_mid = ' '.join(language_level_mid)
        language_level_low = ' '.join(language_level_low)
        mysql_set.execute("""INSERT INTO %s VALUES ('%s', '%s','%s', %s, '%s', '%s', '%s', '%s', '%s');""" % (
        table_name, ID, name_value, sex_value, age_value, major_value, language_value, language_level_hi,
        language_level_mid, language_level_low))
        con.commit()


def whole_search_db(num_data):
    search_data = input("검색어를 입력하세요: ")
    output_full = []

    if num_data == '1':
        mysql_set.execute("SELECT * FROM %s where student_id like '%%%s%%'" % (table_name, search_data))
    elif num_data == '2':
        mysql_set.execute("SELECT * FROM %s where name like '%%%s%%'" % (table_name, search_data))
    elif num_data == '3':
        mysql_set.execute("SELECT * FROM %s where age like '%%%s%%'" % (table_name, search_data))
    elif num_data == '4':
        mysql_set.execute("SELECT * FROM %s where major like '%%%s%%'" % (table_name, search_data))
    elif num_data == '5':
        mysql_set.execute(
            "SELECT * FROM %s where Practicable_computer_languages like '%%%s%%'" % (table_name, search_data))
    elif num_data == '6':
        if search_data == '상':
            level = 'High_level'
        elif search_data == '중':
            level = 'Middle_level'
        elif search_data == '하':
            level = 'Low_level'
        try:
            mysql_set.execute("SELECT * FROM %s where %s like '%%_%%'" % (table_name, level))
        except Exception:
            pass

    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full.append(output)

    if len(output_full) <= 1:
        for parent in output_full:
            print("* %s" % parent[1], end='')
            print("(%s)" % parent[0])
            print("- 성별: %s" % parent[2])
            print("- 나이: %s" % parent[3])
            print("- 전공: %s" % parent[4])
            parent_language = parent[5].split(' ')
            cnt = 0
            level = ''
            if parent_language[0] != '':
                for language_value in parent_language:
                    try:
                        if parent[6].find(language_value) != -1:
                            level = '상'
                        elif parent[7].find(language_value) != -1:
                            level = '중'
                        elif parent[8].find(language_value) != -1:
                            level = '하'
                    except Exception:
                        pass
                    print("> %s, 수준:%s" % (language_value, level))
                    cnt += 1
    else:
        for parent in output_full:
            print("%s (%s, %s, %s)" % (parent[0], parent[1], parent[2], parent[3]))

    print("")


def del_db():
    del_id = input("삭제할 ID를 입력하세요: ")

    if del_id != '':
        try:
            mysql_set.execute("delete from %s where student_id='%s';" % (table_name, del_id))
            con.commit()
        except Exception:
            pass


def update_db():
    update_id = input("수정할 ID를 입력하세요: ")
    num = 1
    value_count = 0
    count = 1
    up_value = ''
    level_value = []
    output_full2 = []
    output_full = []

    mysql_set.execute("SELECT * FROM %s;" % table_name)
    rows = mysql_set.fetchall()
    for row in rows:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full.append(output)

    for parent in output_full:
        if update_id == parent[0]:
            print("%d.이름: %s" % (num, parent[1]))
            num += 1
            print("%d.성별: %s" % (num, parent[2]))
            num += 1
            print("%d.나이: %s" % (num, parent[3]))
            num += 1
            print("%d.전공: %s" % (num, parent[4]))
            num += 1
            parent_language = parent[5].split(' ')
            cnt = 0
            level = ''
            if parent_language[0] != '':
                print("사용 가능한 컴퓨터 언어")
                for language_value in parent_language:
                    level_list = []
                    try:
                        if parent[6].find(language_value) != -1:
                            level = '상'
                        elif parent[7].find(language_value) != -1:
                            level = '중'
                        elif parent[8].find(language_value) != -1:
                            level = '하'
                    except Exception:
                        pass
                    value_count += 1
                    print("%d.언어: %s" % (num, language_value))
                    num += 1
                    print("%d.레벨: %s" % (num, level))
                    level_list.append(language_value)
                    level_list.append(level)
                    level_value.append(level_list)
                    num += 1

    update_info = input("수정할 항목의 번호를 입력하세요: ")
    update_data = input("수정할 값을 입력하세요: ")

    if update_info == '1':
        mysql_set.execute("update student set name='%s' where student_id='%s';" % (update_data, update_id))
    elif update_info == '2':
        mysql_set.execute("update student set sex='%s' where student_id='%s';" % (update_data, update_id))
    elif update_info == '3':
        mysql_set.execute("update student set age=%s where student_id='%s';" % (update_data, update_id))
    elif update_info == '4':
        mysql_set.execute("update student set major='%s' where student_id='%s';" % (update_data, update_id))
    if parent_language[0] != '':
        count += 3
        count2 = 0
        num_of = 0
        list_val = []
        for language_value in parent_language:
            if (int(update_info) <= count + 2 and int(update_info) > count):
                if int(update_info) % 2 == 1:
                    num_of = 1
                    language_value = update_data
                    level_value[count2][0] = update_data
                if int(update_info) % 2 == 0:
                    num_of = 2
                    level_value[count2][1] = update_data

            count += 2
            count2 += 1

            list_val.append(language_value)
        list_val = ' '.join(list_val)

        language_level_hi = []
        language_level_mid = []
        language_level_low = []
        if num_of == 1:
            mysql_set.execute("update %s set Practicable_computer_languages='%s' where student_id='%s';" % (
            table_name, list_val, update_id))

        if num_of == 2 or num_of == 1:
            for language_value in level_value:
                if language_value[1] == '상':
                    language_level_hi.append(language_value[0])
                elif language_value[1] == '중':
                    language_level_mid.append(language_value[0])
                elif language_value[1] == '하':
                    language_level_low.append(language_value[0])
            language_level_hi = ' '.join(language_level_hi)
            language_level_mid = ' '.join(language_level_mid)
            language_level_low = ' '.join(language_level_low)

            mysql_set.execute(
                """update %s set high_level='%s',middle_level='%s',low_level='%s' where student_id='%s';""" % (
                table_name, language_level_hi, language_level_mid, language_level_low, update_id))
    con.commit()
    time.sleep(0.5)

    mysql_set.execute("SELECT * FROM %s;" % table_name)
    rows2 = mysql_set.fetchall()
    for row in rows2:
        output = []
        for column_index in range(len(row)):
            output.append(str(row[column_index]))
        output_full2.append(output)

    for parent in output_full2:
        if update_id == parent[0]:
            print("* %s" % parent[1], end='')
            print("(%s)" % parent[0])
            print("- 성별: %s" % parent[2])
            print("- 나이: %s" % parent[3])
            print("- 전공: %s" % parent[4])
            parent_language = parent[5].split(' ')
            cnt = 0
            level = ''

            if parent_language[0] != '':
                for language_value in parent_language:
                    try:
                        if parent[6].find(language_value) != -1:
                            level = '상'
                        elif parent[7].find(language_value) != -1:
                            level = '중'
                        elif parent[8].find(language_value) != -1:
                            level = '하'
                    except Exception:
                        pass
                    print("> %s, 수준:%s" % (language_value, level))
                    cnt += 1
    print("")
    # con.commit()


def insert_csv():
    try:
        mysql_set.execute('desc %s' % table_name)
    except Exception:
        mysql_set.execute(
            "CREATE TABLE IF NOT EXISTS student(Student_ID VARCHAR(20),Name VARCHAR(20),sex VARCHAR(20),Age int,Major VARCHAR(20),"
            "Practicable_computer_languages VARCHAR(20),High_level VARCHAR(20),Middle_level VARCHAR(20),Low_level VARCHAR(20));")
        con.commit()
    with open('student_info.csv', newline='', encoding='utf-8') as infile:
        data = list(csv.reader(infile))

    sel_op = input("기존데이터가 다 사라지고 csv파일의 데이터를 불러옵니다 하시겠습니까(y/n): ")
    if sel_op == 'y':
        mysql_set.execute("delete FROM %s" % table_name)

        for i in data:
            mysql_set.execute("""INSERT INTO %s VALUES ('%s', '%s','%s', %s, '%s', '%s', '%s', '%s', '%s');"""
                              % (table_name, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        con.commit()


con = MySQLdb.connect(host='localhost', port=3306, db='it_student', user='root', passwd='1111', charset='utf8mb4')
mysql_set = con.cursor()
table_name = 'student'

while True:
    print("학생정보 db데이터 분석 시작..")
    input_data = input("1.요약정보 \n2.입력 \n3.조회 \n4.수정 \n5.삭제 \n6.종료 \n7.데이터입력 \n메뉴 입력: ")
    if input_data == '6':
        print("학생 정보 분석 완료!")
        quit()
    elif input_data == '1':
        sumup_db()
    elif input_data == '2':  # 입력
        insert_db()
    elif input_data == '3':  # 조회
        search_db()
    elif input_data == '4':  # 수정
        update_db()
    elif input_data == '5':  # 삭제
        del_db()
    elif input_data == '7':  # csv파일 insert
        insert_csv()
