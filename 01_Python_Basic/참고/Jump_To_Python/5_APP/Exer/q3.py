class Restaurant:
    def __init__(self,type):
        self.name = type[0]
        self.type = type[1]
    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 '{self.name}'이고 {self.type} 전문점입니다.")
    def open_restaurant(self):
        print(f"저희 {self.name} 레스토랑이 오픈했습니다.")




name_type = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ')
name_type = name_type.split()
a = Restaurant(name_type)
a.describe_restaurant()
a.open_restaurant()