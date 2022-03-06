#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 17:34
# @Author  : 一叶知秋
# @File    : multiply.py
# @Software: PyCharm
from functools import partial
from operator import mul


def multiply():
    return [lambda x: x * i for i in range(4)]


print([m(100) for m in multiply()])


def multiply():
    return (lambda x: i * x for i in range(4))


print([m(100) for m in multiply()])


def multiply():
    for i in range(4):
        yield lambda x: x * i


print([m(100) for m in multiply()])


def multiply():
    return [partial(mul, i) for i in range(4)]


print([m(100) for m in multiply()])
