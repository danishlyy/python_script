import time


def i_can_sleep():
    time.sleep(3)


start_time = time.time()
i_can_sleep()
end_time = time.time()
# function has run 3.004099130630493
print('function has run %s' % (end_time - start_time))

print(time.time())  # 1721981114.538421 Return the current time in seconds since the Epoch
print(
    time.localtime())  # time.struct_time(tm_year=2024, tm_mon=7, tm_mday=26, tm_hour=16, tm_min=5, tm_sec=14, tm_wday=4, tm_yday=208, tm_isdst=0)
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 2024-07-26 16:05:14

print(time.strftime('%Y%m%d'))  # 20240726

import datetime

print(datetime.datetime.now())  # 2024-07-26 16:19:12.606069
new_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + new_time)  # 2024-07-26 16:29:12.606135

one_day = datetime.datetime(2024, 8, 12)
new_day = datetime.timedelta(days=10)
print(one_day + new_day)  # 2024-08-22 00:00:00
