'''
재귀호출(recursive call)
 - 함수 내부에서 자신의 함수를 반복적으로 호출하는 기법
 - 조건 : exit 조건  
 - 용도 : 반복적으로 변수를 조금씩 변경하여 연산
   ex) 5! = 1*2*3*4*5
'''

# (1) 1~n 카운트(n=5: 1 2 3 4 5)
def Counter(n):
    if n == 0 :
        return 0 # exit 조건 
    else :
        Counter(n-1) # 5(first) -> 4(5-1) -> 3(4-1) -> 2(3-1) -> 1(2-1) [0(1-1)]
        '''
        stack(5, 4, 3, 2, 1) : LIFO
        return 값은 stack 저장되지 않음 
        '''
        print(n, end = ' ') # 중복 출력
        # 1 2 3 4 5  

# 함수 호출1
print('n=0 : ', Counter(0)) # n=0 :  0
# 함수 호출2
Counter(5)

print()

# (2) 1~n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n == 1 : # n=1 -> exit 조건 
        return 1
    else :
        # 재귀호출 
        result = n + Adder(n-1) 
        # 5(first)->4(5-1) -> 3(4-1) -> 2(3-1) | [1(2-1)] 
        '''
        1. stack(5, 4, 3, 2)
        2. 덧셈 : 1 + [2 + 3 + 4 + 5 ]         
        '''   
        print(n, end = ' ')   # 2 3 4 5   
        return result # 15
    
print('n=1 :', Adder(1)) # n=1 : 1
print('\nn=5 :', Adder(5)) # n=5 : 15
        

# 3. myData 생성 

data = [[1,2,3], [4,5,6]] # [[1col], [2col]] 
cols = ['one', 'tow']
myData = {} # dict - {'one' : [1,2,3], 'tow' : [4,5,6]}

print(len(data), len(cols)) # 2

size = len(data) # 2
for i in range(size) : # 0~1 
    myData[cols[i]] = myData.get(cols[i], data[i])# {'one':value}
    # dict.get(key, value)

print(myData) # {'one': [1, 2, 3], 'tow': [4, 5, 6]}


# 재귀호출 : data 생성
def createData(size): # size = 2
    myData2 = {} 
    
    if size == 0 :
        return 
    else :
        # 재귀호출 
        for i in range(size) :
            createData(size-1)
            myData2[cols[i]] = myData2.get(cols[i], data[i])
            
        return myData2
        
myData2 = createData(len(cols)) # 2
print(myData2) # # {'one': [1, 2, 3], 'tow': [4, 5, 6]}

    
    








        
    
    