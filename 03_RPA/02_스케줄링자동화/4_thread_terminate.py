from time import sleep
from threading import Thread


def infinite_loop():
    while True:
        sleep(1)
        print('Infinite Loop Thread!')


if __name__ == '__main__':
    # 스레드 생성 후 데몬 스레드 설정하기
    t = Thread(target=infinite_loop)
    t.daemon = True
    # 스레드 생성 시 데몬 스레드 설정하기
    t = Thread(target=infinite_loop, daemon=True)
    t.start()

    print('Script Start!')
    sleep(5)
    print('sleep 5sec')
    print('Script End!')