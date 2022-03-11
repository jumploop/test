#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
from random import random
from time import sleep
import requests
import logging

formatter = '%(asctime)s %(levelname)s %(filename)s[%(lineno)d]: %(message)s'

logging.basicConfig(level=logging.DEBUG, format=formatter, datefmt='%Y:%m:%d %H:%M:%S', encoding='utf-8')


def retry(*, retry_times=3, max_wait_secs=5, errors=(Exception,)):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retry_times):
                logging.info('第%s次下载', i + 1)
                try:
                    func(*args, **kwargs)
                except errors as err:
                    logging.error('第%s次下载失败，error %s', i + 1, err)
                    sleep(random() * max_wait_secs)
            return None

        return wrapper

    return decorate


class Retry(object):
    def __init__(self, *, retry_times=3, max_wait_secs=5, errors=(Exception,)):
        self.retry_times = retry_times
        self.max_wait_secs = max_wait_secs
        self.errors = errors

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.retry_times):
                logging.info('第%s次下载', i + 1)
                try:
                    func(*args, **kwargs)
                except self.errors as err:
                    logging.error('第%s次下载失败，error %s', i + 1, err)
                    sleep(random() * self.max_wait_secs)
            return None

        return wrapper


@Retry()
def download(url, timeout=1):
    response = requests.get(url, timeout=timeout)
    logging.info("response %s",response.text)
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.text)


if __name__ == '__main__':
    download('wwww.google.com')
