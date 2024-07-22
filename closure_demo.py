# 闭包：内部函数引用外部函数变量的函数
# 闭包 vs 函数： 闭包传递的参数相对函数少、且可以传递函数
def sum_closure(a):
    def add(b):
        return a + b

    return add


def summary():
    num1 = 1
    num2 = 2
    return num1 + num2


a = summary()
print(type(a))  # <class 'int'>
b = sum_closure(1)
print(type(b))  # <class 'function'>


# a * x + b = y
def a_line(a, b):
    def arg_y(x):
        return a * x + b

    return arg_y


line1 = a_line(3, 5)
print(line1(10))  # 35

