#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取大文件
with open('demo.py', 'r', encoding='utf-8') as file:
    for data in iter(lambda: file.read(2097152), ''):
        print(data)

# 类动态添加新属性，对象属性访问权限

class A:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

obj = A(1)
obj.__value = 2
print(obj.value)
print(obj.__value)
