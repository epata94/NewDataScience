user_input = '''임꺽정 900327
# 홍길동 871021'''
# f = open('방명록.txt', 'w')
# f.write(user_input)
# f.write("\n")
# f.close()
name = input('이름을 입력하세요: ')
def check_visitior(name):
    with open('방명록.txt','r') as f:
        if f.read().find(name) != -1:
            print('{0}님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요^^'.format(name))
            return
        else:
            date_of_birth = input('생년월일을 입력하세요 (ex:801212) : ')
            register(name, date_of_birth)

def register(name, date_of_birth):
    print('{0}님 환영합니다. 아래 내용을 입력하셨습니다.'.format(name))
    print('{0}{1}'.format(name, date_of_birth))
    with open('방명록.txt', 'a')as f:
        f.write('\n{}''{}'.format(name, date_of_birth))

check_visitior(name)