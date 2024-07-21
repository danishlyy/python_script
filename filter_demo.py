a = (1, 3, 5, 7)
b = 4
filter_result = filter(lambda x: x < b, a)  # 取出 a 中小于4的元素
print(filter_result)  # <filter object at 0x1004395a0>
print(list(filter_result))  # 取出 a 中小于4的元素 [1, 3]b

b = 6
filter_result = filter(lambda x: x < b, a)  # 取出 a 中小于6的元素
print(filter_result)  # <filter object at 0x1004395a0>
print(list(filter_result))
print(len(list(filter_result)))  # 0
print(len(list(filter(lambda x: x < b, a))))  # 取出a中小于6的元素个数 3


