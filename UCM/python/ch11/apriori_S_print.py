

def loadDataSet():
    return [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]

dataSet = loadDataSet()
# print "dataSet:", dataSet

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        # print "transaction:",transaction
        for item in transaction:
            # print "item:",item
            if not[item] in C1:
                # if item not in C1: not giving unique result---idk
                C1.append([item])
                # print "C1:",C1
    C1.sort()
    # print "C1 sorted:",C1
    return map(frozenset, C1)

# C1 = createC1(dataSet)
# print "C1:",C1
#
# D = map(set, dataSet)
# print "D:", D

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for transaction in D:
        # print "transaction:",transaction
        for candidate in Ck:
            if candidate.issubset(transaction):
                if not ssCnt.has_key(candidate): ssCnt[candidate] = 1
                else: ssCnt[candidate] += 1
    # print "ssCnt:", ssCnt
    numTransactions = float(len(D))
    retList = []
    supportData = {}
    for candidate in ssCnt:
        support = ssCnt[candidate] / numTransactions
        if support >= minSupport:
            retList.append(candidate)
        supportData[candidate] = support
    return retList, supportData

# # scanD(D, C1, 0.5)
# retList, supportData = scanD(D, C1, 0.5)
# print "retList:",retList
# print "supportData:", supportData

def aprioriGen(Lk, k):
    retList = []
    numItemsets = len(Lk)
    # print "numItemsets: ",numItemsets
    for i in range(numItemsets):
        for j in range(i+1, numItemsets):
            itemset1 = list(Lk[i])[:k-2]
            # print "itemset1:", itemset1
            itemset2 = list(Lk[j])[:k-2]
            # print "itemset2:", itemset2
            itemset1.sort(); itemset2.sort()
            if itemset1 == itemset2:
                retList.append(Lk[i] | Lk[j])
    return retList

# aprioriGen(retList, 2)
# retList2 = aprioriGen(retList, 2)
# # print "retList2:", retList2

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    print "C1:", C1
    D = map(set, dataSet)
    print "D:", D
    L1, supportData = scanD(D, C1, minSupport)
    print "L1:", L1
    L = [L1]
    print "L:", L
    k = 2
    # print len(L)
    while len(L[k-2]) > 0:
        # print k-2
        # print len(L[k-2])
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

L, supportData =apriori(dataSet, minSupport=0.5)
print "L:", L
print "supportData:", supportData