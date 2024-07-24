import time


def i_can_sleep():
    time.sleep(3)


start_time = time.time()
i_can_sleep()
end_time = time.time()
# function has run 3.004099130630493
print('function has run %s' % (end_time - start_time))
