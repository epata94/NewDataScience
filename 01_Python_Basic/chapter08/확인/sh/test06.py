def search_visitor(check_name):
    with open("방명록.txt","r",encoding="UTF-8") as file:
        names=file.readlines()
        visitor=[]
        for name in names:
            for check in name.split():
                visitor.append(check.strip())
        if check_name in visitor:
            return check_name
        else:
            return ""

name=input('이름을 입력하세요  ( 예 : 홍길동 )  : ')

name_check=search_visitor(name)
if name_check != "":
    print(f'{name}님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요.')
else:
    birthday=int(input('생년월일을 입력 하세요 ( 예 : 801212 ) : '))
    with open("방명록.txt",'a',encoding='UTF-8') as file:
        file.write(f"\n{name} {birthday}")
    print(f"{name}님 환영합니다. 아래 내용을 입력하셨습니다.")
    print(f"{name} {birthday}")

