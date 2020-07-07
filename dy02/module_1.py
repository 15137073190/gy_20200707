# a = "我是模块1中的a变量"
#
# def name():
#     print("我是模块1中的name方法")
#
# class Test():
#     name = "我是模块1中的Test类"
#
#
# if __name__ == '__main__':
#      #print(module_1.a)
#     name()
#     print(Test.name)
#
#
#
# #类型转换
# l = [1,2,3,4,6,9,7,8,62,36]
# s = {1,3,4,9,7,62,36,5,6,7,9,15,41,2,5,42}
# #字符串转列表
# print(list(s))
# #元组转列表
# print(list(s))






#打开模式:r 读取 w 清空写入   b 二进制模式
# f = open("aaa.txt",'w')  #open 打开文件
# f.write("hello Kitty , how are you , good good study \nday day up")  #write写入内容至打开文件
# f.close() #关闭文件
#
# f = open("aaa.txt",'r')
# #print(f.read()) #默认读取全部数据
# #print(f.read(10)) #读取指定大小数据
# #print(f.readline()) #按行读取，读取一行
# #print(f.readlines()) 按行读取，读取所有行
# #f.close()
#
#
# s = "13579246810abcdefjhijklmnopqrstuvwsyz"
# print(s[0])
# print(s[-1])
# print(s[1:-2])
# print(s[1:-2:2])
# print(s[-1:0:-1])
# print(s[::-1])
# print(s[2:])
# print(s[:-2])

#
# l = "sfsyrdhdf,jeoitjsk,gjwojf,ssfsfsfs"
# print(l.split(","))
# with open("aaa.txt",'r') as f: #with 使用一个上下文管理器
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n","") , end="") #print 默认带一个换行
#九九乘法表
#通过占位符格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d X %d = %d"%(j,i,i*j),end="\t")
#     print()
# # .format
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} X {} = {}".format(j,i,i*j),end="\t")
#     print()

#
# l = [1,3,3,64,64,6,97,64,34,6,5,7,64]
#
# l[0] = 20
# print(l)
# l[1:5] = 147,258,369,123
# print(l)


# l = []
# l.append("王大锤")
# l.append("王二锤")
# l.append("王小锤")
# l.extend({'12,23,34,56,',123456,45674})
# print(l)

# l = [1,3,3,64,64,6,97,64,34,6,5,7,64]
# print(l.pop())
# print(l)
#
# print(l.pop(1))
# print(l)
#
#
# l = [1,3,3,64,64,6,97,64,34,6,5,7,64]
# l.remove(1)
# print(l)
#
# l = [True,1,3,3,64,64,6,97,64,34,6,5,7,64]
# l.remove(1)
# print(l)
# l.clear()
# print(l)
#
# # 字典的操作
# d = {"name":"小明","age":18,"sex":"男"}
#
# for key in d:      #只能遍历key值
#     print(d[key])
#
# d.items()          #对字典全部遍历，先转成items，再用for循环
# print(d.items())
#
# for k,v in d.items():
#     print(k,v)
#
# d["addr"] = "上海闵行"
# print(d)
# d["addr"] = "上海浦东"
# print(d)
#
# d = {"name":"小明"，"age":18,"sex":"男"}
#
# d.update({"addr":"上海闵行","学历":"本科"})
# print(d)



# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
# print("操作完文件")
#
#
# def div(a,b):
#     try:
#         return a/b
#     except:
#         return
#
# print(div(10,2))

class CustomException(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value
    def __str__(self):
        return self,value

a = 1
try:
    if a == 1 :
        print("a = {} 触发异常".format(a))
except CustomException as e :
    print(e)













