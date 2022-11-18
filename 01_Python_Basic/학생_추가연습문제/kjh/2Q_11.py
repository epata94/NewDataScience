import random

def coffee_lotto(student_list, target_num):
    # names = ["김유진", "문성준", "박종민", "송지예", "양석훈", "이예지", "임성혁", "한권제", "현재봉", "이현구"]

    # win = int(input("당첨자 수를 입력하세요 : "))

    # for i in range(win):
    #     name = random.randint(int(names))
    #
    #     while name in names:
    #         name = random.randint(names)
    #
    #     names.append(name)

    name = random.sample(student_list, target_num)

    print("축하합니다!")
    print(f"{' '.join(name)}님 당첨입니다.")



def presentation_order(student_list):
    name = random.sample(student_list, len(student_list))

    print("발표자 순서는 아래와 같습니다.")
    print(' '.join(name))



while True:
    select_num = input("1. 커피로또\n2. 발표자순\n메뉴를 선택하세요 (엔터는 종료) : ")
    student_list = ["김유진", "문성준", "박종민", "송지예", "양석훈", "이예지", "임성혁", "한권제", "현재봉"]

    if select_num == '1':
        student_list.append("이현구")
        target_num = int(input("당첨자 수를 입력하세요 : "))
        coffee_lotto(student_list, target_num)

    elif select_num == '2':
        presentation_order(student_list)

    else:
        quit()