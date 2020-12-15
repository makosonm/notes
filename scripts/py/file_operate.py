"""记录总结文件操作相关
"""


def way01():
    """采用with推荐使用"""
    with open("test.csv") as f:
        for line in f:
            print(line)


def way02():
    """直接open打开，如文件较大会占用很多内存"""
    f = open("test.csv")
    for row in f:
        print(row)


def way03():
    """每次读取指定的行数"""
    f = open("test.csv")
    while True:
        rows = f.readlines(10000)
        if not rows:
            break
        for row in rows:
            print(row)


def way04():
    """使用fileinput模块"""
    import fileinput
    import time

    for line in fileinput.input("test.csv"):
        print(line)


if __name__ == "__main__":
    way01()
