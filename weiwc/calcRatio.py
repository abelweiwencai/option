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
from math import log,sqrt,exp
# 第三方模块
import numpy
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


    def calcOption(self):
        pass




def main():
    pass


if __name__ == "__main__":
    print "__name__:", __name__
    main()