from threading import Thread, current_thread
import time
import random
from queue import Queue

queue = Queue(5)


class Producer(Thread):
    '生产者'

    def run(self):
        name = current_thread().name
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' % (name, t))


class Consumer(Thread):
    '消费者'

    def run(self):
        name = current_thread().name
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消费了数据 %s ' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


p1 = Producer(name='p1')
p1.start()

c1 = Consumer(name='c1')
c1.start()
c2 = Consumer(name='c2')
c2.start()