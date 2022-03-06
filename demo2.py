#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 21:36
# @Author  : 一叶知秋
# @File    : demo2.py
# @Software: PyCharm
from __future__ import print_function
import fileinput
import sys
import contextlib

if sys.version_info[0] == 2:
    input = raw_input
else:
    input = input

with contextlib.closing(fileinput.input(files=input())) as f:
    for line in f:
        line = line.rstrip()
        num = fileinput.lineno()
        print("#%d\t%s" % (num, line))
