class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restaurant(self):
        print(f'저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.')

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.")


restaurant_name,cuisine_type=list(input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split())
restaurant_info=Restaurant(cuisine_type,restaurant_name)
restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()
