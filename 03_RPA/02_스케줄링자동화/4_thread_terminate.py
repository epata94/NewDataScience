from time import sleep
from threading import Thread


def infinite_loop():
    while True:
        sleep(1)
        print('\t\t\t\t\t\t\t\t무한루프 실행 중..')


# 스레드 생성 시 데몬 스레드 설정하기
# t = Thread(target=infinite_loop)
# 쓰레드의 deamon 속성 값이 True 라면 부모 프로그램이 종료될 경우
# 같이 종료된다.
t = Thread(target=infinite_loop, daemon=True)
t.start()

print('Main Program Start!')
sleep(5)
print('Main Progrom sleeps 5 sec')
print('Main Program End!')