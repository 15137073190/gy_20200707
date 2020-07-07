# a = 20
# b = 30
# print(a + b)
#
# x,y,*z = (1, 2, 3, 4)
#
# print(x)
# print(y)
# print(z)
#
#
# a =1,2,3,4,5
# print(a)
#
# a,b,c = [1,2,3] #解包赋值
# print(a)
# print(b)
# print(c)
#
# a = 20
# b = 30
# print(a + b)
# print(a - b)
# print(a * b)
#
# x=9
# y=2
# print(x / y)
# print(y % x)
# print(x**2)
# print(x // y)
#
# a = 50
# b = 30
# print(a and b)
#
#
# z= 12331
# #取个位数
# print(z % 10)
# #取十位数
# #z = z // 10
# z //= 10
# print(z)
# print(z % 10)
#
#
#
# z = 132546
# print(z % 100)
#
# l = ["果芽","360","老干妈","腾讯","阿里"]
# if("知乎" in l):
#     print("合作方")
# else:
#     print("非合作方")
# ...
# score_1 = [40,65,45,78,98,62,23,48,88,72]
#  for score in score_1:
#         if  (score > 0 and score <= 59):
#          print("不及格")
#         elif (score >= 60 and score <= 70):
#          print("及格")
#         elif (score >= 71 and score <= 80):
#          print("良好")
#         elif (score >= 81 and score <= 100):
#          print("优秀")
#         else:
#          print("请输入正确的成绩")
#
# ...
#
#
#
#
# a = 1
# for i in range(10,0,-1):
#     a*=i
# print(a)

#
# flag = True
# a = 31
# while flag:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大")
#     elif (b < a):
#         print("小")
# #     else:
# #         print("对")
# #         flag = False
# #       break  终止循环
# #       continue  跳过本次循环
#
# #100以内可以被3整除的数字
# # for i in range(1,100):
# #     if (i % 3 != 0):
# #         continue
# #     print(i)
# #
# # for i in range(1,100):
# #     if (i % 3 != 0):
# #        print(i)
# #     break
#
# # 定义一个求两个数的商和余数的方法
# # def shang_yu(a , b):
# #     print("商:" a // b , "余数:" a % b)
# # level(16 , 5)
# # level(16 , 4)
#
# def shang_yu(a, b):
#     if (b == 0):
#         return None
#     else:
#         return (a // b , a % b)
# res = shang_yu(20,3) #按位置传参
# if res is None:
#     print("参数错误")
# else:
#     print("商为:",res[0],"余数为:",res[1])
#
# res = shang_yu(b=3,a=20) #按关键字传参
# if res is None:
#     print("参数错误")
# else:
#     print("商为:",res[0],"余数为:",res[1])
#
# #定义关键字形参，给参数b设置默认值
#
# c = 1,2,3,5,6
# a,*b = (1,2,3,4,5,6)
#
# print(b)



# def sm(a,b=5):
#     return a+b
# print(sm(5))
#
# def sum1 (*args):
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(sum1(1,3,45,454,6,5,7,654,3,23))
#
# def sum1 (name,*args,**kwargs):
#     #  *args 接受动态位置参数 （注：设置默认值name在 *args 后面，不设置默认值name在 *args 前面）
#     # **kwargs 接受动态关键字参数
#     print(**kwargs)
#     print(name)
#     s=0
#     for i in args:
#         s+=i
#     return s
# print(sum1(1,3,45,454,6,5,7,654,3,23))
# print(sum1(name="王大锤"))


# #面向对象
# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a +self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
#
# c = calc()     #类的实例化  c对象
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result() #要展示的结果

# class calc():
#     res=None
#
#     def __init__(self,a,b):   #魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a +self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
#
# c = calc(29,39)
# c.sum()
# c.get_result()

#九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
         print(j,"X",i,"=",i*j,end="\t")
    print()

#冒泡排序

# l = [23,21,2,13,64,45,12,11,10,9,5,78,98,72,65,35,16,100,1]
# length = len(l)
# # print(length)
# for i in range(length-1,0,-1):  #外层循环确定排好序的数据下标
#     for j in range(i):   #遍历未排好序的列表
#         if(l[j]>l[j+1]): #判断相邻两个数据，前边的如果大于后面的，则两个数据互换位置
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)





#
# #继承
# class Parent():
#     money = 10000000000000
#     house = 100000
#     __yi_wu = "裤子"
#     def shou_yi(self):
#         print("点石成金")
#
# class Child(Parent):
#     ai_hao = "花钱"
#     pass
#
#
# c = Child()
# print(c.ai_hao)
# print(c.money)
# print(c.house)
#
# 封装
#
# class aaa():
# #变量
#
#     pub_res = "共有变量"
#     __pri_res = "私有变量1"
#     __pri_res = "私有变量2"
#
#
# #方法
#
#     def pub_function(self):
#         print("共有办法")
#     def pri_function(self):
#         print("私有办法1")
#     def pri_function(self):
#         print("私有办法2")
#
#
# print(aaa.pub_res)
# print(aaa.pri_res)
# #print(aaa.pri_res) 这个是封装，无法调用的变量
# print(aaa().pub_function())
# print(aaa().pri_function())





































