import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("메인 프로그램 Start")

threads = []
for i in range(5):
    # target인자에 쓰레드로 동작할 함수 이름을 지정한다.
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start()  # 스레드를 실행한다.

print("메인 프로그램 End")