#coding:utf-8
#!/bin/python
__author__ = "weiwc"
'''
email:972237007@qq.com
date:20160727
'''

'''

'''
# 内置模块
import math
import time
from math import log,sqrt,exp
# 第三方模块
import numpy as np
import scipy
from scipy.stats import norm
# 自己写的模块
'''
关于这样的简单欧式期权的定价，有经典的Black - Scholes[1]公式：
    Call(S, K, r, τ, σ)d1d2 = SN(d1)−Ke−rτN(d2), = ln(S / K) + (r + 12σ2)τστ√, =d1−στ√.
其中S为标的价格，K为执行价格，r为无风险利率，τ = T−t为剩余到期时间。 N(x)为标准正态分布的累积概率密度函数。
Call(S, K, r, τ, σ)为看涨期权的价格。
'''

class optionDemo(object):
    def __init__(self):
        self.spot = 2.45  # 当前价
        self.strike = 2.50  # 行权价
        self.maturity = 0.25  # 到期期限
        self.r = 0.05  # 无风险利率
        self.vol = 0.25  # 波动率

        self.portfolioSize = range(1, 10000, 500)
        self.timeSpend = []


    def calcCallOptionPricer(self,spot, strike, maturity, r, vol):
        '''计算期权价格'''
        try:
            d1 = (log(spot/strike) + (r + 0.5 * vol * vol) * maturity)/vol/sqrt(maturity)
            d2 = d1 - vol * sqrt(maturity)
            price = spot * norm.cdf(d1) - strike * exp(-r * maturity) * norm.cdf(d2)
            return price
        except Exception,errMsg:
            print "计算期权价格出错", errMsg
            return False

    def quiklyCalc(self):
        '''利用numpy 提高计算速度'''
        try:

            for size in self.portfolioSize:
                now = time.time()
                # print "now:", now
                strikes = np.linspace(2.0, 3.0, size)
                # print "size:", size
                for i in range(size):
                    res = self.calcCallOptionPricer(self.spot, strikes[i], self.maturity, self.r, self.vol)

                self.timeSpend.append(time.time() - now)
        except Exception,errMsg:
            print "Error: %s" % (errMsg.message)
            return False

    def lineGriphic(self):
        from matplotlib import pylab
        import seaborn as sns
        # pylab.size(15)
        # font = pylab.size(15) #set_size(15)
        sns.set(style="ticks")
        font = self.timeSpend
        pylab.figure(figsize=(12,8))
        pylab.bar(self.portfolioSize, self.timeSpend, color="r", width=300)
        pylab.grid(True)
        pylab.title("期权计算耗时（单位：秒）", fontproperties=font,fontsize=18)
        pylab.ylabel("时间（s）", fontproperties=font,fontsize=15)
        pylab.xlabel("组合数量）", fontproperties=font, fontsize=15)







def main():
    od = optionDemo()
    optionPrice = od.calcCallOptionPricer(od.spot, od.strike, od.maturity, od.r, od.vol)
    print "期权价格为：%.4f" % (optionPrice)
    # od.quiklyCalc()
    od.lineGriphic()

    # print "期权价格为：%2f" % 12365.456877
    # print "期权价格为：%.2f" % 12365.456877
    # print "期权价格为：%3f" % 12365.456877
    pass


if __name__ == "__main__":
    print "__name__:", __name__
    main()