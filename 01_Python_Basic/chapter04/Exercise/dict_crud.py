menu={'자장면':4000,'짬뽕':5000,'볶음밥':5500,'탕수육':8000}

#def menu_print():
#    count=0
#    print("\n<메뉴판 출력>\n")
#    for key in menu.keys():
#        count += 1
#        print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")

while True:

    number=int(input("\n어서 오세요, 기능을 입력하여 주세요 ( 메뉴판 출력 : 1 , 메뉴 추가 : 2 , 메뉴 수정 : 3, 메뉴 삭제 : 4, 프로그램 종료 : -1 ) : "))

    if number==1:
        #menu_print()
        count=0
        print("\n<메뉴판 출력>\n")
        for key in menu.keys():
            count+=1
            print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key],',')}원")
    elif number==2:
        #menu_print()
        count = 0
        print("\n<메뉴판 출력>\n")
        for key in menu.keys():
            count += 1
            print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
        new_menu=input("\n추가 할 메뉴를 입력하여 주세요 : ")
        if new_menu in menu:
            print("이미 해당 메뉴가 존재 합니다\n")
            continue
        menu_price=int(input("가격을 입력하여 주세요 : "))
        menu[new_menu]=menu_price
        print("\n신메뉴가 추가 되었습니다.")
        #menu_print()
        count = 0
        print("\n<메뉴판 출력>\n")
        for key in menu.keys():
            count += 1
            print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
    elif number==-1:
        print("\n감사합니다, 또 오세요.")
        quit()
    elif number==3:
        count = 0
        print("\n<메뉴판 출력>\n")
        for key in menu.keys():
            count += 1
            print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
        update_menu=input("\n수정할 메뉴를 입력하여 주세요 : ")
        if update_menu in menu:
            menu[update_menu]=int(input("\n새 가격을 입력하여 주세요 : "))
            count = 0
            print("\n<메뉴판 출력>\n")
            for key in menu.keys():
                count += 1
                print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
        else:
            print("존재 하지 않는 메뉴 입니다.")
            continue
    elif number==4:
        count = 0
        print("\n<메뉴판 출력>\n")
        for key in menu.keys():
            count += 1
            print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
        delete_menu = input("\n삭제할 메뉴를 입력하여 주세요 : ")
        if delete_menu in menu:
            del menu[delete_menu]
            count = 0
            print("\n<메뉴판 출력>\n")
            for key in menu.keys():
                count += 1
                print(f"{count}번 메뉴 : {key},\t가격 : {format(menu[key], ',')}원")
            print("\n 해당 메뉴가 삭제 되었습니다.")
        else:
            print("존재 하지 않는 메뉴 입니다.")
            continue
    else:
        continue
