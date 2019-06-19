#!/usr/bin/env python
# __author__= 'w8ay'
import re
class spider():
    def run(self,url,html): # url,html是插件系统传递过来的链接和链接的网页源码。
        #print(html)
        pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
        email_list = re.findall(pattern, html)
        if(email_list):
            print(email_list)
            return True
        return False