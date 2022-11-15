def input_ingredient():
    temp=input("안녕하세요. 원하시는 재료를 입력 하세요 ( 입력 종료 -> '종료' ) : ")
    sandwiches_list=[]
    while True:
        if temp=='종료':
            return sandwiches_list
        else:
            sandwiches_list.append(temp)
            temp = input("안녕하세요. 원하시는 재료를 입력 하세요 ( 입력 종료 -> '종료' ) : ")


def make_sandwiches(ingredient_list):
    print("\n샌드위치를 만들겠습니다.\n")
    for ingredient in ingredient_list:
        print(f"{ingredient}를 추가합니다.")
    print("\n여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요\n")

while True:
    print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.")
    state=int(input("1. 주문\n2. 종료\n입력 : "))
    if state==1:
        sandwiches_list=input_ingredient()
        make_sandwiches(sandwiches_list)
    else:
        quit()
