import re
pattern = re.compile('[abc]') # compile에는 정규식

match_result = pattern.match('a') # match안에는 원본 문자열
print(match_result)
# <re.Match object; span=(0, 1), match='a'> <= Match object 반환
# span안의 숫자는 매칭되는 구간
# match는 매칭이 되는 문자열

match_result = pattern.match('before')
print(match_result)

match_result = pattern.match('dude')
print(match_result)
# 매칭이 되지 않는다면 None을 반환한다.

match_result = pattern.match('Sang')
print(match_result)

pattern = re.compile('S[abc]') # 기본 정규식 문법을 적용하였을 경우
# 문자열 클래스는 매칭이되는 순서를 고려해야 한다.
match_result = pattern.match('Sang')
print(match_result)

pattern = re.compile('s[abc]') # 정규식은 대소문자를 구분한다.
match_result = pattern.match('Sang')
print(match_result)
