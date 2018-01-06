import numpy as np
import operator

def  createDataSet():
    group = [[1.0, 1.1],
             [1.0, 1.0],
             [0, 0],
             [0, 0.1]]
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteILabel = labels[sortedDistIndices[i]]
        classCount[voteILabel] =\
            classCount.get(voteILabel, 0) + 1
    sortedClassCount = sorted(
        classCount.iteritems(),
        key=operator.itemgetter(1),
        reverse=True
    )
    return sortedClassCount[0][0]

def classify1(x, X, Y, k):
    n = X.shape[0]
    dist = ((np.tile(x, (n, 1)) - X)**2).sum(axis=1)**0.5
    sorting_dist = dist.argsort()
    """
    counts = {}
    for i in range(k):
        neigbor_lbl = Y[sorting_dist[i]]
        counts[neigbor_lbl] = counts.get(neigbor_lbl, 0) + 1
    sorted_counts = sorted(counts.iteritems(),
                           key=operator.itemgetter(1),
                           reverse=True)
    return sorted_counts[0][0]
    """
    from collections import Counter
    neigbor_counts = Counter(list(Y[sorting_dist[0:k]]))
    return neigbor_counts.most_common(1)[0][0]

def file2matrix(filename):
    fr = open(filename)
    lines = fr.readlines()
    ret_X = np.zeros((len(lines), 3))
    ret_Y = []
    index = 0
    for line in lines:
        tokens = line.strip().split('\t')
        ret_X[index, :] = tokens[0:3]
        ret_Y.append(int(tokens[-1]))
        index += 1
    return ret_X, ret_Y

def autoNorm(X):
    min_v = X.min(axis=0)
    max_v = X.max(axis=0)
    ranges = max_v - min_v
    norm_X = np.zeros(X.shape)
    m = X.shape[0]
    norm_X = X - np.tile(min_v, (m, 1))
    norm_X = norm_X / np.tile(ranges, (m, 1))
    return norm_X, ranges, min_v

def datingCalssTest():
    ratio = 0.1
    dX, dY = file2matrix('datingTestSet2.txt')
    norm_dX, ranges, min_v = autoNorm(dX)
    m = norm_dX.shape[0]
    m_test = int(m * ratio)
    error_count = 0.0
    for i in range(m_test):
        guess = classify0(norm_dX[i, :],
                          norm_dX[m_test:m],
                          dY[m_test:m], 3)
        print "the classfier came back with: %d, the real answer is: %d" \
              % (guess, dY[i])
        if (guess != dY[i]): error_count += 1.0
    print "the total error rate is: %f" % (error_count/m_test)