

def loadDataSet():
    return [[1,3,4],
            [2,3,5],
            [1,2,3,5],
            [2,5]]


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    ssCnt = {}
    for transaction in D:
        for candidate in Ck:
            if candidate.issubset(transaction):
                if not ssCnt.has_key(candidate): ssCnt[candidate] = 1
                else: ssCnt[candidate] += 1
    numTransactions = float(len(D))
    retList = []
    supportData = {}
    for candidate in ssCnt:
        support = ssCnt[candidate] / numTransactions
        if support >= minSupport:
            retList.append(candidate)
        supportData[candidate] = support
    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    numItemsets = len(Lk)
    for i in range(numItemsets):
        for j in range(i+1, numItemsets):
            itemset1 = list(Lk[i])[:k-2]
            itemset2 = list(Lk[j])[:k-2]
            itemset1.sort(); itemset2.sort()
            if itemset1 == itemset2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while len(L[k-2]) > 0:
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


def generateRules(L, suppData,minConf = .7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, suppData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, suppData, bigRuleList, minConf)
    return bigRuleList

def calcConf(freqSet, H, suppData, brl,minConf = .7):
    prunedH = []
    for conseq in H:
        conf = suppData[freqSet]/suppData[freqSet-conseq]
        if conf >= minConf:
            print freqSet-conseq, '-->', conseq, 'conf:', conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, suppData, brl, minConf = .7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, suppData, brl, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, suppData, brl, minConf)

def loadBakeryDataSet(filename):
    D = []
    fr = open(filename, 'r')
    for transaction in fr.readlines():
        transaction = transaction.strip()
        transaction = transaction.split(', ')[1:]     # discard tid
        D.append(transaction)
    return [set(transaction) for transaction in D]



