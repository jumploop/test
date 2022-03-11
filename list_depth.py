#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_depth(items):
    if isinstance(items, list):
        max_depth = 1
        for item in items:
            max_depth = max(list_depth(item) + 1, max_depth)
        return max_depth
    return 0


if __name__ == '__main__':
    print(list_depth([1, 2, 3]))
    print(list_depth([[1], [2, [3]]]))