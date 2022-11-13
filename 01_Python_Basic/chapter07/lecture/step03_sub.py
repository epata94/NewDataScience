from re import sub

# 3.sub(pattern, repl, string)
# 텍스트 전처리 용도
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# ^ 앞부분에 \를 붙이는 이유 : ^가 메타문자가 아닌 특수문자로 인식(\특수문자)
# 이스케이프 문자인 경우 : \\이스케이프문자

# (1) 특수문자 제거
text1 = sub('[\^*$]+', '', st3)
print(text1)
# text : test홍길동 abc 대한민국 123tbc

# (2) 숫자 제거
text2 = sub('[0-9]', '', text1)
print(text2)
# test홍길동 abc 대한민국 tbc

