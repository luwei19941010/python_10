#-*-coding:utf-8-*-
# Author:Lu Wei

'''
def func():
     return 1,2

print(type(func()))


def func(a1,a2,a3):
    print(a1,a2,a3)
#func(1,2,a3=9)
#func(1,a2=2,a3=9)
func(1,2,a3=9)

def fuc(*args):
    pass
fuc(10)
'''

#
# def func(**kwargs):
# 	print(kwargs)
# func(k1=1,K2='asd')#kwargs={'k1':1,'k2':'asd'}
#
# def func(**kwargs):
# 	print(kwargs)
# func(**{'k1':1,'k2':'asd'})#kwargs={'k1':1,'k2':'asd'}
#
# def func(*args):
# 	print(args)
# func(1,2,[11,22],12,'tasd','alex')#以元组的方式传入
# func(1,2)#args=(1,2)
# func({'k1':1,'k2':'asd'})#args=((11,22,33,44),)
#
# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#
# func()
#
# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#     x1()
#
# func()
#
#
# x = 10
# def func():
#     x = 9
#     print(x)
#     def x1():
#         x = 999
#         print(x)
#     print(x)
#     x1()
#
# func()
#
#
# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#     x1()
#     print(x)
#
# func()



# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#     x = 9
#     x1()
#     x = 10
#     print(x)
#
# func()


#
# x = 10
# def func():
#     x = 8
#     print(x)
#     def x1():
#         print(x)
#
#     x1()
#     x = 9
#     x1()
#     x = 10
#     print(x)
#
# func()


# #####################
# name = 'oldboy'
# def func():
#     name = 'alex' # 在自己作用域再创建一个这样的值。
#     print(name)
# func()
# print(name)



# # ###################### 如果非要对全局的变量进行赋值
# # 示例一
# name = ["老男孩",'alex']
# def func():
#     global name
#     name = '我'
# func()
# print(name)
# 示例一
# name = "老男孩"#999
# def func():
#     name = 'alex'
#     def inner():
#         global name
#         name = 999
#     inner()
#     print(name)
# func()
# print(name)



