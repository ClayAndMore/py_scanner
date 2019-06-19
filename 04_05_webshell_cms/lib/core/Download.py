#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import urllib3

class Downloader(object):
    # 解决： requests.exceptions.SSLError: HTTPSConnectionPool(host='****.org', port=443): Max retries exceeded with url
    s = requests.session()
    s.keep_alive = False

    # 解决： InsecureRequestWarning: Unverified HTTPS request is being made.
    urllib3.disable_warnings()

    def get(self,url):
        # verify, 忽略证书认证，requests请求时证书认证失败的问题
        r = requests.get(url,timeout=10, verify=False)  # verify ： 解决HTTPSConnectionPool
        if r.status_code != 200:
            return None
        _str = r.text
        return _str

    def post(self,url,data):
        r = requests.post(url,data, verify=False)
        _str = r.text
        return _str
    
    def download(self, url,htmls):
        if url is None:
            return None
        _str = {}
        _str["url"] = url
        try:
            r = requests.get(url, timeout=10, verify=False)
            if r.status_code != 200:
                return None
            _str["html"] = r.text
        except Exception, e:
            print Exception,":",e

        htmls.append(_str)