# 4
class Restaurant :
    restaurant_name = None
    cuisine_type = None
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) :

        print(f'저희 레스토랑 명칭은 {self.restaurant_name}이고 {self.cuisine_type} 전문점입니다.')

    def open_restaurant(self) :

        print(f'저희 {self.restaurant_name} 레스토랑이 오픈했습니다.')

restaurant_name, cuisine_type = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) :').split()
res = Restaurant(restaurant_name, cuisine_type)
res.describe_restaurant()
res.open_restaurant()


