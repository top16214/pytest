#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests

print(requests.__doc__)

url = "https://www.baidu.com"
r = requests.get(url)
print(r.status_code)

url = "https://www.google.com"
r = requests.get(url)
print(r.status_code)
