# 8. 샌드위치 만들기
def input_ingredient():
    ingredient_list = []

    while True:
        ingredient = input('안녕하세요 원하는 재료를 입력하세요 (종료=>"엔터") : ')

        if ingredient == '':
            print()
            return ingredient_list
        else:
            ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    print('샌드위치를 만들겠습니다.')

    for ingredient in ingredient_list:
        print(f'{ingredient} 추가합니다.')

    print('\n여기 주문하신 샌드위치를 만들었습니다. 맛있게 드세요.\n')


while True:
    print('안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.')
    print('1. 주문')
    print('2. 종료')

    select = int(input('입력 : '))

    if select == 2:
        break

    ingredient_list = input_ingredient()

    make_sandwiches(ingredient_list)

