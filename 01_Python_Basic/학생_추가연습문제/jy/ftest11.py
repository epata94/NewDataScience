#11. 4번 문제를 응용해서 우리반 커피쏘는 사람과 발표순서를 제공하는 함수를 만들어보자.
import random

def coffee_lotto(student_list, target_num):
    target_list = []
#    s_list = random.sample(student_list,target_num) * 참고 짧게쓰기
#    print(s_list)
    while len(target_list) < target_num:
        target = random.randint(0, 10)

        if student_list[target] not in target_list:
            target_list.append(student_list[target])

    print(f"축하합니다! {target_list}님 당첨입니다.\n")
def presentation_order(student_list):
    print("발표순서 : \n")

while True:
    option = input("1. 커피로또\n2. 발표자순서\n메뉴를 선택하세요 (엔터는 종료): ")


    if option == "1":
        student_list = ["김유진", "김지혜", "문성준", "박종민", "송지예", "양석훈", "이예지", "임성혁", "한권제", "현재봉", "이현구쌤"]
        print(f"<전체명단>\n{student_list}")

        target_num = int(input("당첨자 수를 입력하세요: "))
        if target_num > len(student_list):
            print("명단초과")
            break
        coffee_lotto(student_list, target_num)

    elif option == "2":
        presentation_order(student_list)

    elif option == "":
        break