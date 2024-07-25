import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().name, 'start')
        print('run')
        print(current_thread().name, 'stop')


t1 = MyThread()
# Thread-1 start
# run
# Thread-1 stop
# MainThread main thread end
t1.start()
t1.join()
print(current_thread().name, 'main thread end')
