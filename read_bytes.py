#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    try:
        with open('demo.py', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('示例.txt', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
