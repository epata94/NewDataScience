import time
import threading
from datetime import datetime

s_dt = datetime.now()
print(s_dt) # 타임스템프 (로그 작성 또는 프로그램 성능 측정시 사용)

def long_task():
    print("쓰레드 구동!")
    while True:
        menu = int(input("작업 진행하시겠습니까? (0: 종료, 1: 구동) : "))
        if menu == 0:
            break
        else:
            for i in range(1,6):
                print(f"잡업{i} 완료")
                time.sleep(1)

print("Start")

# t = threading.Thread(target=long_task)
# Thread 생성자의 기본 daemon 옵션은 False이다.
# 부모 thread가 종료되어도 자식(Sub) thread는 종료되지 않는다.
# daemon=True로 하게되면 부모 Thread가 종료되면 모든 Sub Thread는 종료된다.
t = threading.Thread(target=long_task, daemon=True)
t.start()

print("End")

e_dt = datetime.now()
print(e_dt)
print(e_dt-s_dt)

