#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys
from lib.core import webcms, PortScan
from lib.core.Spider import SpiderMain
reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    root = "http://struts.apache.org/"
    threadNum = 10
    #spider
    #w8 = SpiderMain(root,threadNum)
    #w8.craw()

    # webcms
    www = webcms.webcms(root,1)
    www.run()

if __name__ == '__main__':
    main()