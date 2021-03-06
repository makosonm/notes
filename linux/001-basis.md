# Linux基础

* GUI \(Graphical User Interface\) 图形用户界面。用户界面的所有元素图形化，主要使用鼠标作为输入工具，点击图标执行程序，使用按钮、菜单、对话等尽心个交互，追求医用，看起来比较美
* CLI \(Command Line Interface\) 命令行界面。用户界面字符化，使用键盘作为输入工具，输入命令、选项、参数执行程序，追求高效，看起来比较酷

## 缩写习惯

### 1. 最常见的缩写，取每个单词的首字母

* `cd` `Change Directory`
* `dd` `Disk Dump`
* `df` `Disk Free`
* `du` `Disk Usage`
* `pwd` `Print Working Directory`
* `ps` `Processes Status`
* `PS` `Prompt Strings`
* `su` `Substitute User`
* `rc` `Run Command`
* `Tcl` `Tool Command Language`
* `cups` `Common Unix Printing System`
* `apt` `Advanced Package Tool`
* `bg` `BackGround`
* `ping` `Packet InterNet Grouper`

### 2. 如果首字母后为'h',通常保留

* `chsh` `CHange SHell`
* `chmod` `CHange MODe`
* `chown` `CHange OWNer`
* `chgrp` `CHange GRouP`
* `bash` `Bourne Again Shell`
* `zsh` `Z SHell`
* `ksh` `Korn SHell`
* `ssh` `Secure SHell`

### 3. 递归缩写类

* `GNU` `GUN's Not Unix`
* `PHP` `PHP; Hypertext Pregrocessor`
* `RPM` `RPM Package Manager`
* `WINE` `WINE Is Not an Emulator`
* `PNG` `PNG's Not GIF`
* `nano` `Nano's ANOther editor`

### 4. 如果只有一个单词，通常取每个音节的首字母

* `cp` `CoPy`
* `ln` `LiNk`
* `ls` `LiSt`
* `mv` `MoVe`
* `rm` `ReMove`

### 5. 对于目录，通常使用前几个字母作为缩写

* `bin` `BINaries`
* `dev` `DEVices`
* `etc` `ETCetera`
* `lib` `LIBrary`
* `var` `VARiable`
* `proc` `PROCesses`
* `sbin` `Superuser BINaries`
* `tmp` `TemPorary`
* `usr` `Unix Shared Resources`
* `diff` `DIFFerences`
* `cal`    `CALendar`
* `cat`    `CATenate`
* `ed`    `EDitor`
* `exec` `EXECute`
* `tab`    `TABle`
* `regexp` `REGular EXPression`

### 6. 如果某种缩写比较深入人心，例如"mesg"代表"message"，在新的复合缩写中，将沿用这种缩写方式

* `dmesg` `Diagnostic MESsaGe`
* `sed` `Stream EDitor`
* `stty` `Set TTY`
* `fstab` `FileSystem TABle`
* `passwd` `PASSWorD`

### 7. 有些缩写中，第一个字母'g'，代表'GNU'

* `awk` `Aho Weiberger and Kernighan`
* `gawk` `GNU AWK`
* `gpg` `GNU Privacy Guard`
* `grep` `GNU Regular Expression Print`
* `egrep` `Extended GREP`

## 命令选项，从a到z

* a
  * all: 全部，所有（ls, uname, lsattr）
  * archive: 存储\(cp, rsync\)
  * append: 附加 \(tar -A , 7z\)
* b
  * blocksize: 块大小，带参数 \(du , df\)
  * batch: 批处理模式 \(交互模式的程序通常拥有此选项，如 top -b\)
* c
  * commands : 执行命令，带参数 \(bash , ksh , python\)
  * create : 创建 \(tar\)
* d
  * debug : 调试
  * delete : 删除
  * directory : 目录 \(ls\)
* e
  * execute : 执行，带参数 \(xterm , perl\)
  * edit : 编辑
  * exclude : 排除
* f
  * force : 强制，不经确认\(cp , rm ,mv\)
  * file : 文件，带参数 \(tar\)
  * configuration file : 指定配置文件\(有些守护进程拥有此选项，如 ssh , lighttpd\)
* g
* h
  * --help : 帮助
  * human readable : 人性化显示\(ls , du , df\)
  * headers : 头部
* i
  * interactive : 交互模式，提示\(rm , mv\)
  * include : 包含
* k
  * keep : 保留
  * kill
* l
  * long listing format : 长格式\(ls\)
  * list : 列表
  * load : 读取 \(gcc , emacs\)
* m
  * message : 消息 \(cvs\)
  * manual : 手册 \(whereis\)
  * create home : 创建 home 目录 \(usermod , useradd\)
* n
  * number : 行号、编号 \(cat , head , tail , pstree , lspci\)
  * no : \(useradd , make\)
* o 
  * output : 输出 \(cc , sort\)
  * options : 选项 \(mount\)
* p
  * port : 端口，带参数 \(很多网络工具拥有此选项，如 ssh , lftp \)
  * protocol : 协议，带参数
  * passwd : 密码，带参数
* q
  * quiet : 静默
* r
  * reverse : 反转
  * recursive : 递归 \(cp , rm , chmod -R\)
* s
  * silent : 安静
  * size : 大小，带参数
  * subject
* t
  * tag
  * type: 类型（mount）
* u
  * user：用户名、UID、带参数
* v
  * verbose : 冗长
  * version : 版本
* w
  * width : 宽度
  * warning : 警告
* x
  * exclude : 排除 \(tar , zip\)
* y
  * yes
* z
  * zip : 启用压缩 \(bzip , tar , zcat , zip , cvs\)

## 学会使用`man`命令

> 下面以 `man date` 为例进行说明

![](../.gitbook/assets/basis-001.png) 

![](../.gitbook/assets/basis-002.png) 

* `man date`
  * DATE\(1\) 1代表的是一般用户可以执行的命令
  * Name 简短的命令，数据名称说明
  * SYNOPSIS 简单的命令执行语法简介
  * DESCRIPTION 命令较为完整的说明
  * FORMAT 格式化输出的详细数据
  * ENVIRONMENT 与这个命令相关的环境参数有如下说明
  * AUTHOR 这个命令的作者
  * REPORTING BUGS bugs  反馈地址
  * COPYRIGHT 收到著作权法的保护！用的就是 GPL
  * SEE ALSO 查看与 date 相关的说明
* 常见的数字的意义

| 数字 | 代表内容 |
| :--- | :--- |
| 1 | 用户在 shell 环境中可以操作的命令或可执行文件 |
| 2 | 系统内核可调用的函数与工具等 |
| 3 | 一些常用的函数（function）与函数库（library）大部分为 C 的函数库（libc） |
| 4 | 设备文件的说明，通常在 /dev 下的文件 |
| 5 | 配置文件或是某些文件的格式 |
| 6 | 游戏 games |
| 7 | 惯例与协议等，例如 Linux 文件系统、网络协议、ASCII code 等的说明 |
| 8 | 系统管理员可以执行的管理命令 |
| 9 | 跟 kernel 有关的文件 |

* Man page 大致分为下面几个部分

| 代号 | 内容说明 |
| :--- | :--- |
| NAME | 简短的命令，数据名称说明 |
| SYNOPTIONS | 简短的命令执行语法（syntax）简介 |
| DESCRIPTION | 较为完整的说明 |
| OPTIONS | 针对 SYNOPTIONS 部分中，有列举的所有可用的选项说明 |
| COMMANDS | 当这个程序（软件）在执行的时候，可以在此程序（软件）中执行的命令 |
| FILES | 这个程序或数据所使用或参考或连接到的某些文件 |
| SEE ALSO | 这个命令或数据相关的其他说明 |
| EXAMPLE | 一些参考的范例 |
| BUGS | 是否哟相关的错误 |

