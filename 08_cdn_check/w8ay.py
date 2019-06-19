#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms,PortScan,common,webdir,fun_until

reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    root = "https://www.shiyanlou.com/"
    threadNum = 10
    # CDN Check
    print "CDN check...."
    msg,iscdn =  fun_until.checkCDN(root)
    print msg
    if iscdn:
        #IP Ports Scan
        ip = common.gethostbyname(root)
        print "IP:",ip
        print "START Port Scan:"
        pp = PortScan.PortScan(ip)
        pp.work()
    
    # DIR Fuzz
    dd = webdir.webdir(root,threadNum)    
    dd.work()
    dd.output()
    
    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()
    
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()