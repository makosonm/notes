# asciinema

## 安装

```
brew install asciinema
```

## 相关命令 

### `rec [filename]`

通过运行 `asciinema rec [filename]` 可以启动一个新的记录会话。记录的命令（进程）可以用`-c`选项指定，默认为`$SHELL`,

- 如果不指定`filename`结果上传到`asciinema-server`默认为`asciinema.org`
- 指定 `filename` 则可以可以进行 play <filename> adn/or 上传到asciinema server

```
asciinema rec ../.gitbook/assets/asciinema.json
```

### `play <filename>`

- 播放时下面监控操作可以
    - `Space` 播放暂停
    - `.` (当暂停时)步进一次记录一个帧
    - `Ctrl+C` 退出

- `播放本地文件`

```
asciinema play ../.gitbook/assets/asciinema.json
```

- `播放暂停HTTP(S) URL`

```
asciinema play https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd
```

- 重标准输入播放

```
cat .gitbook/assets/asciinema.json | asciinema play -

ssh user@host cat asciicast.cast | asciinema play -
```

### `cat <filename>`

当asciinema播放<filename>使用存储在asciicast中的时间信息回放记录的会话时，asciinema cat <filename>立即将完整的输出(包括所有转译序列)转储到一个终端。


### `upload <filename>`

上传记录

### `auth`

账号id 与asciinema.org用户帐户链接


## 嵌入


- HTML

```
<a href="https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd">
	<img src="https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd.png" width="836"/>
</a>
```

- Markdown

```
[![asciicast](https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd.png)](https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd)
```

[![asciicast](https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd.png)](https://asciinema.org/a/61aAMcZc5SMK0ByFZMyXwSXdd)


{% hint style="info" %}
详细信息参考 https://asciinema.org/docs/how-it-works
{% endhint %}
