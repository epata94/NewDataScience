class FourCal:
    def __init__(self, first, second):
        self.fisrt = first
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

a = FourCal(4,2)
b = FourCal(3,8)
a.print_number()
b.print_number()
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

a.setdata(9,4) # setXXX 관련 함수가 있기 때문에 원하는 연산을 초기화하여 다시
               # 수행 할 수 있다.
b.setdata(382,48)
a.print_number()
b.print_number()
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
