from collections import Counter
import numpy as np
import operator
from os import listdir

# Step-2 define a function load_data(filename) that loads data from the specified input file, and
# returns a numpy 2d array X, and a numpy vector Y.
def load_data(filename):
    input_file = open(filename)
    lines = input_file.readlines()
    data_matrix = np.zeros((len(lines), 8))
    labels = []
    index = 0
    for line in lines:
        line = line.strip()
        tokens = line.split(',')
        data_matrix[index, :] = tokens[:8]
        labels.append(int(tokens[-1]))
        index += 1
    return data_matrix, labels

X, Y = load_data('pima-indians-diabetes-train.data')


# define a function normalize(X) that normalizes the data matrix X, and
# returns X normalized, column ranges, and column min_values.
def normalize(X):
    min_values = X.min(axis=0)
    max_vals = X.max(axis=0)
    column_ranges = max_vals - min_values
    nrows = X.shape[0]
    norm_data_matrix_X = X - np.tile(min_values, (nrows, 1))
    norm_data_matrix_X = norm_data_matrix_X / np.tile(column_ranges, (nrows, 1))
    return norm_data_matrix_X, column_ranges, min_values

# print normalize(X)
# Step-4
# define a function classify_kNN(test_x, X, Y, k) that uses the training data matrix X,
# and labels Y, to find the class label of the test sample test_x, using k neighbors.

# print X.shape[0]


def classify_kNN(test_x, X, Y, k):
    dataset_size = X.shape[0]
    #print dataset_size
    diff_matrix = np.tile(test_x, (dataset_size, 1)) - X
    sq_diff_matrix = diff_matrix**2
    sq_distances = sq_diff_matrix.sum(axis=1)
    distances = sq_distances**0.5
    sorted_distances_indices = distances.argsort()
    label_counts = {}
    for i in range(k):
        neighbor_label = Y[sorted_distances_indices[i]]
        label_counts[neighbor_label] = \
            label_counts.get(neighbor_label, 0) + 1
    sorted_label_counts = sorted(label_counts.iteritems(),
                                 key=operator.itemgetter(1),
                                 reverse=True)
    return sorted_label_counts[0][0]

# print "classify_kNN([6,148,72,35,0,33.6,0.627,50], X, Y, k=7) is", classify_kNN([6,148,72,35,0,33.6,0.627,50], X, Y, 7)
norm_x,col_range, min_val = normalize(X)


"""
define the function test_kNN(train_X, train_Y, test_X, test_Y, k) that accepts training data matrix, training data labels, test data matrix, test data labels, and # of neighbors k, and
prints the error rate on the test dataset. The output should be like the following:
(k, error_count, |test|, error_rate): (6, 44, 150, 0.293333)
"""

# train_X, train_Y = load_data('pima-indians-diabetes-train.data')
# test_X, test_Y = load_data('pima-indians-diabetes-test.data')



def test_kNN(train_X, train_Y, test_X, test_Y, k):
    norm_data_matrix, ranges, min_vals = normalize(train_X)
    dataset_size = test_X.shape[0]
    test_dataset_size = int(dataset_size)
    error_count = 0.0
    for i in range(test_dataset_size):
        guess = classify_kNN(test_X[i, :],
                          train_X[test_dataset_size:, :],
                             train_Y[test_dataset_size:], k)
        # print 'the classifier came back with: %d, the real answer is: %d' \
        #       % (guess, train_Y[i])
        if (guess != test_Y[i]):
            error_count += 1
    print '(k, error_count, |test|, error_rate): (%d, %d, %d, %f)' \
                  % (k, error_count, test_X.shape[0], (error_count / test_X.shape[0]))

# print "test_kNN(train_X, train_Y, test_X, test_Y, k)", test_kNN(train_X, train_Y, test_X, test_Y, k=7)

# 6.1 call load_data() on training_file.data (the filename specified by user)
load_data('pima-indians-diabetes-train.data')
train_X, train_Y = load_data('pima-indians-diabetes-train.data')

# 6.2 call load_data() on test_file.data (filename specified by user)
load_data('pima-indians-diabetes-test.data')
test_X, test_Y = load_data('pima-indians-diabetes-test.data')

# 6.3 call normalize() on training matrix returned by 6.1
normalize(train_X)
normalized_train_X, column_ranges_train, min_values_train = normalize(train_X)

# 6.4 normalize the test matrix returned by 6.2 using min_vals and ranges from 6.3
normalize(test_X)
normalized_test_X, column_ranges_test, min_values_test = normalize(test_X)

# 6.5 Given K, run a loop for k = 1 to K, for each k call test_kNN(normalized_train_X, train_Y, normalized_test_X, test_Y, k).
# Assuming that K = 10
for k in range(1,11):
    test_kNN(normalized_train_X, train_Y, normalized_test_X, test_Y, k)
