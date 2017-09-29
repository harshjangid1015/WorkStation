from math import log
import operator


def calc_entropy(dataset):
    num_vecs = len(dataset)
    # print num_vecs
    label_counts = {}
    # print label_counts
    for feat_vec in dataset:
        current_label = feat_vec[-1]
        label_counts[current_label] = \
            label_counts.get(current_label, 0) + 1
        # print feat_vec
        # print label_counts
    entropy = 0.0
    # print feat_vec
    # print feat_vec[-1]
    # print label_counts
    for label in label_counts:
        prob = float(label_counts[label]) / num_vecs
        entropy -= prob * log(prob, 2)
    return entropy



def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


mydataset, mylabels = create_dataset()
print mydataset
print mylabels

# print calc_entropy(mydataset)
calc_entropy(mydataset)


def split_dataset(dataset, feat, value):
    child_dataset = []
    for feat_vec in dataset:
        if feat_vec[feat] == value:
            reduced_feat_vec = feat_vec[:feat]
            reduced_feat_vec.extend(feat_vec[feat+1:])
            child_dataset.append(reduced_feat_vec)
            # print feat_vec
            # print reduced_feat_vec
            # print child_dataset
    return child_dataset

# print split_dataset(mydataset,0,1)
# print split_dataset(mydataset,0,0)

# print split_dataset(mydataset,0,1)
# print split_dataset(mydataset,0,0)
# # print split_dataset(mydataset,1,1)
# # print split_dataset(mydataset,1,0)


def choose_best_feat(dataset):
    num_feats = len(dataset[0]) - 1
    # print "num_feats", num_feats
    parent_entropy = calc_entropy(dataset)
    # print "parent_entropy", parent_entropy
    best_infogain = 0.0; best_feat = -1     #why these values
    for feat in range(num_feats):
        feat_vals = [feat_vec[feat] for feat_vec in dataset]
        # print "feat_vals", feat_vals
        unique_vals = set(feat_vals)
        # print "unique_vals", unique_vals
        children_entropy = 0.0
        for value in unique_vals:
            child = split_dataset(dataset, feat, value)
            # print "child", child
            prob = len(child) / float(len(dataset))
            # print "prob",prob
            # print "calc_entropy(child)", calc_entropy(child)
            children_entropy += prob * calc_entropy(child)
            # print "children_entropy", children_entropy
        infogain = parent_entropy - children_entropy
        # print "infogain", infogain
        if infogain > best_infogain:
            best_infogain = infogain
            best_feat = feat
    return best_feat

# print choose_best_feat(mydataset)
choose_best_feat(mydataset)

def majority_vote(class_labels):
    class_counts = {}
    for label in class_labels:
        class_counts[label] = class_counts.get(label, 0) + 1
    sorted_counts = sorted(class_counts.iteritems(),
                           key=operator.itemgetter(1),
                           reverse=True)
    return sorted_counts[0][0]


def create_tree(dataset, feat_labels):
    feat_labels_clone = feat_labels[:]      # clone, not change labels that might passed later to classify
    # print "feat_labels_clone", feat_labels_clone
    class_labels = [feat_vec[-1] for feat_vec in dataset]
    # print "class_labels", class_labels
    if class_labels.count(class_labels[0]) == len(class_labels):
        return class_labels[0]
    if len(dataset[0]) == 1:
        return majority_vote(class_labels)
    best_feat = choose_best_feat(dataset)
    best_feat_label = feat_labels_clone[best_feat]
    my_tree = {best_feat_label:{}}
    del(feat_labels_clone[best_feat])
    feat_vals = [feat_vec[best_feat] for feat_vec in dataset]
    unique_vals = set(feat_vals)
    for value in unique_vals:
        sub_labels = feat_labels_clone[:]
        my_tree[best_feat_label][value] = create_tree(
            split_dataset(dataset, best_feat, value), sub_labels)
    return my_tree

print create_tree(mydataset, mylabels)


def classify(input_tree, feat_labels, test_vec):
    first_str = input_tree.keys()[0]
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key],
                                       feat_labels,
                                       test_vec)
            else:
                class_label = second_dict[key]
    return class_label


