# 7개 라인 실행문
def say_hello(name) :
    print(name + "님 안녕하세요.")
    print("교실에 입장하셨습니다.")
    print("출석체크하세요.")
    print("오늘도 화이팅입니다.\n")

student_list = ["James","Bruno","Evan","George","Henry"]

for name in student_list:
    say_hello(name)