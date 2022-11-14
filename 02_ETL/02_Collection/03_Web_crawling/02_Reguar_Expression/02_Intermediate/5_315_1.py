import re
p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
p = re.compile(r'(?P<name>\w+)\s+(?P<first_numbers>\d+)[-]\d+[-]\d+')
p = re.compile(r"""         # 원문이 'park 010-1234-5678' 일 경우에
(?P<name>\w+)\s+            # 이름과 공백문자가 매칭이 되는 정규식: 'park ' 매치
(?P<first_numbers>\d+)      # 첫번째 전화번호 그룹: 010 매치
[-]                         # 첫번째 전화번호 그룹 다음에 반드시 '-' 문자가 와야함
(?P<second_numbers>\d+)     # 두번째 전화번호 그룹: 1234 매치
[-]                         # 그 다음에 반드시 '-' 문자가 와야함
(?P<third_numbers>\d+)      # 세번째 전화번호 그룹: 5678 매치
""", re.VERBOSE)
m = p.search('park 010-1234-5678')
print(m.group('name'))
print(m.group('first_numbers'))
print(m.group('second_numbers'))
print(m.group('third_numbers'))
