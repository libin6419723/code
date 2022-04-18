#!/data/python/test/venv/bin/python3


import time
from datetime import datetime
#import peewee
import re


#m math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        print('__repr__');
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __repr__(self):
        print('__repr__');
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        print('__abs__')
        return hypot(self.x, self.y)

    def __bool__(self):
        print('__bool__')
        return bool(abs(self))

    def __add__(self, other):
        print('__add__')
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


#v1 = Vector(1, 2)
#v2 = Vector(3, 4)
#s = str(v1)
#print(v1 + v2)
#a = 'ab'
#b = 'ab'
#a = 'abcdefghijklmnopqrstuvwxyz'
#b = 'abcdefghijklmnopqrstuvwxyz'
#a = 'I am using long string for testing' * 100
#b = 'I am using long string for testing' * 100
#print(a is b)
#print(a)
#f = open('temp.txt', 'w');
#f.write('test');
#with open('temp.txt', 'w') as f:
#    f.write('test');
# a = None
# a ={}
#if a is None:
#    print("none")
#else:
#    print("not none")
if __name__ == '__main__':
    str = '[同步].Synchronic.2019.1080p.BluRay.DD+5.1.x264-iFT';
    #r = re.match("\[(.*?)\][\.](.*?)\.(\d\d\d\d)", str);
    r = re.sub("\[(.*?)\]", "", str);
    print(r);
    print(str);
    #print(r.groups());

