#9_14骰子
#导入随机数类
from random import randint
#创建类
class Die():
#初始化
    def __init__(self,sides):
        self.sides=sides
    def roll_die(self):
        num = randint(1,self.sides)
        return num
#6面的骰子十次
print("\n6面的骰子十次")
#创建一个6面的骰子
t=Die(6)
for i in range(10):
    print(t.roll_die())
#10面的骰子十次
print("\n10面的骰子十次")
#创建一个10面的骰子
x=Die(10)
for i in range(10):
    print(x.roll_die())
#20面的骰子十次
print("\n20面的骰子十次")
#创建一个20面的骰子
z=Die(20)
for i in range(10):
    print(z.roll_die())