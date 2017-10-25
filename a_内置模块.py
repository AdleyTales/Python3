# -*- coding: utf-8 -*-

from datetime import datetime


now = datetime.now()

print(now)

print('=====================================')

dt = datetime(2015, 4, 19, 12, 20)

print(dt)  # 2015-04-19 12:20:00

# 时间戳
timestamp = now.timestamp()
print(timestamp)

timestamp = dt.timestamp()
print(timestamp)

# 时间戳转datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))


print('2222222222222222222222222222222222222')

#base64

import base64


str = 'jfdksjhk'

a = base64.b64encode(str.encode('utf-8'))
print(a)
