#!../venv/bin/python3

from classes.Time import Time

import time
from datetime import datetime
import peewee

## 变量交换
'''
a=1
b=2
a,b = b,a
print(a,b)
'''

## 列表推导
my_list = [ i for i in range(1, 100) if i % 2 == 0 ]
# print(my_list)

## 带索引遍历
# for i, k in enumerate(my_list):
#    print(i, k)

## 序列解包
for i, k in enumerate(my_list):
    print(i, k);
exit(0)

a, *k = my_list
print(a, k)

## 字符串拼接
# list = [ 'a', 'b', 'c', 'c' ];
# print(''.join(list))

## 真假判断

attr = False
print('here')
if attr:
    print('attr is truthy!')

if not attr:
    print('attr is falsey!')

if attr is None:
    print('attr is None!')

## 文件读取
with open("f.txt") as f:
    for line in f:
        print(line)

## 链式比较
age = 10
if 18 < age < 28:
    print("Young man");




