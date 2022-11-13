
class Restaurant:
    def __init__(self):
        self.number = 0
    def reset_number_served(self, persons):
        print(f'손님 {persons}명 들어오셨습니다. 자리를 안내해 드리겠습니다.')

    def increment_number_served(self,persons):
        self.number = self.number + int(persons)

    def check_customer_number(self):
        print(f'지금까지 총 {self.number}명 손님께서 오셨습니다.')


name_type = []
persons = 0
check = ""

name_type = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ').split()
print(f'저희 레스토랑 명칭은 {name_type[0]}이고 {name_type[1]} 전문점입니다.')
check = input('레스토랑을 오픈하시겠습니까? (y/n): ')

if check == 'n':
    exit()
elif check == 'y':
    print(f'저희 {name_type[0]} 레스토랑이 오픈했습니다.')
else:
    print('y또는n만 입력가능합니다.')
    exit()


a = Restaurant()
while 1:
    persons = input('어서오세요. 몇명이십니까?(초기화:0,종료:-1,누적고객 확인:p): ')

    if persons == '0':
        print('손님 카운팅을 0으로 초기화 하였습니다.')
        a = Restaurant()
    elif persons == '-1':
        exit()
    elif persons == 'p':
        a.check_customer_number()
    else:
        a.reset_number_served(persons)
        a.increment_number_served(persons)
        continue




