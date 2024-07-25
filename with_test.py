class TestWith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常输出')
        else:
            print('has error %s' % exc_tb)


# normal case
# run
# Test is running
# 正常输出

# failure case
# run
# Test is running
# has error <traceback object at 0x1004bf600>
with TestWith():
    print('Test is running')
    raise NameError('testNameError')
