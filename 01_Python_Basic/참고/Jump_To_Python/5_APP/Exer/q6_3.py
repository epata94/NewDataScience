class Restaurant:
    def __init__(self):
        self.todays_customer = 0
        file_log = open("고객서빙현황로그.txt",'r')
        self.total = file_log.read()
        file_log.close()
    def reset_number_served(self, persons):
        print(f'손님 {persons}명 들어오셨습니다. 자리를 안내해 드리겠습니다.')

    def increment_number_served(self,persons):
        self.todays_customer = self.todays_customer + int(persons)

    def check_customer_number(self):
        print(f'오늘방문자 수는 {self.todays_customer}명 입니다.')
        print(f'지금까지의 누적 방문자수는 {self.todays_customer+int(self.total)}명 입니다.')

    def initialization(self):
        while 1:
            self.gg = int(input('오늘포함 총 누적고객초기화:0, 오늘 방문자수만 초기화:1 선택: '))
            if self.gg == 0:
                # file 포인터를 1개로 작성
                file_log = open("고객서빙현황로그.txt", 'w')
                file_log.write("0")
                file_log.close()
                self.total = 0
                self.todays_customer = 0
                break
            elif self.gg == 1:
                self.todays_customer = 0
                break
            else:
                print('0과1중에 선택하여주세요')
                print("")
                continue

    def __del__(self):
        file_log = open("고객서빙현황로그.txt", 'w')
        file_log.write(str(self.todays_customer + int(self.total)))
        file_log.close()
        print(f'{name_type[0]} 레스토랑 문닫습니다.')
        print('이용해주셔서 감사합니다.')




# 여기서부터 시작!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
try:
    file_log = open("고객서빙현황로그.txt",'r')
except FileNotFoundError:
    file_log = open("고객서빙현황로그.txt", 'w')
    file_log.write('0')
    file_log.close()


a = Restaurant()
name_type = []
persons = 0
check = ""

name_type = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ').split()
print(f'저희 레스토랑 명칭은 {name_type[0]}이고 {name_type[1]} 전문점입니다.')

while 1:
    check = input('레스토랑을 오픈하시겠습니까? (y/n): ')
    if check == 'n':
        del a
        break
    elif check == 'y':
        print(f'저희 {name_type[0]} 레스토랑이 오픈했습니다.')
    else:
        print('y 또는 n 만 입력')
        print('')
        continue
    while 1:
        persons = input('어서오세요. 몇명이십니까?(누적고객초기화:0, 종료:-1, 누적고객 확인:p): ')
        if persons == '0':
            a.initialization()
        elif persons == '-1':
            del a
            exit()
        elif persons == 'p':
            a.check_customer_number()
        else:
            a.reset_number_served(persons)
            a.increment_number_served(persons)
            print("")
            continue
        print("")




