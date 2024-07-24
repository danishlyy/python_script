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

    pass


class Animals(Monster):
    '定义一个普通怪物'

    def __init__(self, age=10):
        super().__init__(age)


class Boss(Monster):
    '定义一个超级怪物'
    pass


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
