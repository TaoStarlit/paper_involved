# coding:utf-8
least squere
假设模型（线性方程），知道数据，反推模型参数
#本例子，用最高9次的线性方程组（0次到9次，十个参数），拟合这条三角曲线
#数据(X,Y), 模型参数B

首先给出最小二乘解的矩阵形式的公式：

XB=Y ---> B=(X^T X)^-1 X^T Y


推导过程：
given XB=Y
--> X^T XB= X^T Y        multiple X^T
--> B=(X^T X)^-1 X^T Y   

?? why not directly mulitple X^-1 and the B=X^-1 Y
because (X^T X)^-1  is easier than X^-1 ??
no!  it's because sometime the X^-1 doesn't exit, so it need a normalized one


条件：
矩阵必须是列满秩矩阵，否则的逆就不会存在。



若A为m×n的矩阵，b为m×1的矩阵，则Ax=b表达了一个线性方程组，它的normal equation的形式为ATAx=ATb。



当Ax=b有解时（即矩阵[A|b]的秩与A的秩相同），Ax=b与ATAx=ATb的解集是一样。



而当Ax=b无解时，ATAx=ATb仍然有解，其解集即最小二乘解（least squares solution），即使得(Ax-b)T(Ax-b)的值最小的解，可以理解为使方程组Ax=b近似成立且误差最小的解。



皮尔森相关系数：
协方差/标准差之积



K-means
Lloyd's algorithm								
The k-means NP hard problem can solved by alternating between 2 operations:								
1)once a set of centroids μk is available, the clusters are updated 								
	to contain the points closest in distance to each centroid.							
2)Given a set of clusters, the centroids are recalculated as the means of all points belong to a cluster								
The 2-step procedure continues until the assignments of cluster and centroids no longer change.								
								
But as already mentioned, the convergence is guaranteed but the sulution might be a local minimum.								
In practice, the algorithm is rum muliple times and averaged.								
								
For starting set of centroids, several method can be employed, for instance random assignation.								
								
Lloyd's algorithm								
	D:\UserData\IT\python\paper_involved\K-means_Lloyd_algorithm.py							

