#-*-coding:utf-8-*-
# Author:Lu Wei

#1.写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
# def func(*arg):
#     sum=0
#     for i in arg:
#         sum+=i
#     return sum
# print(func(1,2,3,4,5,1))

#2.看代码写结果
# def func():
#     return 1,2,3
#
# val = func()
# print( type(val) == tuple )
# print( type(val) == list )

#3.看代码写结果
# def func(*args,**kwargs):
#     pass

# a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# def func(*args,**kwargs):
#     print(args)
# func(1,2,3,4)

# b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# def func(*args,**kwargs):
#     print(args)
# func([1,2,3,4],[11,22,33])

# c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# def func(*args,**kwargs):
#     print(args,kwargs)
# func([11,22],33,k1='v1',k2='v2')

# d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args, kwargs)
# func(*{'武沛齐','金鑫','女神'})#args=('武沛齐','金鑫','女神')

# e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args, kwargs)
# func({'武沛齐','金鑫','女神'},[11,22,33])#args=({'武沛齐','金鑫','女神'},[11,22,33])

# f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
# def func(*args,**kwargs):
#     print(args, kwargs)
# func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})#args=('武沛齐','金鑫','女神',[11,22,33]) kwargs=('k1'='栈')




# def func(name,age=19,email='123@qq.com'):
#     pass

# a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func('alex')#name=alex,age=19,email='123@qq.com'
# b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func('alex',20)#name=alex,age=20,email='123@qq.com'

# c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func('alex',20,30) #name=alex,age=20,email=30

# # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func('alex',email='x@qq.com')#name=alex,age=19,email='x@qq.com'


# # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func('alex',email='x@qq.com',age=99)#name=alex,age=99,email=x@qq.com

# # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func(name='alex',99)#不可以执行

# # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# def func(name,age=19,email='123@qq.com'):
#     print(name,age,email)
# func(name='alex',99,'111@qq.com')#不可以执行

#5.
# def func(users,name):
#     users.append(name)
#     return users
#
# result = func(['武沛齐','李杰'],'alex')
# print(result)#result=(['武沛齐','李杰','alex'])

#6.
# def func(v1):
#     return v1* 2
#
# def bar(arg):
#     return "%s 是什么玩意？" %(arg,)
#
# val = func('你')
# data = bar(val)
# print(data)#你你 是什么玩意？

#7.
# def func(v1):
#     return v1* 2
#
# def bar(arg):
#     msg = "%s 是什么玩意？" %(arg,)
#     print(msg)#你你 是什么玩意？
#
# val = func('你')
# data = bar(val)
# print(data)#None


#8.
# v1 = '武沛齐'
# def func():
#     print(v1)
# func()#'武沛齐'
# v1 = '老男人'
# func()#'老男人'

#9.
# v1 = '武沛齐'
#
# def func():
#     v1 = '景女神'
#     def inner():
#         print(v1)#'肖大侠''肖大侠'
#     v1 = '肖大侠'
#     inner()
# func()
# v1 = '老男人'
# func()


#10.
# def func():
#     data = 2*2
#     return data
#
# new_name = func
# val = new_name()
# print(val)#4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。

# #11.
# def func():
#     data = 2*2
#     return data
#
# data_list = [func,func,func]
# for item in data_list:
#     v = item()
#     print(v)#4,4,4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。

#12.
# def func(arg):
#     arg()
#
# def show():
#     print('show函数')
#
# func(show)#show函数
