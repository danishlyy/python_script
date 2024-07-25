import threading
import time
from threading import current_thread


def my_thread(arg1, arg2):
    print(current_thread().name, 'start')
    print('%s %s' % (arg1, arg2))
    time.sleep(1)
    print(current_thread().name, 'end')


for i in range(1, 6, 1):
    # t1 = my_thread(i, i + 1)#顺序执行
    t1 = threading.Thread(target=my_thread, args=(i, i + 1))  # 多线程执行
    t1.start()

print(current_thread().name, 'stop')
