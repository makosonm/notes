# brew

- 安装
    - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`


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

| :exclamation:  如果使用oh-my-zsh 需要重新编译 zcompdump|
|-----------------------------------------|

`rm -f ~/.zcompdump; compinit`



### fish 配置
