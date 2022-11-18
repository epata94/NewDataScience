def all_gugu():

    dan = input('원하는 단을 입력하세요 (예:2, 전체:all) : ')

    if dan == 'all' :
        for i in range(2, 10):
            for j in range(1, 10) :
                print(i*j, end='\t')
            print()
    else :
        for i in range(1, 10):
            print(i*int(dan), end='\t')

all_gugu()
