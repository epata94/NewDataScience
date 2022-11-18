import random

def coffee_lotto(student_list, target_num):
    coffee_buyer = []
    i = 0
    while i < target_num:
        rand_num = random.randint(0,len(student_list)-1)
        if student_list[rand_num] not in coffee_buyer:
            coffee_buyer.append(student_list[rand_num])
            i += 1
    print('축하합니다!')
    print(f'{",".join(coffee_buyer)}님 당첨입니다\n')
def presentation_order(student_list):
    presentation_list=[]
    i=0
    while i < len(student_list):
        rand_num = random.randint(0,len(student_list)-1)
        if student_list[rand_num] not in presentation_list:
            presentation_list.append(student_list[rand_num])
            i += 1
    print('발표자 명단은 아래와 같습니다')
    print(f'{" ".join(presentation_list)}\n')


while True:
    student_list = ['김유진', '문성준', '박종민', '송지예', '양석훈', '이예지', '임성혁', '한권제', '현재봉']
    teacher = '이현구'
    option=input("\t1. 커피로또\n\t2. 발표자 순서\n메뉴를 선택하세요 (엔터는 종료) : ")
    if option=='1':
        student_list.append(teacher)
        print(f'<전체명단>')
        print(f'{" ".join(student_list)}')
        target_num=int(input("당첨자 수를 입력하세요: "))
        coffee_lotto(student_list,target_num)
    elif option=='2':
        print(f'<전체명단>')
        print(f'{" ".join(student_list)}')
        presentation_order(student_list)
    elif option == '':
        print('프로그램을 종료합니다')
        break
    else:
        print('잘못된 접근입니다')
        break