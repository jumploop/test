#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from operator import itemgetter

# 对下面给出的字典按值从大到小对键进行排序。
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
print(sorted(prices, key=lambda x: prices[x], reverse=True))
