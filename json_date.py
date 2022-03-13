#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from urllib.parse import quote


def main():
    key = input("Enter your key:")
    headers = {
        'Accept':
        'application/json',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    url = 'http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key={key}&bk_length=600'.format(
        key=quote(key))
    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    print(resp.json())
    data_model = json.loads(resp.text)
    for news in data_model['card']:
        print(news)


if __name__ == '__main__':
    main()
