class User():  # 定义一个类
    def __init__(self, name, age, occupation):
        self.name = name  # 属性
        self.age = age
        self.occupation = occupation

    def print_role(self):  # 定义一个方法
        print('%s : %s %s' % (self.name, self.age, self.occupation))

    def update_name(self,new_name):
        self.name = new_name



class Monster():
    '定义怪物'
    pass


user1 = User('Tom', 18, 'teacher')
user2 = User('Mike', 20, 'player')
user1.print_role()  # Tom : 18 teacher
user2.print_role()  # Mike : 20 player

user1.update_name('Peter')
user1.print_role() # Peter : 18 teacher
