#encoding=UTF-8  
''''' 
Created on 2014年6月30日 
 
@author: jin 
'''  
from numpy import *  # so can use mat()  array() directly
import matplotlib.pyplot as plt  
from random import *  
  
def loadData():  
    x = arange(-1,1,0.02)  #100个样点
    y = ((x*x-1)**3+1)*(cos(x*2)+0.6*sin(x*1.3))   #用最高9次的线性方程组，拟合这条三角曲线
    #生成的曲线上的各个点偏移一下，并放入到xr,yr中去  
    xr=ndarray(shape(x));yr=ndarray(shape(y));i = 0  
    for xx in x:  
        yy=y[i]  
        d=float(randint(90,110))/100  
        xr[i]=xx*d  
        yr[i]=yy*d
        i+=1   
    return x,y,xr,yr  

def XY(x,y,order):  
    X=[]  
    for i in range(order+1):  
        X.append(x**i)  #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'  but numpy.ndarray is OK
    X=mat(X).T  
    Y=array(y).reshape((len(y),1))  
    return X,Y  

def figPlot(name,x1,y1,x2,y2,label1="line1",label2="line2"): 
    plt.figure(name) 
    plt.plot(x1,y1,color='g',linestyle='-',marker='',label=label1)  
    plt.plot(x2,y2,color='m',linestyle='',marker='.',label=label2)   

def Main():      
    x,y,xr,yr = loadData()  
    figPlot("figure1 origin and noisy one",x,y,xr,yr,"origin","* 0.8~1.2") 
    print("type(x)",type(x))
    print("type(xr)",type(xr))
    X,Y = XY(x,y,9)  #为啥不用 xr yr(有噪声) 来乘方（线性方程组）来算B，却用xr ,yr比较
    XT=X.transpose()#X的转置  
    B=dot(dot(linalg.inv(dot(XT,X)),XT),Y)#套用最小二乘法公式  , 求出系数B
    myY=dot(X,B)  #带入回去求重新估算的Y
    print("shape(x):",shape(x))
    print("shape(B):",shape(B))
    figPlot("figure2 model trained by origin",x,myY,x,y,"orginal trained model","origin") 

    #原始生成的数据加上噪声再来训练模型
    Xr,Yr = XY(xr,yr,9)  
    XTr=Xr.transpose() 
    Br=dot(dot(linalg.inv(dot(XTr,Xr)),XTr),Yr)
    myYr=dot(X,Br)  #带入回去原始求重新估算的Y
    figPlot("figure3 model trained by noisy one and origin data",x,myYr,x,y,"model trained by noisy one","origin") 
    figPlot("figure4 model trained by noisy one and noisy data",x,myYr,xr,yr,"model trained by noisy one","origin with noise") 
    plt.show() 

Main()  