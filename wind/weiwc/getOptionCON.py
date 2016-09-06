#coding:utf-8
#!/bin/python
__author__ = "weiwc"
'''
email:972237007@qq.com
date:20160713
'''

'''
本文件主要是从sina获取期权合约
'''

import urllib2
import re

class getOptinCON(object):
    def __init__(self):
        self.months = ["1605", "1606", "1607"]
        self.codes = ["510050"]
        self.row_url = "http://hq.sinajs.cn/list="
        self.directions = ["OP_UP_", "OP_DOWN_"]
        self.all_url = []
        self.all_codes = []

    def getUrls(self):
        for dirc in self.directions:
            for co in self.codes:
                for mo in self.months:
                    tmp_url = self.row_url + dirc + co + mo
                    print tmp_url
                    self.all_url.append(tmp_url)

    def getCON(self,inUrl):

        #
        CON = []
        try:
            data = urllib2.urlopen(inUrl,timeout=5).read()
            # print data

            # data = re.sub(data,)
            data = data.replace("var hq_str_OP_UP_","")
            data = data.replace("var hq_str_OP_DOWN_", "")
            data = data.replace("CON_OP_", "")
            data = data.replace(";", "")
            data = data.replace("\"", "")
            data = data[11:]
            data = data[:-2]
            CON = data.split(",")

            print data
        except Exception, msg:
            print "get error:", msg
            return []
        return CON


    def getAllCON(self):
        # codes = []
        for x in self.all_url:
            codes = self.getCON(x)
            self.all_codes = self.all_codes + codes
        for y in self.all_codes:
            print y






def main():
    c = getOptinCON()
    c.getUrls()
    c.getAllCON()


if __name__ == "__main__":
    main()