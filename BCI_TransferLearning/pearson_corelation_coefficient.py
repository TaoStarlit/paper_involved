# coding:utf-8
# import numpy #numpy.ndarray
import numpy as np #np.np.ndarray
#from numpy import * #ndarray ,but no info

#import scipy.stats.pearsonr as pearsonr # no info too
#from scipy.stats import *
import scipy.stats as stats
from random import *  

X = np.arange(0,10,1)
Y = np.arange(0,20,2)

Yminus = np.arange(0,-20,-2)

Yr = np.ndarray(np.shape(X))
i=0
for x in X:
    d = float(randint(80,120))/100
    Yr[i]=x*d
    i+=1

print("P(X,Y)",stats.pearsonr(X,Y))
print("P(X,Yminus)",stats.pearsonr(X,Yminus))
print("P(X,Yr)",stats.pearsonr(X,Yr))