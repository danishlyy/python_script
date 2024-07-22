def add(x, y):
    return x + y


result = add(1, 2)
print(result)  # 3

# 替换为 lambda
lambda x, y: x + y

# filter
a = [1, 2, 3, 4, 5, 6, 7]
a = list(filter(lambda x: x > 2, a))
print(a)  # [3, 4, 5, 6, 7]

# map
a = [1, 2, 3]
print(list(map(lambda x: x + 1, a)))  # [2, 3, 4]
b = [2, 3, 4]
print(list(map(lambda x, y: x + y, a, b)))  # [3, 5, 7]
  
