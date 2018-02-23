from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import operator


def create_dataset():
    group = np.array(
        [[1.0, 1.1],
         [1.0, 1.0],
         [0, 0],
         [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_matrix, labels, k):
    dataset_size = data_matrix.shape[0]
    diff_matrix = np.tile(in_x, (dataset_size, 1)) - data_matrix
    sq_diff_matrix = diff_matrix**2
    sq_distances = sq_diff_matrix.sum(axis=1)
    distances = sq_distances**0.5
    sorted_distances_indices = distances.argsort()
    label_counts = {}
    for i in range(k):
        neighbor_label = labels[sorted_distances_indices[i]]
        label_counts[neighbor_label] = \
            label_counts.get(neighbor_label, 0) + 1
    sorted_label_counts = sorted(label_counts.iteritems(),
                                 key=operator.itemgetter(1),
                                 reverse=True)
    return sorted_label_counts[0][0]


def classify1(in_x, data_matrix, labels, k):
    dataset_size = data_matrix.shape[0]
    distances = \
        ((np.tile(in_x, (dataset_size, 1)) - data_matrix)**2).sum(axis=1)**0.5
    sorted_distances_indices = distances.argsort()
    knn_labels = \
        [labels[neighbor_index] for neighbor_index in sorted_distances_indices[0:k]]
    knn_label_counts = Counter(knn_labels)
    return knn_label_counts.most_common(1)[0][0]


def file2matrix(filename):
    """
    Parse dating-site data into a data matrix and a list of class labels
    :param filename:
    :return: data_matrix and labels
    """
    input_file = open(filename)
    lines = input_file.readlines()
    data_matrix = np.zeros((len(lines), 3))
    labels = []
    index = 0
    for line in lines:
        line = line.strip()
        tokens = line.split('\t')
        data_matrix[index, :] = tokens[:3]
        labels.append(int(tokens[-1]))
        index += 1
    return data_matrix, labels


def auto_norm(data_matrix):
    min_vals = data_matrix.min(axis=0)
    max_vals = data_matrix.max(axis=0)
    ranges = max_vals - min_vals
    nrows = data_matrix.shape[0]
    norm_data_matrix = data_matrix - np.tile(min_vals, (nrows, 1))
    norm_data_matrix = norm_data_matrix / np.tile(ranges, (nrows, 1))
    return norm_data_matrix, ranges, min_vals


def dating_knn_test(dating_data_matrix, dating_labels):
    test_ratio = 0.10
    norm_data_matrix, ranges, min_vals = auto_norm(dating_data_matrix)
    dataset_size = dating_data_matrix.shape[0]
    test_dataset_size = int(dataset_size * test_ratio)
    error_count = 0.0
    for i in range(test_dataset_size):
        guess = classify0(norm_data_matrix[i, :],
                          norm_data_matrix[test_dataset_size:, :],
                          dating_labels[test_dataset_size:], 3)
        print 'the classifier came back with: %d, the real answer is: %d' \
              % (guess, dating_labels[i])
        if (guess != dating_labels[i]):
            error_count += 1
    print 'the total error rate is: %f' % (error_count / test_dataset_size)


def main():
    X, Y = create_dataset()
    print "classify0([0, 0], k=3) is", classify0([0, 0], X, Y, 3)
    print "classify1([0, 0], k=3) is", classify1([0, 0], X, Y, 3)

    dating_data_matrix, dating_labels = file2matrix('datingTestSet2.txt')
    fig, axarr = plt.subplots(1, 2, sharey=True)
    axarr[0].scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2])
    axarr[0].set_ylabel('Liters of Ice Cream Consumed Per Week')
    axarr[0].set_xlabel('Time Spent Playing Video Games')
    np_dating_labels = np.array(dating_labels)
    axarr[1].scatter(dating_data_matrix[:, 1],
                     dating_data_matrix[:, 2],
                     15.0 * np_dating_labels,
                     15.0 * np_dating_labels)
    axarr[1].set_xlabel('Time Spent Playing Video Games')
    plt.show()
    dating_knn_test(dating_data_matrix, dating_labels)


main()
