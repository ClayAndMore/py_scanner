
import sys
import urlparse
from script import bak_check
from lib.core import webcms,PortScan,webdir
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    # ww = PortScan.PortScan("115.29.233.149")
    # ww.work()

    qq = webdir.webdir("https://blog.yesfree.pw/",20)    
    qq.work()
    pp.output()
