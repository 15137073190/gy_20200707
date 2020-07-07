from dy02 import module_1
from dy02.module_1 import as module_1_a,name as module_1_name,Test



a = "我是模块2中的a变量"

def name():
    print("我是模块2中的a方法")

class Test():
    name = "我是模块2中的Test类"


print(module_1_a)
#print(module_1.a)
print(name())
print(Test.name)



