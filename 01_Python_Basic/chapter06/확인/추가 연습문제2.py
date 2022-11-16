class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val

class UpgradeCalculator(Calculator):

    def __init__(self):
        # Calculator().__init__()
        super().__init__()
        #self.value = 0

    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

cal = Calculator()
cal.add(10)
print(cal.value)