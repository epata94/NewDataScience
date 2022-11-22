import io
# import os
# print(os.getcwd())

mileage_data = {'kim99': 12000, 'lee66': 11000, 'han55': 3000, 'hong55': 5000, 'hwang33': 18000}
class mileage_class:

    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.mileage_dict = mileage_data
        # try:
        #     self.mileage_dict = {}
        #     with open('mileage.txt','r',encoding='utf-8') as file:
        #         self.mileage_dict = file.read().split(',')
        #         print(self.mileage_dict)
        # except Exception as e:
        #     self.mileage_dict = mileage_data
        #     print(f"파일 읽기 오류: {e}")

    def display(self):
        print(self.mileage_dict)
        for client in self.mileage_dict:
            print(f"아이디: {client}, 마일리지: {self.mileage_dict[client]}점")

    def update(self):
        self.mileage_dict[self.id] = self.value
        for key in self.mileage_dict:
            if key == self.id:
                print(f"{key}님의 마일리지가 {self.mileage_dict[self.id]}점으로 수정되었습니다.")
        print(f"전체 딕셔너리 : {self.mileage_dict}")
        #return self.id,self.value,self.mileage_dict   #질문
    def add(self):
        self.mileage_dict[self.id] = self.value
        print(f"{self.id}님의 마일리지({self.value}점)가 추가되었습니다")
        print(f"전체 딕셔너리 : {self.mileage_dict}")

    def max(self):
        max_value = 0
        print(self.mileage_dict)
        for item in self.mileage_dict.items():
            if max_value < item[1]:
                max_value = item[1]
                target_id = item[0]
            else:
                pass
        print(f"{target_id}님의 {self.mileage_dict[target_id]}점이 가장 높은 점수입니다")

    def __del__(self):
        print('마일리지 프로그램 종료')
        # try:
        #     #with open("mileage.txt", 'a',encoding='utf-8') as mileage_file:
        #     #    mileage_file.write(f"{self.mileage_dict}")
        # except Exception as e:
        #     print(f'파일 쓰기 오류: {e}')

while True:
    command = int(input("사용하실 마일리지 메뉴를 선택하세요(1:고객정보 확인 2:마일리지 수정 3:고객정보 추가 4:마일리지 최대값확인 -1: 종료)"))
    mileage = mileage_class(' ',' ')  # 질문
    if command ==1:
        mileage.display()
    elif command ==2:
        id,value = input('수정할 고객 아이디와 마일리지를 입력하세요. (예: han55 5000)').split()
        mileage = mileage_class(id,value)
        mileage.update()
    elif command == 3:
        id,value = input('추가할 고객 아이디와 마일리지를 입력하세요. (예: han55 5000)').split()
        mileage = mileage_class(id,value)
        mileage.add()
    elif command == 4:
        mileage.max()
    elif command == -1:
        break