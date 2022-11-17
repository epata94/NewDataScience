# 2.	사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
# - 단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고
#  새로 입력한 내용을 추가해야 한다.
# -	엔터가 들어올 때 까지 반복문으로 처리한다. (엔터는 ‘’로 판단가능)
#
# 화면출력] 저장할 내용을 입력하세요 (종료는 엔터):

while True:
    user_input=input("저장할 내용을 입력하세요 (종료는 엔터):")
    if user_input == '':
        print('입력을 종료합니다')
        break
    try:
        input_file=open('Test/test2.txt',mode='a')
        input_file.write(user_input+' ')
        input_file = open('Test/test2.txt')
        print(f'지금까지 입력된 내용은 다음과 같습니다: {input_file.read()}')
    except Exception as e:
        print(f"에러발생: {e}")
    finally:
        input_file.close()