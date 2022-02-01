# -*- coding: utf-8 -*-
"""Bonus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HXbyOVbm246irSbMkLeV97sG9s0xjeOv
"""

from math import log, sqrt, pi, exp
from scipy.stats import norm
import numpy as np


def d1(S,X,T,r,sigma):
    return( log(S/X) + (r + sigma**2/2 )*T )/( sigma*sqrt(T) )
def d2(S,X,T,r,sigma):
    return d1(S,X,T,r,sigma) - sigma*sqrt(T)

def c(S,X,T,r,sigma): ## Call option function
    return S*norm.cdf(d1(S,X,T,r,sigma)) - X*exp(-r*T)*norm.cdf( d2(S,X,T,r,sigma) )
  
def p(S,X,T,r,sigma): ## Put option function
    return X*exp(-r*T)*norm.cdf(-d2(S,X,T,r,sigma))+S *norm.cdf(-d1(S,X,T,r,sigma))