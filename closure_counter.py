def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num1 = counter()
print(num1)  # <function counter.<locals>.add_one at 0x10b719a80>

print(num1())  # 1
print(num1())  # 2
print(num1())  # 3

num2 = counter(5)
print(num2())  # 6
print(num2())  # 7

num3 = counter(10)
print(num3())  # 11
print(num3())  # 12
