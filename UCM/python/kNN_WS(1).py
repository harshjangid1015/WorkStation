from collections import Counter
import numpy as np
import operator
from os import listdir


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


def dating_classify_person(dating_data_matrix, dating_labels):
    class_txt_labels = ['not at all', 'in small doses', 'in large doses']
    video_games = \
        float(raw_input('percentage of time playing video games? '))
    ff_miles  = \
        float(raw_input('frequent flyer miles earned per year? '))
    ice_cream = \
        float(raw_input('liters of ice cream consumed per year? '))
    norm_data_matrix, ranges, min_vals = auto_norm(dating_data_matrix)
    candidate_date = np.array([ff_miles, video_games, ice_cream])
    knn_recommendation = classify0((candidate_date - min_vals) / ranges,
                                   norm_data_matrix, dating_labels, 3)
    print 'You will probably like this person:', \
        class_txt_labels[knn_recommendation - 1]


def img2vector(filename):
    img_vector = np.zeros((1, 1024))
    input_file = open(filename)
    for i in range(32):
        line = input_file.readline().strip()
        for j in range(32):
            img_vector[0, 32 * i + j] = int(line[j])
    return img_vector


def mnist_knn_test():
    """
    Handwritten digit dataset
    :return:
    """
    hw_labels = []
    training_file_list = listdir('trainingDigits')
    n_training_files = len(training_file_list)
    data_matrix = np.zeros((n_training_files, 1024))
    for i in range(n_training_files):
        filename = training_file_list[i]
        filename_base = filename.split('.')[0]
        hw_digit_label = int(filename_base.split('_')[0])
        hw_labels.append(hw_digit_label)
        data_matrix[i, :] = img2vector('trainingDigits/%s' % filename)
    test_file_list = listdir('testDigits')
    error_count = 0.0
    n_test_files = len(test_file_list)
    for i in range(n_test_files):
        filename = test_file_list[i]
        filename_base = filename.split('.')[0]
        test_digit_label = int(filename_base.split('_')[0])
        test_vector = img2vector('testDigits/%s' % filename)
        guessed_digit_label = classify0(test_vector,
                                        data_matrix,
                                        hw_labels, 3)
        print 'the classifier came back with: %d, the real answer is: %d' \
              % (guessed_digit_label, test_digit_label)
        if (guessed_digit_label != test_digit_label):
            error_count += 1
    print '\nthe total number of errors is: %d' % error_count
    print '\nthe total error rate is: %f' % (error_count / n_test_files)


def main():
    X, Y = create_dataset()
    print "classify0([0, 0], k=3) is", classify0([0, 0], X, Y, 3)
    print "classify1([0, 0], k=3) is", classify1([0, 0], X, Y, 3)

    dating_data_matrix, dating_labels = file2matrix('datingTestSet2.txt')
    import matplotlib.pyplot as plt
    fig, axarr = plt.subplots(1, 2, sharey=True)
    axarr[0].scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2])
    axarr[0].set_ylabel('Liters of Ice Cream Consumed Per Week')
    axarr[0].set_xlabel('Percentage of Time Spent Playing Video Games')
    np_dating_labels = np.array(dating_labels)
    axarr[1].scatter(dating_data_matrix[:, 1],
                     dating_data_matrix[:, 2],
                     15.0 * np_dating_labels,
                     15.0 * np_dating_labels)
    axarr[1].set_xlabel('Percentage of Time Spent Playing Video Games')
    plt.show()
    dating_knn_test(dating_data_matrix, dating_labels)

    # input: 10, 10000, 0.5, output: small doses
    dating_classify_person(dating_data_matrix, dating_labels)


main()