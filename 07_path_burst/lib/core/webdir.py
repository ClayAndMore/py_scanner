#!/usr/bin/env python
# __author__= 'w8ay'
import os
import sys
import Queue
import requests
import threading

class webdir:
    def __init__(self,root,threadNum):
        self.root = root
        self.threadNum = threadNum
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
             'Referer': 'http://www.shiyanlou.com',
             'Cookie': 'whoami=w8ay',
             }
        self.task = Queue.Queue()
        self.s_list = []
        filename = os.path.join(sys.path[0], "data", "dir.txt")
        for line in open(filename):  
            self.task.put(root + line.strip())
    
    def checkdir(self,url):
        status_code = 0
        try:
            r = requests.head(url,headers=self.headers) # 为了提升检测网站的速度，我们只需要用head访问网页头来判断返回的状态码即可：
            status_code = r.status_code
        except:
            status_code = 0
        return status_code

    def test_url(self):
        while not self.task.empty():
            url = self.task.get()
            s_code = self.checkdir(url)
            if s_code==200:
                self.s_list.append(url)
            print "Testing: %s status:%s"%(url,s_code)
    
    def work(self):
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self.test_url())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The DirScan is complete!')

    def output():
        if len(self.s_list):
            print "[*] status = 200 dir:"
            for url in s_list:
                print url