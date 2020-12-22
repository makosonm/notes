# awk

## awk 的工作流程

![image](http://wiki.jikexueyuan.com/project/awk/images/awk_workflow.jpg)


## awk 标准选项
    
- -v 变量赋值
- --dump-variables[=file] 此选项会将全局变量及相应值按序输出到指定文件中。默认的输出文件名是 awkvars.out
- --lint[=fatal] 检查程序的可移植情况以及代码中的可疑部分。如果提供了参数 fatal，AWK 会将所有的警告信息当作错误信息处理
- --profile[=file] 这个选项会将程序文件以一种很优美的方式输出 默认输出文件是 awkprof.out

## awk 内置变量

- ARGC 表示在命令行提供的参数的个数
- ARGV 存储命令行输入参数的数组。数组的有效索引是从 0 到 ARGC-1
- CONVFMT 此变量表示数据转换为字符串的格式，其默认值为 %.6g
- ENVIRON 此变量是与环境变量相关的关联数组变量 `for (i in ENVIRON) print i, ENVIRON[i] # 遍历该数组`
- FILENAME 便是当前文件名
- FS 输入数据每列的分隔符
- OFS 输出数据每列的分隔符默认是空格    
- RS 输入数据每行的分隔符，默认为换行符
- ORS 输出数据每行的分隔符，默认为换行符
- NF 表示输出列的总数 如:`echo -e "One Two\nOne Two Three\nOne Two Three Four" | awk 'NF > 2'` 只输出超过两列的行
- NR 表示输出的总行数 如:`echo -e "One Two\nOne Two Three\nOne Two Three Four" | awk 'NR < 3'` 只输出前两行
- IGNORECASE 设置为1后，将便是 awk 对大小写不敏感
- PROCINFO 关联数组保存进程相关信息

## awk 内置变量

- rand 函数返回一个大于等于 0 小于 1 的随机数 N（0<= N < 1）
- sqrt(expr) 此函数计算 expr 的平方根
- srand([expr]) 
- asort(arr,[,d[,how]]) 对数组的值排序
- asorti(arr,[,d[,how]]) 对数组的索引排序
- gsub(regx, sub, string) gsub 是 global substitution 的缩写。它将出现的子串(sub) 替换为 regx.第三个参数 string 是可选的，默认是 $0
- index(str, sub) index 函数用于检测字符串 sub 是否是 str 的子串。如果 sub 是 str 的子串，则返回子串 sub 在字符串 str 的开始位置；若不是其子串，则返回 0。str 的字符位置索引从 1 开始计数
- length(str) 返回字符串的长度
- match(str, regex) 返回正则表达式在字符串 str 中第一个最长匹配的位置。匹配失败返回0
- split(str, arr, regex) split 函数使用正则表达式 regex 分割字符串 str。分割后的所有结果存储在数组 arr 中。如果没有指定 regex 则使用 FS 切分
- sprintf(format,expr-list)
- strtonum(str)
- sub(regex,sub,string) sub 函数执行一次子串替换。它将第一次出现的子串用 regex 替换。第三个参数是可选的，默认为 $0
- substr(str, start, l) substr 函数返回 str 字符串中从第 start 个字符开始长度为 l 的子串。如果没有指定 l 的值，返回 str 从第 start 个字符开始的后缀子串
- tolower(str)
- toupper(str)
- systime() 返回当前的时间戳
- mktime(dataspec) 此函数将字符串 dataspec 转换为与 systime 返回值相似的时间戳。 dataspec 字符串的格式为 YYYY MM DD HH MM SS
- strftime([format [, timestamp[, utc-flag]]]) 
	
	```
	awk 'BEGIN{ print strftime("Time=%Y%m%d %H:%M:%S", systime())}'
	```

- system 执行特定的命令然后返回其推出状态
- next 停止处理当前记录，并且进入到下一条记录的处理过程
	
	```
	awk '{if($0 ~/Shyam/) next; print $0}' mark.txt
	```

- getline 函数读入下一行
- delete 删除数组中元素
- close(expr) 关闭管道文件


## 输出重定向

- 管道
    
```
awk 'BEGIN{print "hello, world!!!" | "tr [a-z] [A-Z]" }'
# 输出 HELLO, WORLD!!!
```

- 双向通信管道

```
BEGIN {
	cmd = "tr [a-z] [A-Z]"              # 建立一个双向的通信通道
	print "hello, world !!!" |& cmd     # print 为 tr 提供输入,|&表示双向通信
	close(cmd, "to")                    # 执行后关闭 to 进程
	cmd |& getline out                  # 使用 getline 函数将输出存储到 out 变量中
	print out                           # 打印输出内容，最后关闭 cmd
	close(cmd)
}
```

## 问题总结

-  `awk FPAT` 模式需要 gawk 版本在 4 及以上生效 [here](https://www.gnu.org/software/gawk/manual/html_node/Splitting-By-Content.html#Splitting-By-Content)

```
文件内容：
Robbins,Arnold,"1234 A Pretty Street, NE",MyTown,MyState,12345-6789,USA
```

```awk
BEGIN {
	FPAT = "([^,]+)|(\"[^\"]+\")"
}

{
	print "NF = ", NF
	for (i = 1; i <= NF; i++) {
		printf("$%d = <%s>\n", i, $i)
	}
}

输出：awk —version = 3.1.7
NF =  5
$1 = <Robbins,Arnold,"1234>
$2 = <A>
$3 = <Pretty>
$4 = <Street,>
$5 = <NE",MyTown,MyState,12345-6789,USA>

输出：awk version 4.1.4
NF =  7
$1 = <Robbins>
$2 = <Arnold>
$3 = <"1234 A Pretty Street, NE">
$4 = <MyTown>
$5 = <MyState>
$6 = <12345-6789>
$7 = <USA>
```
