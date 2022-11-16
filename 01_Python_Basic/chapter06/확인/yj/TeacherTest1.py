class FourCal:
    #cons
    def __init__(self,first=0,second=0):
        self.first=first
        self.second=second

    #method
    def add(self):
        print(self.first+self.second)

    def mul(self):
        print(self.first*self.second)

    def sub(self):
        print(self.first-self.second)

    def div(self):
        print(self.first/self.second)

    def setdata(self,first,second):
        self.first = first
        self.second = second

a=FourCal()
b=FourCal(3,8)
a.setdata(4,2)
a.add()
a.mul()
a.sub()
a.div()
b.div()
b.add()
b.mul()
b.sub()