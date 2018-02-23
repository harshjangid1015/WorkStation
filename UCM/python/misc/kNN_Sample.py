from numpy import *
import operator

group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
labels = ['A', 'A', 'B', 'B']

def createDataSet():
    # print group
    # print labels
    return group, labels

createDataSet()


# def classify0(inX, dataSet, labels, k):
#     dataSetSize = dataSet.shape[0]
#     diffMat = tile(inX, (dataSetSize,1)) - dataSet
#     sqDiffMat = diffMat**2
#     sqDistances = sqDiffMat.sum(axis=1)
#     distances = sqDistances**0.5
#     sortedDistIndicies = distances.argsort()
#     classCount={}
#     for i in range(k):
#         voteIlabel = labels[sortedDistIndicies[i]]
#         classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
#     sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
#     print "Return of sortedClassCount : "+ sortedClassCount[0][0]
#     return sortedClassCount[0][0]
#
# classify0([0,0], group, labels, 3)


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
      #  print "forloopke andar voteIlabel" + voteIlabel
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

classify0([0,0], group, labels, 3)


def file2matrix(datingTestSet):
    fr = open(datingTestSet)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(datingTestSet)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append((listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

# print file2matrix('C:\Workstation\UCM\python\datingTestSet.txt')
datingDataMat,datingLabels = file2matrix('C:\Workstation\UCM\python\datingTestSet.txt')
#print datingDataMat
#print datingLabels
print datingLabels[0:20]


import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
#plt.show()
ax.scatter(datingDataMat[:,1], datingDataMat[:,2] , 15.0*array(datingLabels) , 15.0*array(datingLabels))
plt.show()