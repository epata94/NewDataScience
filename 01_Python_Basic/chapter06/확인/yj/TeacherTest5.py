class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def __del__(self):
        print(f'{self.restaurant_name} 문 닫습니다.')
        del self.restaurant_name
        del self.cuisine_type

    def describe_restaurant(self):
        print(f'저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.')

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.")

restaurant_info=[]

for i in range(3):
    restaurant_name,cuisine_type=input("레스토랑 이름과 요리 종류를 선택하세요.[공백으로 구분] 예) 띵호화 중식 : ").split()
    restaurant_info.append(Restaurant(restaurant_name,cuisine_type))
    restaurant_info[i].describe_restaurant()
    restaurant_info[i].open_restaurant()

print("\n 저녁 10시가 되었습니다.\n")

