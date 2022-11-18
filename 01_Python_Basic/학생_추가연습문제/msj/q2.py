try:
    file = open('//192.168.0.47/데이터분석_수업/문성준/메시지.txt', mode='w', encoding='utf-8')

    msg = input('메시지를 입력하세요 : ')

    for i in range(10) :

        file.write(f'{msg}{i+1}\n')

except Exception as e:

    print('예외 발생 : ', e)

finally:
    file.close()