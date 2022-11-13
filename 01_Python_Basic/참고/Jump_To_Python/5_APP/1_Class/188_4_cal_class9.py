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

a = FourCal(4,2)
print(a.add())
child = MoreFourCal(2,3)

child.print_number()
print(child.add())
print(child.pow())

a.pow() # 부모 클래스에서 자식클래스의 멤버 함수를 호출 할 수 없다.
