name = input('이름을 입력하세요.')
def search_visitor(name) :
    with open("방명록.txt", "r", encoding="UTF-8") as file :
        if name in file.read() :
            return name
        return ''

#if search_visitor(name) != '' :
if search_visitor(name) :
        print(f'{name}님 다시 방문해주셔서 감사합니다. 즐거운 시간되세요.')
else :
    rn = input('생년월일을 입력하세요 (예:801212) \n')
    print(f'{name}님 환영합니다. 아래 내용을 입력하셨습니다.')
    print(f'{name} {rn}')

    with open("방명록.txt", "a", encoding="UTF-8") as file:
        file = open('방명록.txt', mode='a', encoding='utf-8')
        file.write(f'\n{name} {rn}')
