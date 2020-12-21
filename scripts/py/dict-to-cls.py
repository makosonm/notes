#! -*- coding:utf-8 -*-

import json
import sys
from timeit import timeit

if sys.version_info.major == 3:
    from types import SimpleNamespace
    from munch import munchify
else:
    from collections import namedtuple
    from bunch import bunchify

class Dict2Cls(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Dict2Cls(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Dict2Cls(b) if isinstance(b, dict) else b)


class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        return Struct(value) if isinstance(value, dict) else value


json_data = '''{"result":{"suitable":[],"pageInfo":{"bg_time":1519704900,"has_union_apply":0,"phone_require":0,"vid":"","grade":"6002","ios_check":0,"subpay_price":0,"course_logo":"https://p.qpic.cn/qqconadmin/0/24f411c85f2842568d7017f1e5a9a22f/0","deadline":1588492183,"has_discount":0,"total":1000000,"is_small_term":0,"is_login":1,"subject":6002,"course_time_desc":"每天开课","knowledge":"","term_id":2000005534,"auto_in":0,"evaluate_info":{"evaluate_level":[{"score":0,"name":"满分班","level":"1"},{"score":80,"name":"实验班","level":"2"}],"evaluate_times":0,"max_evaluate_times":3,"evaluate_score":100,"evaluate_id":100,"evaluate_state":0},"purchase_status":0,"sys_time":1522326447288,"desc":"","type":7,"status":1,"first_time":1519704900,"evaluate_flag":100,"price":1,"cover_url":"https://p.qpic.cn/qqconadmin/0/15ce86d956904e0888b6719f6bbcc0ce/0","bg_color":"#69C188","dis_begin_time":0,"use_coupon_type":0,"coupon_disc":0,"teacher":[{"name":"alan-初中数学-1","pic":"https://pub.idqqimg.com/pc/misc/files/20180227/0e1404f1f4774259b6acbf1bf8c74db6.png","label":"alan-初中数学-1","content":"","exp":"[{&quot;icon&quot;:&quot;http://pub.idqqimg.com/pc/misc/files/20180227/075ceabc2bd64715b3be87e93e3e0b21.png&quot;}]","tid":2300001382,"good_rate":"-","desc":"alan-初中数学-1"}],"name":"在线教育_分班考试课程_初二数学","target":["现网测试专用"],"cid":12535,"sale":0,"addr_required":0,"express_time":"","end_time":1553845709,"directory":[{"title":"验证考试","bgtime":1519704900,"tid":2300001382,"csid":58817,"tname":"alan-初中数学-1","endtime":1519708800,"cs_type":0},{"title":"验证考试","bgtime":1519660800,"tid":2300001382,"csid":58818,"tname":"alan-初中数学-1","endtime":1519747199,"cs_type":0}],"dis_end_time":0,"reshelf":0}},"retcode":0}'''


#@profile
def T(method):
    data = json.loads(json_data)
    if method == 0:
        s = Struct(data)
        return s.result.pageInfo.directory[0].title
    if method == 1:
        s = Dict2Cls(data)
        return s.result.pageInfo.directory[0].title
    if method == 2: # python3版本中该函数速度最快
        if sys.version_info.major == 3:
            s = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))
            return s.result.pageInfo.directory[0].title
        s = json.loads(json_data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))
        return s.result.pageInfo.directory[0].title
    if method == 3:
        if sys.version_info.major == 3:
            s = munchify(data)
            return s.result.pageInfo.directory[0].title
        s = bunchify(data)
        return s.result.pageInfo.directory[0].title


# 测试结果内存占用均差不多主要耗费再json laods
# python3 -m memory_profiler dict-to-cls.py
#T(0)  # 42M
#T(1)  # 42M
#T(2)  # 41M
#T(3)

# python3 中使用 SimpleNamespace 最快
# python2 中使用 使用T(1) 速度最快 T(2) 非常差
#26.0841290951
#20.472784996
#5.96872591972 执行1000次
#26.2860958576
print(timeit("T(0)", setup="from __main__ import T", number=100000))
print(timeit("T(1)", setup="from __main__ import T", number=100000))
print(timeit("T(2)", setup="from __main__ import T", number=1000))
print(timeit("T(3)", setup="from __main__ import T", number=100000))

