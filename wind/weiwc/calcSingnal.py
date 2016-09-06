#coding:utf-8
#!/bin/python
__author__ = "weiwc"
'''
email:972237007@qq.com
date:20160727
'''

'''

'''


import redis



def calcSingnal(oldOp, newOp, oldBD, nweBD):
    delta = (newOp - oldOp)/(nweBD - oldOp)
    print "delta:", delta
    pass



def main():
    oldOp = 1
    newOp = 2
    oldBD = 1
    newBD = 2
    rc = redis.Redis(host="192.168.15.9", port=6379, db=3)
    ps = rc.pubsub()
    ps.subscribe(["000000"])

    for item in ps.listen():
        print item
        if (newBD - oldBD) == 0:
            print "nweBD - oldBD = 0"
        else:
            delta= (newOp - oldOp) / (newBD - oldBD)
            print delta
        hq =  rc.get(item["data"])
        if item["data"] == "510050":
            newBD = float(hq.split(",")[1])
            print "newBD:", newBD
        else:
            newOp = float(hq.split(",")[1])
            print "newOp:", newOp


if __name__ == '__main__':
    main()

