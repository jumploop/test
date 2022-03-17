#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 传入一个有若干个整数的列表，该列表中某个元素出现的次数超过了50%，返回这个元素。
def more_than_half(items):
    temp, times = None, 0
    for item in items:
        if times == 0:
            temp = item
            times += 1
        else:
            if item == temp:
                times += 1
            else:
                times -= 1
    return temp


if __name__ == '__main__':
    print(more_than_half([1, 2, 3]))
