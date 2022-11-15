charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}
# {
#     'abc':2,'code':1,'band':2
# }
for key in charset:
    # get()함수 : key 이용 value 가져오기
    wc[key] = wc.get(key, 0) + 1  # get() 이용

print(wc)

{
    "국어":100,
    "영어":95,
    "수학":98
}