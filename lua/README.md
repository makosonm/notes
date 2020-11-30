# Lua 学习

## 1、Lua数据类型 

Lua中有8个基本类型分别为：nil、boolean、number、string、userdata、function、thread和table。


数据类型 | 描述
---|---
nil | 只有值为nil属于该类，表示一个无效值（判断中相当于false）
boolena | false / true
number | 双精度类型的实浮点数
string | 字符串由一对双引号或单引号来表示
function | 由C 或 Lua编写的函数
userdata | 表示任意存储在变量中的C数据结构
thread | 表示执行的独立线路，用于执行协同程序
table | Lua中的（table）其实是一个“关联数据”，数组的索引可以是数字或这是字符串。在Lua里，table的创建时通过“构造表达式”来完成，最简单的构造表达式实{}, 用来创建一个空表


## 2、Lua变量

- Lua 变量有三种类型：全局变量、局部变量、表中的域
- Lua 中的变量全是全局变量，那怕是语句块或是函数里，除非用 local 显式声明为局部变量
- 局部变量的作用域为从声明位置开始到所在语句块结束
- 变量的默认值均为 nil


## 3、Lua循环

- while
    - while conditions do .. end   
- for
    - for  do .. end   
- repeat...until
    - 限制性后判断，类似其他语言的 do .. while    
- 循环嵌套

## 4、流程控制

- if (布尔值表达式) then ... end
- if (布尔值表达式) then ... else ... end
- if 嵌套

## 5、Lua 函数

- Lua函数主要有两种用途
    - 完成指定的任务，这种情况下函数作为调动语句使用
    - 计算并返回值，这种情况下函数作为赋值语句的表达式使用

- 函数定义

```Lua
optional_function_scope function function_name( argument1, argument2, argument3..., argumentn)
    function_body
    return result_params_comma_separated
end
```
    
- 解析
    - optional_function_scope该参数是可选的制定函数是全局函数还是局部函数，未设置该参数默认为全局函数，如果你需要设置函数为局部函数需要使用关键字 local
    - function_name: 指定函数名称
    - argument1, argument2, argument3..., argumentn: 函数参数，多个参数以逗号隔开，函数也可以不带参数
    - function_body: 函数体，函数中需要执行的代码语句块
    - result_params_comma_separated: 函数返回值，Lua语言函数可以返回多个值，每个值以逗号隔开
    

- 可变参数，和C语言类似，在函数参数列表中使用三个 ... 便是函数有可变参数
    - 通常在遍历变长参数的时候只需要使用 {…}，然而变长参数可能会包含一些 nil，那么就可以用 select 函数来访问变长参数了：select('#', …) 或者 select(n, …)
    - select('#',...) 返回可变参数的长度
    - select(n, ...) 用于访问n到select('#', ...)的参数
    
```Lua
function add(...)
    local s = 0
    local arg={...}    --> arg 为一个表，局部变量
    for i, v in ipairs{...} do -- {..} 表示一个由所有变长参数构成的数组
        s = s + v
    end
    -- #arg 获取可变参数的个数
    -- select('#', ...) 和 #arg作用一样
    return s, s/#arg,s/select('#', ...) 
end

print(add(1,2,3,4,5,6,7,8,9)) --> 25 5.0 5.0
```
    
##  6、Lua运算符

下面用到的A设定为10， B设定为20

- 算数运算符
    
操作符 | 描述 | 实例
---|--- | ---
+  | 加法 | A + B = 30
-  | 减法 | A - B = -10
*  | 乘法 | A * B = 200
/  | 除法 | B / A = 2
%  | 取余 | B % A = 0
^  | 乘幂 | A^2 = 100
-  | 负号 | -A  = -10

- 关系运算符

操作符 | 描述 | 实例
---|--- | ---
==  | 等于 | (A == B) false
~=  | 不等 | (A ~= B) true
>  | 大于 | (A > B) false
<  | 小于 | (A < B) true
>=  | 大于等于 | (A >= B) false
<=  | 小于等于 | (A <= B) true


- 逻辑运算符

设定A的值为true, B的值为false

操作符 | 描述 | 实例
---|--- | ---
and  | 逻辑与,A为False返回A，否则返回B | (A and B) false
or  | 逻辑或 | (A or B) true
not  | 逻辑非 | not (A and B) true

- 其他运算符

操作符 | 描述 | 实例
---|--- | ---
...  | 连接两个字符串 | a...b
#  | 医院运算符，返回字符串或表的长度 | #'Hello' 返回5


## 7、Lua字符串

三种表示方法: 单引号、双引号及 [[字符串内容]]之间的一串字符

常用字符串操作

- .. 链接两个字符串
- string.upper(argument)
- string.lower(argument)
- string.reverse(argument) 字符串反转
- string.len(arg) 
- string.gsub(mainString, findString, replaceString, num)
    - 字符串中查找替换，num忽略替换全部
    - string.gsub('aaaa', 'a', 'z', 3) -- zzza  3
    - string.gsub('aaaa', 'a', 'z') -- zzzz 4
- string.find(str, substr, [inti, [end]])
    - 在一个指定的目标字符串中搜索指定的内容（第三个参数为索引），返回其具体的位置，不存在返回nil
    - string.find('Hello Lua user', 'Lua', 1) -- 7 9
    > s = "Deadline is 30/05/1999, firm"
    > date = "%d%d/%d%d/%d%d%d%d" -- 匹配模式
    > print(string.sub(s, string.find(s, date)))    --> 30/05/1999
- string.format(...) 返回一个类似printf的格式化字符串
- string.char(arg) 及 string.byte(arg[,int])
    - char 将整型数字转成字符并连接， byte 转换字符为整数值(可以指定某个字符，默认第一个字符)
    - string.char(97,98,99,100) -- abcd
    - string.byte("ABCD",4) -- 68
    - string.byte("ABCD") -- 65
- string.rep(string, n)  把字符串重复几次
    - string.rep('abcd', 2) -- abcdabcd
- string.gmatch(str, pattern) 
    - 反回一个迭代器函数，每一次调用这个函数，返回一个在字符串 str 找到的下一个符合 pattern 描述的子串。如果参数 pattern 描述的字符串没有找到，迭代函数返回nil
    > for word in string.gmatch("Hello Lua user", "%a+") do print(word) end
    > Hello
    > Lua
    > user
- string.match(str, pattern, init)
    - 只查找源字符串str中的第一个配对，参数init可选，指定搜索过程的起点，默认为1
    - 成功匹配函数返回匹配表达式中的所有获取结果
    - 没有设置捕获标记，则返回整个配对字符串
    - 没有成功匹配是返回nil
    > string.match("I have 2 questions for you.", "%d+ %a+") -- 2 questions
    > string.format("%d, %q", string.match("I have 2 questions for you.", "(%d+) (%a+)")) -- 2, "questions"

## 8、数组

Lua 数组的索引键值可以使用整数表示，数组的大小不是固定的

> 类似于Python的List, PHP中的索引数组

- 一维数组

```Lua
array = {'Lua', 'Tutorial'}
for i, v in ipairs(array) do
    print(i, v)
end
-- 1 Lua
-- 2 Tutorial
```

- 多维数组

```Lua
array = {}
for i = 1, 3 do
    array[i] = {}
    for j = 1, 3 do
        array[i][j] = i * j
    end
end

-- 访问数组
for i = 1, 3 do
    for j = 1, 3 do
        print(array[i][j])
    end
end
```

## 9、table

- table 是 Lua 的一种数据结构用来帮助我们创建不同的数据类型，如：数组、字典等
- Lua table 使用关联型数组，你可以用任意类型的值来作数组的索引，但这个值不能是 nil

- table的结构

```Lua
mytable = {} -- 初始化表
mytable[1] = 'Lua' -- 指定值
mytable = nil --> 移除引用 lua垃圾回收会释放内存
```

- table.concat(table[,sep[,start[,end]]])

```Lua
fruits = {"banana","orange","apple"}
-- 返回 table 连接后的字符串
print("连接后的字符串 ",table.concat(fruits))

-- 指定连接字符
print("连接后的字符串 ",table.concat(fruits,", "))

-- 指定索引来连接 table
print("连接后的字符串 ",table.concat(fruits,", ", 2,3))

[[
连接后的字符串     bananaorangeapple
连接后的字符串     banana, orange, apple
连接后的字符串     orange, apple
]]
```

- table.insert(table, [pos,]value)
- table.remove(table[,pos])

```Lua
fruits = {"banana","orange","apple"}
-- 在末尾插入
table.insert(fruits,"mango")
print("索引为 4 的元素为 ",fruits[4])

-- 在索引为 2 的键处插入
table.insert(fruits,2,"grapes")
print("索引为 2 的元素为 ",fruits[2])

print("最后一个元素为 ",fruits[5])
table.remove(fruits)
print("移除后最后一个元素为 ",fruits[5])
```
- table.maxn(table) -- 在Lua5.2之后该方法不存在
- table.sort(table[,comp])


## 10、模块与包

模块类似于一个封装库，从 Lua 5.1 开始，Lua 加入了标准的模块管理机制，可以把一些公用的代码放在一个文件里，以 API 接口的形式在其他地方调用，有利于代码的重用和降低代码耦合度。

Lua 的模块是由变量、函数等已知元素组成的 table，因此创建一个模块很简单，就是创建一个 table，然后把需要导出的常量、函数放入其中，最后返回这个 table 就行

以下为创建自定义模块 module.lua，文件代码格式如下

```
-- 文件名为 module.lua
-- 定义一个名为 module 的模块
module = {}
 
-- 定义一个常量
module.constant = "这是一个常量"
 
-- 定义一个函数
function module.func1()
    io.write("这是一个公有函数！\n")
end
 
local function func2()
    print("这是一个私有函数！")
end
 
function module.func3()
    func2()
end
 
return module

-- 使用 test_module.lua
local m = require("module")
print(m.constant)
print(m.func3())

-- 第二种引入方式
require("module")
print(module.constant)

```

- Lua提供了一个名为require的函数用来加载模块。要加载一个模块，只需要简单地调用就可以了
    - require("模块名")
    - require "模块名"
- 执行 require 后会返回一个由模块常量或函数组成的 table，并且还会定义一个包含该 table 的全局变量


## 11、元表（Metatable）
## 12、协同程序（coroutine）
## 13、文件I/O
## 14、错误处理
## 15、调试（Debug）
## 16、垃圾回收
## 17、面向对象
## 18、数据库访问
