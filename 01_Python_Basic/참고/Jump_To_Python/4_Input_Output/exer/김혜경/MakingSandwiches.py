message = '''
안녕하세요. 저희 가게에 방문해주셔서 감사합니다.
1. 주문
2. 종료
입력: '''

def input_ingredient():
    ingredient_list = []
    while True:
        ingredient = input("원하시는 재료를 입력하세요: ")

        if ingredient == "종료":
            return ingredient_list
        ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    for ingredient in ingredient_list:
        print("%s를 추가합니다"%ingredient)
    print("여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요^^")

while True:
    welcome = int(input(message))
    if welcome == 1:
        # list = input_ingredient()
        # make_sandwiches(list)
        make_sandwiches(input_ingredient())
        break
    elif welcome == 2:
        break