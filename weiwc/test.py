#coding:utf-8
#!/bin/python


# 参数
spot = 2.45
strike = 2.50
maturity = 0.25
r = 0.05
vol = 0.25

# 基于Black - Scholes 公式的期权定价公式
from math import log, sqrt, exp
from scipy.stats import norm


def call_option_pricer(spot, strike, maturity, r, vol):
    d1 = (log(spot / strike) + (r + 0.5 * vol * vol) * maturity) / vol / sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)

    price = spot * norm.cdf(d1) - strike * exp(-r * maturity) * norm.cdf(d2)
    return price

print '期权价格 : %.4f' % call_option_pricer(spot, strike, maturity, r, vol)

#
#
# #################
#
#
import time
import numpy as np
#
# portfolioSize = range(1, 10000, 500)
# timeSpent = []
#
# for size in portfolioSize:
#     now = time.time()
#     strikes = np.linspace(2.0,3.0,size)
#     for i in range(size):
#         res = call_option_pricer(spot, strikes[i], maturity, r, vol)
#     timeSpent.append(time.time() - now)
# ######
# from matplotlib import pylab
# import seaborn as sns
#
# # font.set_size(15)
# font = "ylat"
# sns.set(style="ticks")
# pylab.figure(figsize=(12, 8))
# pylab.bar(portfolioSize, timeSpent, color='r', width=300)
# pylab.grid(True)
# print "ajaj"
# pylab.title(u'期权计算时间耗时（单位：秒）', fontproperties=font, fontsize=18)
# pylab.ylabel(u'时间（s)', fontproperties=font, fontsize=15)
# pylab.xlabel(u'组合数量', fontproperties=font, fontsize=15)
#
# # 2.2 使用numpy向量计算
#
# sample = np.linspace(1.0,100.0,5)
# np.exp(sample)
#
#
# # 使用numpy的向量函数重写Black - Scholes公式
# def call_option_pricer_nunmpy(spot, strike, maturity, r, vol):
#     d1 = (np.log(spot / strike) + (r + 0.5 * vol * vol) * maturity) / vol / np.sqrt(maturity)
#     d2 = d1 - vol * np.sqrt(maturity)
#
#     price = spot * norm.cdf(d1) - strike * np.exp(-r * maturity) * norm.cdf(d2)
#     return price
#
# timeSpentNumpy = []
# for size in portfolioSize:
#     now = time.time()
#     strikes = np.linspace(2.0,3.0, size)
#     res = call_option_pricer_nunmpy(spot, strikes, maturity, r, vol)
#     timeSpentNumpy.append(time.time() - now)
#
#
# pylab.figure(figsize = (12,8))
# pylab.bar(portfolioSize, timeSpentNumpy, color = 'r', width = 300)
# pylab.grid(True)
# pylab.title(u'期权计算时间耗时（单位：秒）- numpy加速版', fontproperties = font, fontsize = 18)
# pylab.ylabel(u'时间（s)', fontproperties = font, fontsize = 15)
# pylab.xlabel(u'组合数量', fontproperties = font, fontsize = 15)
# # pylab.show()
#
#
#
# fig = pylab.figure(figsize = (12,8))
# ax = fig.gca()
# pylab.plot(portfolioSize, np.log10(timeSpent), portfolioSize, np.log(timeSpentNumpy))
# pylab.grid(True)
# from matplotlib.ticker import FuncFormatter
# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$10^{%.0f}$' % (x)
# formatter = FuncFormatter(millions)
# ax.yaxis.set_major_formatter(formatter)
# pylab.title(u'期权计算时间耗时（单位：秒）', fontproperties = font, fontsize = 18)
# # pylab.legend([u'循环计算', u'numpy向量加速'], prop = font, loc = 'upper center', ncol = 2)
# pylab.ylabel(u'时间（秒)', fontproperties = font, fontsize = 15)
# pylab.xlabel(u'组合数量', fontproperties = font, fontsize = 15)
#
from scipy.optimize import brentq
#
#
# # 目标函数，目标价格由target确定
# spot = 2.45  # 当前价格
# strike = 2.50  # 行权价
# maturity = 0.25  # 到期期限  单位：年
# r = 0.05  # 无风险利率
# vol = 0.25  # 波动率
#

class cost_function    :
    def __init__(self, target):
        self.targetValue = target

    def __call__(self, x):
        return call_option_pricer(spot, strike, maturity, r, x) - self.targetValue


# 假设我们使用vol初值作为目标
target = call_option_pricer(spot, strike, maturity, r, vol)

cost_sampel = cost_function(target)

# 使用Brent算法求解
impliedVol = brentq(cost_sampel, 0.01, 0.5)

print u'真实波动率： %.2f' % (vol * 100,) + '%'
print u'隐含波动率： %.2f' % (impliedVol * 100,) + '%'