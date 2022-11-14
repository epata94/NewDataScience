from xml.etree.ElementTree import parse

def sumup_xml():
   tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
   note = tree.getroot()
   count=0
   sex = []
   lan_cnt=0
   cnt_level=0
   cnt_python=0
   age_20=[]
   age_30=[]
   age_40=[]
   major_cnt=0
   boy=0
   girl=0
   for parent in note.getiterator("student"):
       sex.append(parent.get("sex"))
       if parent.get("sex").find('남') != -1:
           boy += 1
       elif parent.get("sex").find('여') != -1:
           girl += 1

       if int(parent.findtext("age"))<30:
           age_20.append(parent.get("name")+':'+parent.findtext("age"))
       elif int(parent.findtext("age"))<40:
           age_30.append(parent.get("name")+':'+parent.findtext("age"))
       elif int(parent.findtext("age"))<50:
           age_40.append(parent.get("name")+':'+parent.findtext("age"))

       if parent.findtext("major").find("컴퓨터")!=-1 or parent.findtext("major").find("통계")!=-1:
           major_cnt += 1
       for cont in parent.getiterator("practicable_computer_languages"):
          if cont:
               lan_cnt += 1
       for language_value in parent.getiterator("language"):
           if language_value:
               if language_value.get("name").find("python")!=-1:
                   cnt_python+=1
               if language_value.get("level").find("상")!=-1:
                   cnt_level+=1
       count+=1



   print("* 전체 학생수:%d"%count)
   print("* 성별\n - 남학생: %s명(%s%%)\n - 여학생: %s명(%0.1f%%)"%(boy,boy/int(len(sex))*100,girl,girl/int(len(sex))*100))
   print('* 전공여부')
   print("- 전공자(컴퓨터 공학, 통계): %s명 (%s%%)" % (major_cnt,(major_cnt/count)*100))
   print("- 프로그래밍 언어 경험자: %s명 (%s%%)" % (lan_cnt,(lan_cnt/count)*100))
   print("- 프로그래밍 언어 상급자: %s명 (%s%%)" % (cnt_level,(cnt_level/count)*100))
   print("- 파이썬 경험자: %s명 (%s%%)"% (cnt_python,(cnt_python/count)*100))
   print('* 연령대')
   print('- 20대: %s명 (%s%%) %s' %(len(age_20),(len(age_20)/count)*100,age_20))
   print('- 30대: %s명 (%s%%) %s' %(len(age_30),(len(age_30)/count)*100,age_30))
   print('- 40대: %s명 (%s%%) %s' %(len(age_40),(len(age_40)/count)*100,age_40))
   print("")

def whole_xml():
   tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
   note = tree.getroot()
   for parent in note.getiterator("student"):
       print("* %s"%parent.get("name"))
       print("- 성별: %s"%parent.get("sex"))
       print("- 나이: %s"%parent.findtext("age"))
       print("- 전공: %s"%parent.findtext("major"))
       for language_value in parent.getiterator("language"):
           if language_value:
               for period_value in language_value.getiterator("period"):
                   print("> %s 학습기간:%s,level:%s"%(language_value.get("name"),period_value.get("value"),language_value.get("level")))

   print("")
while True:
    print("학생정보 XML데이터 분석 시작..")
    input_data=input("1.요약정보 \n2.전체데이터 조회 \n3.종료 \n메뉴입력: ")
    if input_data=='3':
        print("학생 정보 분석 완료!")
        quit()
    elif input_data=='2':
        whole_xml()
    elif input_data == '1':
        sumup_xml()