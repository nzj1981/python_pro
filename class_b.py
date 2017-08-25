#!/usr/bin/env python
#coding=utf-8

# 重写一般方法
class ClassA:
    def __init__(self):
        print('this is ClassA method')
    
    def say(self):
        print('I am ClassA')
class ClassB(ClassA):
    def __init__(self):
        print('this is ClassB method')
    pass
    # 重写ClassA方法
    '''
    def say(self):
        print('I am ClassB')
    '''


if __name__ == '__main__':
    a = ClassA()
    a.say()
    b = ClassB()
    b.say()


    