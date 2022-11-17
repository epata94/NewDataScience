# 4.	[인사하기]
# 프로그램 입력 변수에 영어 이름을 아래와 같이 입력한다.
# python greet_user.py janny hannah margot kevin min
# 콘솔에 아래와 같이 출력한다.
# Hello, Janny!
# Hello, Hannah!
# Hello, Margot!
# Hello, Kevin!
# Hello, Min!
# 프로그램작성 조건
# - 이름의 첫글자를 대문자로 변경한다. upper() 사용
# - greet_users(usernames) 함수를 작성한다.
#  > usernames: 문자열 리스트
#  > 인사 메세지를 사람마다 출력한다.


import sys
usernames=sys.argv[:]

def greet_user(usernames):
    for name in usernames:
        # greet_users(usernames)
        name = name[0].upper() + name[1:] #name=name.capitalize
        print(f"Hello, {name}!")

greet_user(usernames)


