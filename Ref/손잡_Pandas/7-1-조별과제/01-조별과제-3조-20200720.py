class Admin:
    __pwd = "admin"
    def pwdComfirm(self, pwd):
        if pwd == self.__pwd:
            return True
        else:
            return False
    def printAdminPage(self, vm):
        sel = 0
        while sel != 3:
            print("=" * 20)
            print("\t\tWelcome to ADMIN PAGE\t\t")
            vm.printAllMenu()
            print("1. 품목 추가")
            print("2. 품목 삭제")
            print("3. 종료")
            print("=" * 20)
            sel = int(input("작업하시고자 하는 번호를 입력하시오 :"))
            if sel == 1:
                item_name = input("추가하고자 하는 물품의 이름을 기입하시오 : ")
                if item_name in vm.ItemNames:
                    print("동일한 이름의 품목이 존재합니다.\n다시 시도해주세요.")
                    continue
                if vm.checkMenu(item_name) == False:
                    while True:
                        item_price = int(input("추가하고자 하는 물품의 가격을 기입하시오 : "))
                        print("물품 이름 :", item_name)
                        print("물품 가격 :", item_price)
                        ans = input("종료를 원하면 'q'를 입력해주세요.\n추가하고자하는 정보가 맞습니까? (Y/N)")
                        if ans == "Y" or ans == "y":
                            vm.addMenu(item_name, item_price)
                            break
                        elif ans == "N" or ans == "n":
                            print("다시 입력 바랍니다.")
                            self.printAdminPage(vm)

            elif sel == 2:
                while True:
                    if len(vm.ItemNames) == 0:
                        print("더이상 삭제할 품목이 없습니다.\n")
                        break
                    vm.printAllMenu()
                    del_idx = int(input("삭제하고자하는 품목의 번호을 기입하시오 : "))
                    if del_idx <= 0 or del_idx > len(vm.ItemNames):
                        print("올바르지 못한 품목 번호입니다.\n다시 시도해주세요.")
                        continue
                    print("물품 이름 :", vm.ItemNames[del_idx-1])
                    ans = input("삭제하고자하는 정보가 맞습니까? (Y/N)\n종료를 원하시면 'q'를 입력해주세요.")
                    if ans == "Y" or ans == "y":
                        vm.deleteMenu(vm.ItemNames[del_idx-1])
                        break
                    elif ans == "N" or ans == "n":
                        print("다시 기입 바랍니다.")
                    elif ans == "q":
                        break
            elif sel == 3:
                if len(vm.ItemNames) == 0:
                    print("판매할 품목이 아예 없습니다!\n판매할 품목을 추가해주십시오.")
                    self.printAdminPage(vm)
                else:
                    break

class VendingMachine:
    def __init__(self):
        self.ItemNames = ["americano", "cafe-latte", "cafe-mocha", "caramel-macciato", "greenTea-latte"]
        self.ItemPrices = [2000, 3000, 3000, 3500, 3000]

    def printAllMenu(self):
        print("=" * 20)
        print("\t\tMenus\t\t")
        print("=" * 20)
        for i in range(len(self.ItemNames)):
            print("%d. %s : %d" %(i+1, self.ItemNames[i], self.ItemPrices[i]))
        print("=" * 20)

    def printAvailableMenu(self, money, order):
        print("=" * 40)
        print("\t\tAvailable Menus\t\t")
        print("=" * 40)
        check = []
        for i in range(len(self.ItemNames)):
            if self.ItemPrices[i] <= money:
                check.append(i)
                print("%d. %s : %d" % (i + 1, self.ItemNames[i], self.ItemPrices[i]))
        print("=" * 40)
        print("\n\n")

        self.selectItem(check, money, order)

    def buyMore(self, changes, order):
        if changes >= 1000:
            ans = input("더 구매하시겠습니까? (Y/N) : ")
            if ans == 'Y' or ans == 'y':
                self.printAvailableMenu(changes, order)
            elif ans == 'N' or ans == "n":
                print("주문하신 음료는 총 %d잔이며 " % len(order), end="")
                for item in order:
                    print("%s" % item, end=" ")
                print("입니다.")
                print("%d 만큼의 잔돈이 반환됩니다." % changes)
                exit(-1)
        elif changes >= 0:
            # print("구매가 완료되었습니다.")
            exit(-1)
            # self.getChanges(changes, order)
        else:
            print("잔액이 부족하여 구매가 불가합니다.")
            exit(-1)

    def getChanges (self, changes, order):
        global init_money
        if changes < 0:
            print("잔액이 부족하여 구매가 불가능 합니다.")
            print("%d원 만큼이 모자랍니다." % abs(changes))
            ans = input("금액을 더 투입하시겠습니까? (Y/N):")
            if ans == "Y" or ans == "y":
                money = int(input("금액을 입력하세요 : "))
                self.getChanges(changes+money, order)
            elif ans == "N" or ans =="n":
                print("잔액이 부족하여 투입하신 전액(%d원)을 반환합니다." %init_money)
                # self.buyMore(changes, order)
                exit(-1)
        else:
            print("주문하신 음료는 총 %d잔이며 " %len(order), end="")
            for item in order:
                print("%s" %item, end=" ")
            print("입니다.")
            print("%d원 만큼의 잔돈이 반환됩니다." %changes)
            self.buyMore(changes, order)
            # exit(-1)

    def selectItem(self, check, money, order):
        global init_money
        if len(check) <= 0:
            print("구매하실 수 있는 품목이 없습니다.")
            print("현재 투입하신 총 금액은 %d원 입니다." % money)
            more_money = int(input("금액을 더 투입해주십시오 : "))
            init_money += more_money
            self.printAvailableMenu(money+more_money, order)
        item_num = int(input("구매하고자 하는 물품의 번호를 입력해주세요 : "))
        if item_num - 1 not in check:
            print("잘못된 입력 값입니다.\n다시 시도해주세요.")
            self.printAvailableMenu(money, order)

        print("선택하신 물품이 %s가 맞습니까?" %self.ItemNames[item_num-1])
        ans = input("Y/N ? : ")
        if ans == "Y" or ans == "y":
            price = self.ItemPrices[item_num-1]
            print("1. 아이스 음료(500원 추가)\n2. 뜨거운 음료")
            ans = int(input("원하는 종류의 번호를 선택하여 주십시오."))
            if ans == 1:
                price += 500
                order.append("ice_"+self.ItemNames[item_num - 1])
                self.getChanges(money-price,order)
            elif ans == 2:
                order.append("hot_"+self.ItemNames[item_num - 1])
                self.getChanges(money-price,order)
            else:
                print("입력이 옳바르지 않습니다.\n다시 시도해주십시오.")
                self.selectItem(check, money, order)
        else:
            self.printAvailableMenu(money, order)

    def checkMenu(self,item_name):
        for i in range(len(self.ItemNames)):
            if self.ItemNames[i] == item_name:
                return True
        return False

    def addMenu(self, item_name, item_price):
        self.ItemNames.append(item_name)
        self.ItemPrices.append(item_price)

    def deleteMenu(self,item_name):
        item_idx = self.ItemNames.index(item_name)
        if item_name in vm.ItemNames:
            del self.ItemNames[item_idx]
            del self.ItemPrices[item_idx]
            print("%s이 삭제되었습니다."%item_name)
        else:
            print("존재하지 않는 품목입니다!.")

# starting point
sel = 0
order = []
vm = VendingMachine()
init_money = 0
while sel != 3:
    print("=" * 20)
    print("1. Customer")
    print("2. Admin")
    print("3. 종료")
    print("=" * 20)
    sel = int(input("이용하고자 하는 번호를 입력해주세요 : "))

    if sel == 1:
        vm.printAllMenu()
        money = int(input("돈을 넣어주세요 :"))
        print("넣으신 돈의 액수는 %d원 입니다." % money)
        print("넣으신 돈으로 구매하실 수 있는 품목들입니다.")
        init_money += money
        vm.printAvailableMenu(money, order)
    elif sel == 2:
        while True:
            pwd = input("관리자 비밀번호를 입력하세요 (종료를 원하시면 'q'를 입력해주세요): ")
            admin = Admin()
            if pwd == "q":
                break
            elif admin.pwdComfirm(pwd):
                admin.printAdminPage(vm)
                break
            else:
                print("옳바르지 않은 비밀번호입니다.\n다시 입력해주세요.")