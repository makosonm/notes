# 一键升级Python包

> 首先升级pip，确保拥有最新的pip程序源 `pip install --upgrade pip`

## 查看哪些包需要升级

- `pip list --out` 或 `pip list --outdated`

```
➜  ~ pip list --outdate
Package                                Version  Latest Type
-------------------------------------- -------- ------ -----
altgraph                               0.10.2   0.17   wheel
asn1crypto                             0.24.0   1.4.0  wheel
cffi                                   1.14.3   1.14.4 wheel
cryptography                           2.6.1    3.3.1  wheel
enum34                                 1.1.6    1.1.10 wheel
future                                 0.17.1   0.18.2 sdist
ipaddress                              1.0.22   1.0.23 wheel
macholib                               1.5.1    1.14   wheel
matplotlib                             1.3.1    2.2.5  wheel
modulegraph                            0.10.4   0.18   wheel
numpy                                  1.8.0rc1 1.16.6 wheel
```


## 一键升级脚本

```python
# -*- coding:utf8 -*-

__author__ = 'makosonm@gmail.com'


import pip
import platform
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions


if __name__ == '__main__':
    for dist in get_installed_distributions():
        if  platform.python_version_tuple()[0] == '3':
            call("pip3 install --upgrade " + dist.project_name, shell=True)
        else:
            call("pip install --upgrade " + dist.project_name, shell=True)
```

## shell脚本

```shell
pip freeze --local | grep -v '^-e' | cut -d = -f 1 | xargs -n1 pip install -U
```
