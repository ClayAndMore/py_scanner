#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms, common, PortScan


reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    root = "https://shiyanlou.com"
    threadNum = 10
    ip = common.gethostbyname(root)
    print "IP:",ip
    print "Start Port Scan:"
    pp = PortScan.PortScan(ip)
    pp.work()

    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()

    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()
