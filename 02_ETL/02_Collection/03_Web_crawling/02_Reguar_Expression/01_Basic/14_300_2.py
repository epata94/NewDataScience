import re
original_text='life is too short'
p=re.compile('[a-z]+')

m = p.search(original_text)
print(m)

match_list = p.findall(original_text)
# 검색 결과는 매칭된 문자열들을 리스트로 반환한다.
print(match_list)
for match_element in match_list:
    print(match_element)