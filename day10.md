### day10

#### 今日内容

- 参数
- 作用域
- 函数嵌套



#### 面试相关：

1.py2与py3区别

2.3 or 8 and 8

3.字符串反转使用切片实现[::-1]

4.is 和==区别

5.

```
v1=1
v2=(1)
v3=(1,)
print(type(v1),type(v2),type(v3),)
```

6.每种数据类型列举方法

```
str 1.startswith/endswith 2.upper/lower 3.isdigit/isdecimal 4.format 5.strip 6.spilt 7.jion 8.encode
list 1.append 2.insert 3.pop/remoce/clear 4.extend 5.reverse 6.sort（）
tuple（无）
dict 1.keys 2.values 3.items 4.pop 5.get 6.update 
set（） 1.add 2.update 3.discard/pop/remove/clear 4.intersection 5.union 6.difference

```

7.深浅copy

#### 笔试题：

1.文件操作，如何读取大文件的内容

```
with open(...) as file_object:
for line in file_object:
	print(line)

file_object=open('text.txt',mode='r',encoding='utf-8')
#读取所有的内容到内存
# data=file_object.read(2)

#从当前光标所在位置向后读取2个字符。
#file_object.seek(3)
#data=file_object.read(2)

#读取所有的内容到内存，并按照每一行进行分割到列表中
data_list=file_object.readlines()
print(data_list)
```



#### 2.知识点回顾

##### 2.1参数

```
def func(n1,n2)
	print(n1,n2)
func(1,2)
func(1.[11,22,33])
func({'k1':'k'},[11,22,33])
#严格按照顺序传参数，位置方式传参--->位置参数
#实际参数可以是任意类型
```



#### 3.返回值

- 函数没有返回值，默认返回：None

- 函数内部执行过程遇到return，就终止

- return可以返回任意类型

  ```
  特殊情况返回元组：
  def func():
       return 1,2,3
  print(type(func()))
  ---> <class 'tuple'>
  ```





### 今日详细内容

#### 1.参数

1.基本参数知识

- 任意个数

- 任意类型

  ```
  def  func(a1,a2,a3)
  	print(a1,a2,a3)
  func(1,'aaa',True)
  ```

#### 2.位置参数（调用函数并传入参数）

实参与形参位置一一对应，数量一一对应。

```
def func(a1,a2):
	print(a1,a2)
func(1,2)
```

#### 3.关键字参数（按照关键字进行传参）

```
def func(a1,a2):
	print(a1,a2)
func(a2=2,a1=99)

#关键字传参和位置传参可以混合使用
#注意保证一点关键字参数必须在位置参数后面，总和等于形参个数。
def func(a1,a2,a3):
	print(a1,a2,a3)
#func(1,2,a3=9)
#func(1,a2=2,a3=9)
#func(a1=1,a2=2,a3=9)
#func(a3=9,1,2)#错误，关键字参数必须在位置参数后面
#func(a1=1,2,a3=9)#错误，关键字参数必须在位置参数后面
```

#### 4.默认参数（定义）

```
def func(a1,a2=123):
	pass
'''
func函数接受两个参数，调用函数进行传值时。
	func（1，2）
	func(1,a2=1)
	func(a1=123,a2=99)
	func(222)#a1=222,a2等于123
'''

```

#### 5.万能参数（打撒）

##### 	*args  

- ​			可以接收任意位置参数，并将参数转换成  元组。
- ​			只能用位置参数进行传参
- 调用函数无*

```
def func(*rgs):
	print(args)
func(1，'asd ')#args=(1,'asd')
```



- 调用函数有*

```
def func(*rgs):
	print(args)
func(*(1，'asd') )#args=(1,'asd')
```

 

```
def func(*args):
	print(args)
func(1,2,[11,22],12,'tasd','alex')#以元组的方式传入
func(1,2)#args=(1,2)
func((11,22,33,44))#args=((11,22,33,44),)
func(*(11,22,33,44))#args=(11,22,33,44)

------------

def func(a1,*args):
	pass
func(1,2,3,4,5)#a1=1,*args=2,3,4,5

------------

def func(a1,*args,a2):
	pass
func(1,2,3,4,5,a2=12)#a1=1,*args=2,3,4,5,a2=12

------------

def func(a1=10,*args,a2=123):
	pass
func(1,2,3,4,5)#a1=1,*args=2,3,4,5,a2=123
```



##### **kwargs

- 可以接收任意关键字参数值，并将传入的参数转换为  字典。
- 只能传关键字传输
- 调用函数无**

```
def func(**kwargs):
	print(kwargs)
func(k1=1，K2='asd')#kwargs={'k1':1,'k2':'asd'}
```

- 调用函数有**

```
def func(**kwargs):
	print(kwargs)
func(**{'k1':1,'k2':'asd'})#kwargs={'k1':1,'k2':'asd'}
```



#### 综合使用

```
def func(*args，**kwargs)
	print(args,kwargs)
func(*[1,2,3],k1=2,k5=9 )
func(*[1,2,3],**{"k1"=1,'K2'=2})
```



### 重点还是 位置参数 要在 关键字参数 前面



### 作用域

python中

- py文件：全局作用域

- 函数：局部作用域

  

  

### 总结：

一个函数就是一个作用域

作用域中查找函数规则：优先在自己作用域找数据，自己没有就去父级域找，最终到全局作用域找。注意理清楚父级作用域中值到底是多少？

```
x=10
def func()
	x=9
	print(x)
func()
---9
```

练习：

```
x=10
def func()：
	x=9
	print（x）
	def x1():#没执行
		x=999
		print(x)
func()
---9


x=10
def func()：
	x=9
	print（x）
	def x1():
		x=999
		print(x)
	x1()
func()
-----9----999


x=10
def func()：
	x=9
	print（x）
	def x1():
		x=999
		print(x)
	print(x)
	x1()
func()
----9---9---999

x=10
def func()：
	x=9
	print（x）
	def x1():
		x=999
		print(x)
	x1()
	print(x)
func()

----9--999-9


x = 10
def func():
    x = 8
    print(x)
    def x1():
        print(x)
    x1()
    print(x)

func()
----8-8-8


x = 10
def func():
    x = 8
    print(x)
    def x1():
        print(x)
    x = 9
    x1()
    x = 10
    print(x)

func()
----8-9-10---


x = 10
def func():
    x = 8
    print(x)
    def x1():
        print(x)

    x1()
    x = 9
    x1()
    x = 10
    print(x)

func()

---8-8--9-10
```



- 子作用域中只能找到父级中的值，默认无法为父级值重新赋值（int str 元组），但是可以进行修改父级值（list，dict，set（）。如果想赋值可以通过global/nonlocal强制赋值任何类型值。

  -  global---赋值全局参数
  - nonlocal----赋值父级参数

  ```
  # #####################
  name = 'oldboy'
  def func():
      name = 'alex' # 在自己作用域再创建一个这样的值。
      print(name)
  func()
  print(name)
  ----alex---oldboy
  
  
  # #####################
  name = [1,2,43]
  def func():
      name.append(999)
      print(name)
  func()
  print(name)
  
  ----[1,2,43,999]---[1,2,43,999]
  
  # ###################### 如果非要对全局的变量进行赋值
  # 示例一
  name = ["老男孩",'alex']
  def func():
      global name
      name = '我'
  func()
  print(name)
  ----我---
  
  # 示例一
  name = "老男孩"#999
  def func():
      name = 'alex'
      def inner():
          global name
          name = 999
      inner()
      print(name)
  func()
  print(name)
  
  -----alex---999
  
  
  
  # ############################## nonlocal
  name = "老男孩"
  def func():
      name = 'alex'
      def inner():
          nonlocal name # 找到上一级的name
          name = 999
      inner()
      print(name)
  func()
  print(name)
  
  -----999---老男孩
  
  ```

  























