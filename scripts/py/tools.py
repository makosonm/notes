"""本文件主要记录一些常用的脚本信息
"""

import datetime
import heapq

import requests


def date_range1(start, end):
    """获取从指定开始时间到指定结束时间的列表"""
    days = (
        datetime.datetime.strptime(end, "%Y%m%d")
        - datetime.datetime.strptime(start, "%Y%m%d")
    ).days + 1

    return [
        datetime.datetime.strftime(
            datetime.datetime.strptime(start, "%Y%m%d") + datetime.timedelta(i),
            "%Y%m%d",
        )
        for i in range(days)
    ]


def date_range2(begin_date, end_date):
    """获取从指定开始时间到指定结束时间的列表"""
    dates = []
    tmpdate = datetime.datetime.strptime(begin_date, "%Y%m%d")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        tmpdate = tmpdate + datetime.timedelta(1)
        date = tmpdate.strftime("%Y%m%d")

    return dates


def get_user_real_ip():
    """获取用户真实IP地址"""
    urls = ["http://ip.42.pl/raw", "http://ip.42.pl/raw", "http://jsonip.com"]
    ips = []
    for url in urls:
        res = requests.get(url)
        ips.append(res.text)
    return ips


def use_heapq():
    """在某个集合中找出最大或最小的N 个元素
    - 使用 heapq 模块中的两个函数 ---nlargest() 和 nsmallest()
    - 这两个函数可以接受第三个参数 key 工作在更复杂的数据结构上
    """

    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "APPLE", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HFQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35},
        {"name": "ACME", "shares": 75, "price": 115.65},
    ]

    larger = heapq.nlargest(1, portfolio, key=lambda s: s["price"])
    small = heapq.nsmallest(1, portfolio, key=lambda s: s["shares"])
    print(larger, small)


if __name__ == "__main__":
    # print(date_range1("20200101", "20200110"))
    # print(date_range2("20200101", "20200110"))
    # get_user_real_ip()
    use_heapq()
