#!../venv/bin/python3


import re

## 操作符
# + * [] [:] in not in r/R %
s = 'aHello world!'
'''
print(s[3]);
print(s[3:]);
print(s[2:5]);
print('Hello' in s)
'''

## 函数
print(s.capitalize())
print(s.center(100))
print(s.count('l', 1, 4))
# decode/encode
# endswith
print(s.endswith('World!'));
print(s.startswith('He'));
# expandables
print(s.find('llx'));

## 格式化
### 数字
'''
print("{:.2f}".format(3.1415926));
print("{:+.2f}".format(3.1415926));
print("{:+.2f}".format(-3.1415926));
print("{:0>2d}".format(3));
print("{:x<4d}".format(3));
print("{:,d}".format(1000000));
print("{:.2%}".format(3.1415926));
print("{:.2%}".format(14));
print("{:.2e}".format(14));
print("{:<10d}".format(1000000));
print("{:>10d}".format(1000000));
print("{:^10d}".format(1000000));
'''

### 其他进制
'''
print("{:b}".format(11));
print("{:d}".format(11));
print("{:o}".format(11));
print("{:x}".format(11));
print("{:#x}".format(11));
print("{:#X}".format(11));
'''


