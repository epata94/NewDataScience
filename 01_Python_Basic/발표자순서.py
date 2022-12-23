import random
import itertools

def coffee_lotto(student_list, target_num):

    temp_student_list = random.sample(student_list, target_num)

    temp_student_list = ' '.join(temp_student_list)

    print(f'\n축하합니다\n{temp_student_list} 당첨입니다.')

    print('\n프로그램 종료\n재 실행')

def get_n(student_list, target_num):

    temp_student_list = random.sample(student_list, target_num)

    return temp_student_list



def presentation_order(student_list):


    join_student_list = ' '.join(student_list)

    print("\n< 학생 명단 >")
    print(join_student_list)

    print("\n발표자 순서는 아래와 같습니다.")


    select_student = random.sample(student_list, len(student_list))

    join_student_list = ' '.join(select_student)
    print(join_student_list)

def combination_group(student_list, n):
    print('조별 그룹 명단')
    while True:
        num_of_remain = len(student_list)
        if num_of_remain > 0 and num_of_remain < n:
            print(f'남은 사람: {student_list} <= 마지막 조에 편입')
            break

        # groups = itertools.combinations(student_list,n)
        if not student_list:
            break;
        groups = get_n(student_list,n)

        if not groups:
            break;
        print(groups)
        for student in groups:
            student_list.remove(student)

while True:

    select = input("\n\t1. N명 선정\n\t2. 발표자 순서\n\t3. N명 조합\n\n 메뉴를 선택하세요 ( 엔터는 종료 ) : ")

    # student_base_list = ['김유진','김지혜', '문성준', '박종민', '송지예', '양석훈', '이예지', '임성혁', '한권제', '현재봉']
    # student_base_list = ['김유진','김지혜', '박종민', '송지예', '양석훈', '한권제', '현재봉']
    student_base_list = ['김지혜','박종민','송지예']
    class_all_list = student_base_list[:]
    class_all_list.append('이현구')

    if select == '1':
        target_num=int(input("선정자 수를 입력 하세요 : "))
        coffee_lotto(class_all_list, target_num)

    elif select == '2':
        presentation_order(student_base_list)
    elif select == '3':
        target_num = int(input(" 그룹 인원수를 입력 하세요 : "))
        combination_group(student_base_list,target_num)

    else:
        quit()