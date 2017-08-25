#!/usr/bin/env python
#coding=utf-8

# 构造方法实例 
class ClassA:
    def __init__(self):
        print("this is ClassA __init__ method")
    def init(self,value1 = ""):
        print("this is ClassA init method")
        print("value1 is %s" %value1)

    
if __name__ == '__main__':
    a = ClassA()
    a.init("hello")


    