# brew

- 安装

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 使用

```
brew install wget
brew install --cask firefox
```

## Homebrew on Linux

> Homebrew on Linux Community [linuxbrew-core](https://github.com/Homebrew/linuxbrew-core)

- Requirements
	- `GCC 4.7.0 or newer`
	- `Linux 2.6.32 or newer`
	- `Glibc 2.13 or newer`
	-  `64-bit x86_64 CPU`


- Debian or Ubuntu
	- `sudo apt-get install build-essential curl file git`

- Fedora, CentOS, or Red Hat
	- `sudo yum -y groupinstall 'Development Tools'`
	- `sudo yum install curl file git`
	- `sudo yum install libxcrypt-compat` # needed by Fedora 30 and up

- 替代的安装方式

> Extract or git clone Homebrew wherever you want. Use /home/linuxbrew/.linuxbrew if possible (to enable the use of binary packages).

```shell
git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew
mkdir ~/.linuxbrew/bin
ln -s ~/.linuxbrew/Homebrew/bin/brew ~/.linuxbrew/bin
eval $(~/.linuxbrew/bin/brew shellenv)
```


## Homebrew命令补全

### bash 配置

- 在 `~/.bash_profile` 或 `~/.profile` 文件中添加如下脚本

```shell
if type brew &>/dev/null; then
  HOMEBREW_PREFIX="$(brew --prefix)"
  if [[ -r "${HOMEBREW_PREFIX}/etc/profile.d/bash_completion.sh" ]]; then
    source "${HOMEBREW_PREFIX}/etc/profile.d/bash_completion.sh"
  else
    for COMPLETION in "${HOMEBREW_PREFIX}/etc/bash_completion.d/"*; do
      [[ -r "$COMPLETION" ]] && source "$COMPLETION"
    done
  fi
fi
```

### zsh 配置

- 在 `~/.zshrc` 文件中添加如下内容

```shell
if type brew &>/dev/null; then
  FPATH=$(brew --prefix)/share/zsh/site-functions:$FPATH

  autoload -Uz compinit
  compinit
fi
```

{% hint style="warning" %}
如果使用oh-my-zsh 需要重新编译 zcompdump
{% endhint %}

```
rm -f ~/.zcompdump; compinit
```

{% hint style="warning" %}
加载zcompdump时如果出现 zsh compinit: insecure directories 需要执行下面命令
{% endhint %}

```
chmod -R go-w "$(brew --prefix)/share"
```

### fish 配置

把下面内容添加到 `~/.config/fish/config.fish`文件中

```sh
if test -d (brew --prefix)"/share/fish/completions"
    set -gx fish_complete_path $fish_complete_path (brew --prefix)/share/fish/completions
end

if test -d (brew --prefix)"/share/fish/vendor_completions.d"
    set -gx fish_complete_path $fish_complete_path (brew --prefix)/share/fish/vendor_completions.d
end
```


###  常用命令

#### 依赖相关

- 列出某个软件的依赖

```
brew deps vim
```

- 查看所以的依赖信息

```
brew deps --formula --installed --tree

autojump
└── python@3.9
    ├── gdbm
    ├── openssl@1.1
    ├── readline
    ├── sqlite
    │   └── readline
    └── xz
curl
├── brotli
├── libidn2
│   ├── gettext
│   └── libunistring
├── libmetalink
├── libssh2
│   └── openssl@1.1
├── nghttp2
│   ├── c-ares
│   ├── jemalloc
│   ├── libev
│   └── openssl@1.1
├── openldap
│   └── openssl@1.1
├── openssl@1.1
├── rtmpdump
│   └── openssl@1.1
└── zstd
```

#### 列出哪些包需要更新

```
brew outdated
```

#### 锁定包不更新

```
brew pin $FORMULA    # 锁定
brew unpin $FORMULA  # 解除锁定
```

### 参考

- https://blog.jpalardy.com/posts/untangling-your-homebrew-dependencies/
