# abc
#
# hello

print('abc', end='\n\n')
print('hello')


def func(a, b, c):
    print('a=%s' % a)
    print('b=%s' % b)
    print('c=%s' % c)


# a=1
# b=2
# c=3
func(1, 2, 3)
# a=3
# b=2
# c=4
func(a=3, c=4, b=2)


# 函数可变长参数，非必须参数前面加*
def howlong(first, *other):
    print(1 + len(other))


howlong(1, 2, 3)  # 3
howlong(1)  # 1

list1 = [1, 2, 3]
i = iter(list1)
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 3
# print(next(i)) #StopIteration

for i in range(10,20,2):
    # 10
    # 12
    # 14
    # 16
    # 18
    print(i)
