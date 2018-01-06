import numpy as np


def create_dataset():
    postings = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'stop', 'him'],
                ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_labels = [0, 1, 0, 1, 0, 1]
    return postings, class_labels


def create_vocab(dataset):
    vocab = set([])
    for document in dataset:
        vocab = vocab | set(document)
    return list(vocab)


def setofwords_2vec(vocab, inputset):
    ret_vec = [0] * len(vocab)
    for word in inputset:
        if word in vocab:
            ret_vec[vocab.index(word)] = 1
        else:
            print 'the word: $s is not in my vocabulary' % word
    return ret_vec


def trainNB0(training_matrix, training_labels):
    size_train = len(training_matrix)
    num_words = len(training_matrix[0])
    pAbusive = sum(training_labels) / float(size_train)
    p0Num = np.ones(num_words); p1Num = np.ones(num_words)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(size_train):
        if training_labels[i] == 1:
            p1Num += training_matrix[i]
            p1Denom += sum(training_matrix[i])
        else:
            p0Num += training_matrix[i]
            p0Denom += sum(training_matrix[i])
    p1Vect = np.log(p1Num / p1Denom)
    p0Vect = np.log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(new_vec, p0v, p1v, pClass1):
    p1 = sum(new_vec * p1v) + np.log(pClass1)
    p0 = sum(new_vec * p0v) + np.log(1 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testing_nb():
    dataset, labels = create_dataset()
    vocab_list = create_vocab(dataset)
    train_mat = []
    for doc in dataset:
        train_mat.append(setofwords_2vec(vocab_list, doc))
    p0v, p1v, pAb = trainNB0(np.array(train_mat), np.array(labels))
    test_doc = ['love', 'my', 'dalmation']
    test_vec = np.array(setofwords_2vec(vocab_list, test_doc))
    print test_doc, 'classified as:', classifyNB(test_vec, p0v, p1v, pAb)
    test_doc = ['stupid', 'garbage']
    test_vec = np.array(setofwords_2vec(vocab_list, test_doc))
    print test_doc, 'classified as:', classifyNB(test_vec, p0v, p1v, pAb)


def text_parse(big_string):
    import re
    tokens = re.split(r'\W*', big_string)
    return [token.lower() for token in tokens if len(token) > 2]


def spam_test():
    doc_list = []; class_list = []; full_text = []
    for i in range(1, 26):
        word_list = text_parse(open('email/spam/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)
        word_list = text_parse(open('email/ham/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)
    vocab_list = create_vocab(doc_list)
    training_set = range(50); test_set = []
    for i in range(10):
        rand_index = int(np.random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
    training_mat = []; training_classes = []
    for doc_index in training_set:
        training_mat.append(setofwords_2vec(vocab_list, doc_list[doc_index]))
        training_classes.append(class_list[doc_index])
    p0v, p1v, pSpam = trainNB0(np.array(training_mat), np.array(training_classes))
    error_count = 0.0
    for doc_index in test_set:
        word_vec = setofwords_2vec(vocab_list, doc_list[doc_index])
        if classifyNB(np.array(word_vec), p0v, p1v, pSpam) != class_list[doc_index]:
            error_count += 1
    print 'the error rate is:', float(error_count) / len(test_set)