age=int(input('나이를 입력 하여 주세요 : '))
price=0
grade=""
if (age>=0) and (age<4):
    grade="유아"
    print(f'귀하는 {grade}등급이며 요금은 무료입니다.')
    quit()
elif (age>=4) and (age<14):
    price=2000
    grade="어린이"
elif (age>=14) and (age<19):
    price=3000
    grade="청소년"
elif (age>=19) and (age<66):
    price=5000
    grade="성인"
elif age>=66:
    grade="노인"
    print(f'귀하는 {grade}등급이며 요금은 무료입니다.')
    quit()
else:
    print("다시 입력 하세요")
    quit()
print(f' 귀하는 {grade}등급이며 요금은 {price}원 입니다.')
