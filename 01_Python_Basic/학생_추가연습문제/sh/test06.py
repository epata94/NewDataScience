def all_gugu(dan):
    if dan == 'all':
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i*j}\t',end = '')
            print()
    # elif dan.isdigit():
    else:
        dan = int(dan)
        for i in range(dan, dan * 10, dan):
            print(f'{i}\t', end = '')

dan = input("원하는 단을 입력 하세요 (예:2, 전체 : all) :")
all_gugu(dan)