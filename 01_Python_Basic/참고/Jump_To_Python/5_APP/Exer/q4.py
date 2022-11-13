class Restaurant:
    def __init__(self,type):
        self.name = type[0]
        self.type = type[1]
    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 '{self.name}'이고 {self.type} 전문점입니다.")
    def open_restaurant(self):
        print(f"저희 {self.name} 레스토랑이 오픈했습니다.")
    def __del__(self):
        print(f'{self.name}레스토랑 문닫습니다.')


total = []
for i in range(3):
    user = input('레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ').split()
    total = total + [user]
    total[i] = Restaurant(user)
    total[i].describe_restaurant()
    total[i].open_restaurant()

print("")

for i in range(3):
    del total[0]



