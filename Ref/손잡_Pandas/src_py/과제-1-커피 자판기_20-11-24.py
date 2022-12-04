class vend_machine:
    def __init__(self):
        self.total_money=0
        self.in_money = 0  
        self.product = ('커피','라떼','생수')
        self.sel = 0
        self.price = ('200','300','400')
        self.coffee_count = 0
        self.latte_count = 0
        self.water_count = 0
    
    def input_money(self):
        self.in_money = int(input('돈을 넣어주시오.'))
    
    def get_drink(self):
        if sel == 1 and self.in_money >= 200:
            print("%s 나왔습니다." % self.product[sel-1])
            self.in_money = self.in_money - int(self.price[sel-1])           
            self.coffee_count = self.coffee_count + 1



        elif sel == 2 and self.in_money >= 300:
            print("%s 나왔습니다." % self.product[sel-1])
            self.in_money = self.in_money - int(self.price[sel-1])         
            self.latte_count = self.latte_count + 1



        elif sel == 3 and self.in_money >= 400:
            print("%s 나왔습니다." % self.product[sel-1])
            self.in_money = self.in_money - int(self.price[sel-1])         
            self.water_count = self.water_count + 1


        else :
            if sel ==  0 :
                print()
                    
            
            else :
                print("잘못된 선택입니다.")



        print("잔돈 %d원 있습니다." % self.in_money)
        print()


            
    
    def get_describe(self):
        print('커피는 %s잔, %s원 어치 판매되었습니다.' %(self.coffee_count,self.coffee_count*200))
        print('라떼는 %s잔, %s원 어치 판매되었습니다.' %(self.latte_count,self.latte_count*300))
        print('생수는 %s잔, %s원 어치 판매되었습니다.' %(self.water_count,self.water_count*400))


vm = vend_machine()
vm.input_money()
while True :
    sel = int(input('"원하는 음료를 고르시오. 1:커피 ,2:라떼 3:생수 0:종료 " : '))
    if int(vm.in_money) >= int(min(vm.price)) :
        vm.get_drink()
        print()
    
        if sel == 0 :
            print("%d원을 반환합니다." %vm.in_money)
            vm.get_describe()
            break
        
    else : 
        vm.get_describe()
        break
        
