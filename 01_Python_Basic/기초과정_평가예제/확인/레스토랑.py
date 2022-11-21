import os.path

class Restaurant :

    restaurant_name = cuisine_type = ''
    today_customer = 0
    number_served = 0

    def __init__(self, name, type, number_served) :
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = number_served

    def describe_restaurant(self) :
        print(f'저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.')

    def open_restaurant(self) :
        print(f'저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.')

    def increment_number_served(self, number):
        self.today_customer += number
        self.number_served += number
        self.set_recode()

    def reset_number_served(self):
        self.today_customer = self.number_served = 0
        self.set_recode()

    def check_customer_number(self):
        print(f'오늘 총 {self.today_customer}명 손님께서 오셨습니다. (전체 누적 손님 :{self.number_served})')

    def set_recode(self) :
        try:
            log = open('고객서빙현황로그.txt', mode='w', encoding='utf-8')

            log.write(f'{self.today_customer} {self.number_served}')
        except Exception as e:
            print('Error 발생 : ', e)
        finally:
            log.close()

name, type = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ').split()

try :
    if not os.path.exists('고객서빙현황로그.txt') :
        file = open('고객서빙현황로그.txt', mode='w', encoding='utf-8')

        file.write('0 0')
        file.flush()

    file = open('고객서빙현황로그.txt', mode='r', encoding='utf-8')

    recode = file.readline()

    number_served = 0

    number_served = int(recode[2])

except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()

restaurant = Restaurant(name, type, number_served)

restaurant.describe_restaurant()

open_restaurant = input('레스토랑을 오픈하시겠습니까 ? (y / n) : ')

if open_restaurant == 'y' :
    restaurant.open_restaurant()

    input_order = 0

    while True :
        input_order = input('어서오세요. 몇명이십니까 ? (초기화 : 0, 입력종료 : -1, 누적고객확인 : p) : ')

        if input_order == '0' :
            restaurant.reset_number_served()
        elif input_order == '-1' :
            break
        elif input_order == 'p' :
            restaurant.check_customer_number()
        else :
            print(f'손님 {input_order}명 들어오셨습니다. 자리를 안내해 드리겠습니다.')

            customer_count = int(input_order)

            print(customer_count)

            restaurant.increment_number_served(customer_count)
