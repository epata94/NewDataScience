def gugu(dan):
    for num in range(1,10):
        #print(num)
        result = int(dan) * num
        print(result,end='\t')
def all_gugu(dan):
    if dan == 'all':
        for i in range(2,10):
            gugu(i)
            print()
    else:
        for num in range(1, 10):
            result = int(dan) * num
            print(result,end='\t')

dan = input("원하는 단을 입력하세요(예: 2,전체: all)")
#dan = '2'
all_gugu(dan)
