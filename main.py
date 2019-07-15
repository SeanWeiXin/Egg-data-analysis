#!/usr/bin/env python
# coding=utf-8

#
# @Version : 0.1
# @Time    : 2018/04/01 8:41
# @Author  : Terrace Sean Wei
# @File    : EGG Future.py
#
# 鸡蛋周报图表

#基础数据包
import numpy as np
import pandas as pd
from pandas import DataFrame
from datetime import *
import math as m

#数据分析包
import statsmodels.api as sm
import statsmodels.tsa.api as smts
import statsmodels.tsa.stattools as ts
import statsmodels.formula.api as smf

#作图包
import matplotlib.pyplot as plt
import seaborn as sns

#数据引入包
import xlrd
##Wind接口
from WindPy import w
w.start()
