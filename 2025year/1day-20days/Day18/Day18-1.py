# 定义类
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在玩游戏.')

stu1 = Student('黄成勇', 22)
stu2 = Student('李咏洋', 21)
print(stu1)
print(stu2)

# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象
# 只需要传入第二个参数课程名称
stu1.study('Python程序设计')

Student.play(stu2)
stu2.play()







