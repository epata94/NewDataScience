class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def print_number(self):
        print("first: %d, second: %d"%(self.first, self.second))

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self): # 메서드 오버라이딩: 자식 클래스에서 부모 클래스의 멤버함수를
                   # 재정의
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# parent = FourCal(4,0)
# print(parent.div())

child = MoreFourCal(4,0)
print(child.div())
# print(child.add())
# print(child.pow())
#
# a.pow() # 부모 클래스에서 자식클래스의 멤버 함수를 호출 할 수 없다.
