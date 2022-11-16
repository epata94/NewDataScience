class FourCal:
    first=second=0

    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        print(f"\nadd() = {self.first+self.second}")

    def sub(self):
        print(f"sub() = {self.first-self.second}")

    def mul(self):
        print(f"mul() = {self.first*self.second}")

    def div(self):
        print(f"div() = {self.first/self.second}\n")

    def setdata(self, first, secode):
        self.first=first
        self.second=secode


first=int(input("__init__ = 첫번째 수 입력 : "))
second=int(input("__init__ = 두번째 수 입력 : "))

a=FourCal(first,second)
a.add()
a.sub()
a.mul()
a.div()


first=int(input("setdata() = 첫번째 수 입력 : "))
second=int(input("setdate() = 두번째 수 입력 : "))

a.setdata(first,second)
a.add()
a.sub()
a.mul()
a.div()
