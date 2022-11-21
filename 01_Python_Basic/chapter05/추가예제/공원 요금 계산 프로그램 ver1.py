age=int(input('나이를 입력 하여 주세요 : '))
price=0
if ((age>=0) and (age<4)) or age>=66:
    print('요금은 무료 입니다')
    quit()
elif (age>=4) and (age<14):
    price=2000
elif (age>=14) and (age<19):
    price=3000
elif (age>=19) and (age<66):
    price=5000
else:
    print("다시 입력 하세요")
    quit()
print(f'요금은 {price} 입니다.')
