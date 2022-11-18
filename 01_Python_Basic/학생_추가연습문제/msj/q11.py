import copy
import random

student_list = ['김유진', '문성준', '박종민', '송지예', '양석훈', '이예지', '임성혁', '한권제', '현재봉', '이현구']

def coffee_lotto(student_list, target_num):
    try:
        result = random.sample(student_list, target_num)

        print('축하합니다!')
        print(' '.join(result), end='')
        print('님 당첨입니다')
    except Exception as e :
        print('잘못된 입력 : ', e)

def presentation_order(student_list):
    except_teacher_list = copy.deepcopy(student_list)

    except_teacher_list.remove('이현구')

    random.shuffle(except_teacher_list)

    print('발표자 순서는 아래와 같습니다')
    print(' '.join(except_teacher_list))


select = ''

while True:
    print('1. 커피로또')
    print('2, 발표자순서')

    select = input('메뉴를 선택하세요 (엔터는 종료) : ')

    if select == '':
        break
    elif select == '1':

        target_num = int(input('당첨자 수를 입력하세요 : '))

        coffee_lotto(student_list, target_num)

    elif select == '2':
        presentation_order(student_list)
