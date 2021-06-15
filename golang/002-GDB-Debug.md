# GDB调试go程序

## 系统信息

```shell
➜  notes git:(master) ✗ brew config
HOMEBREW_VERSION: 2.6.2
ORIGIN: https://github.com/Homebrew/brew
HEAD: 1a52862e6d24cd3bf87bec557a8886a1a825ee3c
Last commit: 7 days ago
Core tap ORIGIN: https://github.com/Homebrew/homebrew-core
Core tap HEAD: 74483394cf7577de5b715fcb0e9071d99c0fa2c0
Core tap last commit: 2 days ago
Core tap branch: master
HOMEBREW_PREFIX: /usr/local
HOMEBREW_CASK_OPTS: []
HOMEBREW_MAKE_JOBS: 4
HOMEBREW_NO_AUTO_UPDATE: set
http_proxy: http://127.0.0.1:1087
https_proxy: http://127.0.0.1:1087
Homebrew Ruby: 2.6.3 => /usr/local/Homebrew/Library/Homebrew/vendor/portable-ruby/2.6.3_2/bin/ruby
CPU: quad-core 64-bit haswell
Clang: 10.0 build 1000
Git: 2.29.2 => /usr/local/bin/git
Curl: 7.54.0 => /usr/bin/curl
Java: 13.0.1
macOS: 10.13.6-x86_64
CLT: 10.1.0.0.1.1539992718
Xcode: 10.1)
```

- go 版本

```shell
go version go1.15.6 darwin/amd64
```

- gdb版本

```shell
GNU gdb (GDB) 10.1)
```

## 安装设置

- `brew install gdb`
- `echo "set startup-with-shell off" >> ~/.gdbinit`
- 创建证书
  - 1、打开 Keychain Access -> Certificate Assistant -> Create a Certificate...
  - 2、设置
    - Name: gdb_cert;
    - Identity Type:Self Signed Root
    - Certifcate Type: Code Signing
    - 勾选 Let me override defaults
    - 一路下一步直到出现最后 Keychain: 选择 login(这里选择System的话会导致证书创建失败，先选择login模式后面进行导出后重新导入设置)
  - 3、设置密码导出证书
  - 4、导入证书把导出的证书拖到 Keychain Access-> System中即可
  - 5、codesign -f -s gdb_cert $(which gdb)
  - 6、如不生效重启电脑

- Go环境设置

  - `export GOFLAGS="-ldflags=-compressdwarf=false"` [参考](https://golang.org/doc/gdb#Known_Issues) 第4点

- 编译 `go build -gcflags "-N -l" -o main main.go`

- 调试demo

```shell
➜  apps gdb main
GNU gdb (GDB) 10.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-apple-darwin17.7.0".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from main...
Loading Go Runtime support.
(gdb) info files
Symbols from "/Users/mako/Work/github.com/pemako/apps/main".
Local exec file:
        `/Users/mako/Work/github.com/pemako/apps/main', file type mach-o-x86-64.
        Entry point: 0x1063f60
        0x0000000001001000 - 0x00000000010a6fd3 is .text
        0x00000000010a6fe0 - 0x00000000010ee3b8 is __TEXT.__rodata
        0x00000000010ee3c0 - 0x00000000010ee4e6 is __TEXT.__symbol_stub1
        0x00000000010ee500 - 0x00000000010eeca0 is __TEXT.__typelink
        0x00000000010eeca0 - 0x00000000010eed10 is __TEXT.__itablink
        0x00000000010eed10 - 0x00000000010eed10 is __TEXT.__gosymtab
        0x00000000010eed20 - 0x0000000001156e04 is __TEXT.__gopclntab
        0x0000000001157000 - 0x0000000001157020 is __DATA.__go_buildinfo
        0x0000000001157020 - 0x00000000011571a8 is __DATA.__nl_symbol_ptr
        0x00000000011571c0 - 0x00000000011656c0 is __DATA.__noptrdata
        0x00000000011656c0 - 0x000000000116c7f0 is .data
        0x000000000116c800 - 0x000000000119c210 is .bss
        0x000000000119c220 - 0x000000000119ef28 is __DATA.__noptrbss
(gdb) b *0x1063f60
Breakpoint 1 at 0x1063f60: file /usr/local/Cellar/go/1.15.6/libexec/src/runtime/rt0_darwin_amd64.s, line 8.
(gdb) b _rt0_amd64
Breakpoint 2 at 0x1060aa0: file /usr/local/Cellar/go/1.15.6/libexec/src/runtime/asm_amd64.s, line 15.
(gdb)  b runtime.rt0_go
Breakpoint 3 at 0x1060ac0: file /usr/local/Cellar/go/1.15.6/libexec/src/runtime/asm_amd64.s, line 89.
(gdb)
```
