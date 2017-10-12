import numpy as np
import matplotlib.pyplot as plt
 
def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
 
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X,K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)


import random
 
def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X


def init_board_gauss(N, k):
    n = float(N)/k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05,0.5)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) < 1 and abs(b) < 1:
                x.append([a,b])
        X.extend(x)
    X = np.array(X)[:N]
    return X

def main():
    K=7
    N=1000
    #X=init_board(N)
    X=init_board_gauss(1000,9)
    mu, clusters = find_centers(X,K)
    print("type(mu)",type(mu))
    print("type(clusters)",type(clusters))
    print("mu:",mu)
    #print("clusters:",clusters)

    cmap=plt.cm.get_cmap("rainbow")
    for i in range(0,len(mu)):
        c=cmap(float(i)/len(mu))
        print(c)
        plt.scatter(mu[i][0],mu[i][1],marker='H', s=200,c=c)

        j=len(clusters[i])
        print("cluster:",i,"len:",j)
        acluster=clusters[i]
        acluster=np.reshape(acluster,[-1,2])
        #print("type(acluster):",type(acluster))
        #print(acluster)
        #print("acluster[:j][0]",acluster[:,0])
        plt.scatter(acluster[:,0],acluster[:,1],marker='o', s=8,c=c)

        
    plt.show()

main()

