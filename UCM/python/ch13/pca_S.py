import numpy as np


def loadDataSet(filename, delim='\t'):
    fr = open(filename)
    strArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [map(float, line) for line in strArr]
    return np.array(datArr)


def pca(dataMat, topNfeat=999999):
    meanVals = dataMat.mean(axis=0)
    meanRemoved = dataMat - meanVals
    covMat = np.cov(meanRemoved, rowvar=0)
    eigVals, eigVects = np.linalg.eig(covMat)
    eigValInds = np.argsort(eigVals)
    eigValInds = eigValInds[:-(topNfeat+1):-1]
    redEigVects = eigVects[:,eigValInds]
    lowDDataMat = np.dot(meanRemoved, redEigVects)
    reconMat = np.dot(lowDDataMat, redEigVects.T) + meanVals
    return lowDDataMat, reconMat


def replaceNanWithMean():
    dataMat = loadDataSet('secom.data', ' ')
    numFeat = dataMat.shape[1]
    for i in range(numFeat):
        meanVal = np.mean(dataMat[~np.isnan(dataMat[:,i]), i])
        dataMat[np.isnan(dataMat[:, i]), i] = meanVal
    return dataMat
