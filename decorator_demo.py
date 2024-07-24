import time


# 装饰器传入进来的是函数
# 闭包传入进来的是变量
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('function has run %s s' % (end_time - start_time))

    return wrapper


@timer
def i_can_sleep():
    time.sleep(3)


# 等价于 timer(i_can_sleep())
i_can_sleep()  # function has run 3.0043270587921143 s


def new_tips(argv):
    def tips(func):
        def inner(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('end')

        return inner

    return tips


@new_tips('add module')
def add(a, b):
    print(a + b);


# start add module add
# 9
# end
print(add(4, 5))


@new_tips('sub module')
def sub(a, b):
    print(a - b);


# start sub module sub
# 1
# end
print(sub(5, 4))
