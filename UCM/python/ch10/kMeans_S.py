import numpy as np


def load_data(filename):
    X = []
    fr = open(filename)
    for line in fr.readlines():
        toks = line.strip().split('\t')
        tok_values = map(float, toks)
        X.append(tok_values)
    return np.array(X)

def dist_Euclidean(vec_a, vec_b):
    return np.sqrt(
        np.sum(
            np.power(vec_a - vec_b, 2)
        )
    )


def rand_cent(X, k):
    n = X.shape[1]
    centroids = np.zeros((k, n))
    for j in range(n):
        min_j = np.min(X[:, j])
        range_j = float(np.max(X[:, j]) - min_j)
        centroids[:, j] = min_j + range_j * np.random.rand(k)
    return centroids


def kMeans(X, k, dist_fun=dist_Euclidean, create_cent=rand_cent):
    m = X.shape[0]
    cluster_assignment = np.mat(np.zeros((m, 2)))
    centroids = create_cent(X, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = np.inf; min_index = -1
            for j in range(k):
                dist_ij = dist_fun(centroids[j, :], X[i, :])
                if dist_ij < min_dist:
                    min_dist = dist_ij; min_index = j
            if cluster_assignment[i, 0] != min_index:
                cluster_changed = True
            cluster_assignment[i, :] = min_index, min_dist**2
        print centroids
        for cent in range(k):
            members = X[
                np.nonzero(cluster_assignment[:, 0].A == cent)[0]]
            centroids[cent, :] = np.mean(members, axis=0)
    return centroids, cluster_assignment


def kMeansN(X, k):
    m = X.shape[0]
    clustering = np.zeros((m, 2))
    C = rand_cent(X, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = np.inf; min_index = -1
            for j in range(k):
                dist_ij = dist_Euclidean(C[j,:], X[i,:])
                if dist_ij < min_dist:
                    min_dist = dist_ij; min_index = j
            if clustering[i,0] != min_index: cluster_changed = True
            clustering[i,:] = min_index, min_dist**2
        print C
        for j in range(k):
            clust_j = X[clustering[:,0] == j, :]
            C[j,:] = clust_j.mean(axis=0)
    return C, clustering


def biKmeans(X, k):
    m = X.shape[0]
    clustering = np.zeros((m, 2))
    c0 = X.mean(axis=0)
    cent_list = [c0]
    for i in range(m):
        clustering[i,1] = dist_Euclidean(c0, X[i,:])**2
    while len(cent_list) < k:
        lowestSSE = np.inf
        for j in range(len(cent_list)):
            clust_j = X[clustering[:,0] == j, :]
            splitCentroids, splitClustering = kMeansN(clust_j, 2)
            splitSSE = sum(splitClustering[:,1])
            notSplitSSE = sum(clustering[clustering[:,0] != j, 1])
            print 'sseSplit, and sseNotSplit:', splitSSE, notSplitSSE
            if (splitSSE + notSplitSSE) < lowestSSE:
                best_clust_to_split = j
                best_new_cent = splitCentroids
                bestSplitClustering = splitClustering.copy()
                lowestSSE = splitSSE + notSplitSSE
        bestSplitClustering[bestSplitClustering[:,0] == 1, 0] = len(cent_list)
        bestSplitClustering[bestSplitClustering[:,0] == 0, 0] = best_clust_to_split
        print 'the best cluster to split is:', best_clust_to_split
        print 'the len of bestSplitClustering is:', len(bestSplitClustering)
        cent_list[best_clust_to_split] = splitCentroids[0,:]
        cent_list.append(splitCentroids[1,:])
        clustering[clustering[:,0] == best_clust_to_split,:] = bestSplitClustering
    return np.array(cent_list), clustering


