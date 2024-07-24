class User():  # 定义一个类
    def __init__(self, name, age, occupation):
        self.__name = name  # 属性
        self.age = age
        self.occupation = occupation

    def print_role(self):  # 定义一个方法
        print('%s : %s %s' % (self.__name, self.age, self.occupation))

    def update_name(self, new_name):
        self.name = new_name


class Monster():
    '定义怪物'

    def __init__(self, age=100):
        self.age = age

    def run(self):
        print('移动一个位置')

    def who_ami(self):
        print('I am Monster')


class Animals(Monster):
    '定义一个普通怪物'

    def __init__(self, age=10):
        super().__init__(age)


class Boss(Monster):
    '定义一个超级怪物'

    def __init__(self, age=20):
        super().__init__(age)

    def who_ami(self):
        print('I am Boss')


user1 = User('Tom', 18, 'teacher')
user2 = User('Mike', 20, 'player')
user1.print_role()  # Tom : 18 teacher
user2.print_role()  # Mike : 20 player

user1.update_name('Peter')
user1.print_role()  # Peter : 18 teacher
user1.name = 'Jack'
user1.print_role()  # __name 私有 只能通过方法修改，不可以直接改变属性值 Tom : 18 teacher

a0 = Monster(30)
print(a0.age)  # 30
a0.run()  # 移动一个位置

animals1 = Animals(20)
animals1.run()  # 移动一个位置
print(animals1.age)  # 20

a3 = Boss()
a3.who_ami()  # I am Boss

print('a1的类型是 %s' % type(animals1))  # a1的类型是 <class '__main__.Animals'>
print('a0的类型是 %s' % type(a0))  # a0的类型是 <class '__main__.Monster'>
print('a3的类型是 %s' % type(a3))  # a3的类型是 <class '__main__.Boss'>

print('a3是否为Boss的子类: %s' % isinstance(a3, Boss))  # a3是否为Boss的子类: True
