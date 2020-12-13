# -*- coding:utf8 -*-

__author__ = "makosonm@gmail.com"


import platform
from subprocess import call

from pip._internal.utils.misc import get_installed_distributions

if __name__ == "__main__":
    for dist in get_installed_distributions():
        if platform.python_version_tuple()[0] == "3":
            call("pip3 install --upgrade " + dist.project_name, shell=True)
        else:
            call("pip install --upgrade " + dist.project_name, shell=True)
