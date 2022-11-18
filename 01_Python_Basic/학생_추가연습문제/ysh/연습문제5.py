
def gugu(dan):
    for num in range(1,10):
        #print(num)
        result = int(dan) * num
        print(result,end='\t')

dan = input("원하는 단을 입력하세요")
#dan = '2'
#print(int(dan)* 2 )
gugu(dan)
#print(gugu(dan))