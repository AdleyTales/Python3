# -*- coding: utf-8 -*-

from collections import Iterable

l = ['hsfkdj','1232','true','nnn','mmmm',1212]
print(l[:2]) #前两项
print(l[-3:]) #后边3项

print('#########################')

t = list(range(100))
print(t[:20:2])

print('#########################')

s = 'jdskfjksdfjks'
print(s[2:6])

print('#########################')
y = (1,2,34,5,6,7,8,9,343)
print(y[-4:]) #还是元祖

print('#########################')
# 迭代
d = {'name':'xiaoming','age':123,'salary':15000}
for key in d:
    print(key)

print('#########################')
for value in d.values():
    print(value)

print('#########################')
for k,v in d.items():
    print('k:',k,'v:',v)

print('#########################')
ss = [x*x for x in range(1,16) if x%2 == 0]  
print(ss)

print('#########################')
li = [1,2,3,4,5]
print(isinstance(li,Iterable))