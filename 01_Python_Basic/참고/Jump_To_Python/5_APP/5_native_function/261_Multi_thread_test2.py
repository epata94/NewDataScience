import time
import threading
from datetime import datetime

s_dt = datetime.now()
print(s_dt) # 타임스템프 (로그 작성 또는 프로그램 성능 측정시 사용)


def long_task(thread_number):
    for i in range(5):
        time.sleep(1)
        print(f"#{thread_number}thread Working: {i+1}\n")

print("Start!")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task,args=(i+1,))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print("End")

e_dt = datetime.now()
print(e_dt)
print(e_dt-s_dt)

