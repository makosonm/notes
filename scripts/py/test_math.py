"""测试相关
unitest 通用测试框架
doctest 简单一些的模块，是检查文档用的，也可以编写单元测试
"""


def square(x):
    """
    Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
