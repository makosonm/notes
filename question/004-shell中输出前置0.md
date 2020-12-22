# Linux输出前置的0

今天遇到一个问题需要处理一下数字对文件进行内容进行相应的替换代码如下

```shell
for i in `seq -w 01 12`;do
    j=$(expr $i + 1) # 想要输出此处的 j 有前置的0
    j=$(expr $i + 1 | awk '{printf("%02d",$0)}') # 使用 awk printf 进行规范输出格式
    echo $j
done
```
