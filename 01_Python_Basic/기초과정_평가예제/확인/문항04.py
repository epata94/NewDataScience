import os

class Restaurant:
    restaurant_name = ''
    cuisine_type = ''
    number_served = 0
    today_customer = 0
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        files=os.listdir()
        if "고객서빙현황로그.txt" in files:
            with open("고객서빙현황로그.txt","r",encoding="UTF-8") as file:
                customer_list=file.readlines()[-1].split()
                self.number_served=int(customer_list[1])
    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 '{self.restaurant_name}'이고 {self.cuisine_type} 전문점입니다.")
        select = input('레스토랑을 오픈 하시겠습니까? (y/n) : ')
        if select =='n' or select =='N':
            quit()

    def open_restaurant(self):
        print(f'저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.')

    def reset_number_served(self,number):
        self.today_customer=number
        print(f"\n금일 손님 입장 횟수를 {number}으로 초기화 하였습니다.")

    def increment_number_served(self,number):
        self.number_served += number
        self.today_customer += number
        print(f'손님 {number}명 들어오셨습니다. 자리를 안내해 드리겠습니다.')

    def check_customer_number(self):
        print(f'오늘 총 {self.today_customer}명 손님께서 오셨습니다. (전체 누적 손님 : {self.number_served})')

    def __del__(self):
        print("소멸자 호출")
        with open("고객서빙현황로그.txt","a",encoding="UTF-8") as file:
            file.write(f'{self.today_customer}\t{self.number_served}\n')

restaurant_name, cuisine_type=input("레스토랑 이름과 요리 종류를 선택 하세요 (공백으로 구분) 예) 띵호와 중식 : ").split()

restaurant=Restaurant(restaurant_name,cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

while 1:

    customerCount=input("\n어서오세요. 몇명이십니까?(초기화 : 0, 종료 : -1, 누적 고객 확인 : p) : ")

    if customerCount == '-1':
        print(f"{restaurant_name} 레스토랑 문 닫습니다.")
        # with open("고객서빙현황로그.txt","a",encoding="UTF-8") as file:
        #     file.write(f'{restaurant.today_customer}\t{restaurant.number_served}\n')
        # quit()
        break

    elif customerCount == '0':
        restaurant.reset_number_served(0)

    elif customerCount.isdigit():
        customerCount=int(customerCount)
        restaurant.increment_number_served(customerCount)

    elif customerCount == 'p':
        restaurant.check_customer_number()

del restaurant
print('End')
