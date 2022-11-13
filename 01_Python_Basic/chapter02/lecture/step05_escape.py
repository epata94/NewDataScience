# 3. escape 처리 : 특수기능('', "",\n, \t)으로 부터 탈출[차단]
'''
escape : 탈출하다, 기능 차단(어떤 기능으로 부터 벗어나다.)
'''
# escape 기능 차단
print('escape 문자 차단 ')
print('\n출력 이스케이프 문자') # \n : 줄 바꿈 기능

print('\\n출력 이스케이프 차단1') # escape 기능 차단1 - \
print(r'\n출력 이스케이프 차단2') # escape 기능 차단2 - r

#경로 표현  : C:\Python\test
print('path =', 'C:\Python\test')
print('path =', 'C:\\Python\\test')
print('path =', r'C:\Python\test')
'''
path = C:\Python    est
path = C:\Python\test
path = C:\Python\test
'''

# 문) c:\'aa'\"abc.txt" 출력되도록 하시오.
print("c:\\\'aa\'\\\"abc.txt\"") #  c:\'aa'\"abc.txt"

