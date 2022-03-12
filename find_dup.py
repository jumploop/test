#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# 要求：列表中有1000000个元素，取值范围是[1000, 10000)，设计一个函数找出列表中的重复元素。
def find_dup(items):
    dups = [0] * 9000
    for item in items:
        dups[item - 1000] += 1
    for idx, value in enumerate(dups):
        if value > 1:
            yield idx + 1000


if __name__ == '__main__':
    nums = [random.randrange(1000, 10000) for _ in range(1000000)]
    print(list(find_dup(nums)))
