import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()

X = iris.data
y = iris.target

#split dataset into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


def entropy(counts, n_samples):
    """
    Parameters:
    -----------
    counts: shape (n_classes): list number of samples in each class
    n_samples: number of data samples

    -----------
    return entropy
    """
    # Convert counts to a NumPy array
    counts_array = np.array(counts)

    # Calculate entropy using the counts of each class
    probabilities = counts_array / n_samples
    adding = 1e-10
    entropy_value = -np.sum(probabilities * np.log2(probabilities + 1e-10))  # Adding a small constant to avoid log(0)
    return entropy_value


def entropy_of_one_division(division):
    """
    Returns entropy of a divided group of data
    Data may have multiple classes
    """
    n_samples = len(division)
    n_classes = list(set(division))  # Convert set to list

    counts = [np.sum(division == c) for c in n_classes]  # Count samples in each class
    return entropy(counts, n_samples), n_samples



def get_entropy(y_predict, y):
    """
    Returns entropy of a split
    y_predict is the split decision by cutoff, True/Fasle
    """
    n = len(y)
    entropy_true, n_true = entropy_of_one_division(y[y_predict]) # left hand side entropy
    entropy_false, n_false = entropy_of_one_division(y[~y_predict]) # right hand side entropy
    # overall entropy
    s = (n_true / n) * entropy_true + (n_false / n) * entropy_false
    return s

class DecisionTreeClassifier:
    def __init__(self, tree=None, depth=0):
        '''Parameters:
        -----------------
        tree: decision tree
        depth: depth of decision tree after training'''

        self.depth = depth
        self.tree=tree
    def fit(self, X, y, node={}, depth=0):
        '''Parameter:
        -----------------
        X: training data
        y: label of training data
        ------------------
        return: node

        node: each node represented by cutoff value and column index, value and children.
         - cutoff value is thresold where you divide your attribute
         - column index is your data attribute index
         - value of node is mean value of label indexes,
           if a node is leaf all data samples will have same label

        Note that: we divide each attribute into 2 part => each node will have 2 children: left, right.
        '''

        #Stop conditions

        #if all value of y are the same
        if np.all(y==y[0]):
            return {'val':y[0]}

        else:
            col_idx, cutoff, entropy = self.find_best_split_of_all(X, y)    # find one split given an information gain
            y_left = y[X[:, col_idx] < cutoff]
            y_right = y[X[:, col_idx] >= cutoff]
            node = {'index_col':col_idx,
                        'cutoff':cutoff,
                   'val':np.mean(y)}
            X_col_left = X[X[:, col_idx] < cutoff]
            x_col_right = X[X[:, col_idx] >= cutoff]
            node['left'] = self.fit(X[X[:, col_idx] < cutoff], y_left, {}, depth+1)
            node['right'] = self.fit(X[X[:, col_idx] >= cutoff], y_right, {}, depth+1)
            self.depth += 1
            self.tree = node
            return node

    def find_best_split_of_all(self, X, y):
        col_idx = None
        min_entropy = 1
        cutoff = None
        XT_value = X.T
        for i, col_data in enumerate(X.T):
            entropy, cur_cutoff = self.find_best_split(col_data, y)
            if entropy == 0:                   #best entropy
                return i, cur_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                col_idx = i
                cutoff = cur_cutoff

        return col_idx, cutoff, min_entropy

    def find_best_split(self, col_data, y):
        ''' Parameters:
        -------------
        col_data: data samples in column'''

        min_entropy = 10
        cutoff = None
        # Loop through col_data to find cutoff where entropy is minimum
        for value in set(col_data):     #find all dinstict values of an attribute
            y_predict = col_data < value        #set the output of y based on the cutoff value
            my_entropy = get_entropy(y_predict, y)      #calculate the entropy of the cutoff value

            if my_entropy < min_entropy:
                min_entropy = my_entropy                #update the smallest entropy
                cutoff = value                          #update the cut off value

        return min_entropy, cutoff

    def predict(self, X):
        tree = self.tree
        pred = np.zeros(shape=len(X))
        for i, c in enumerate(X):
            pred[i] = self._predict(c)
        return pred

    def _predict(self, row):
        cur_layer = self.tree
        while cur_layer.get('cutoff'):
            if row[cur_layer['index_col']] < cur_layer['cutoff']:
                cur_layer = cur_layer['left']
            else:
                cur_layer = cur_layer['right']
        else:
            return cur_layer.get('val')


model = DecisionTreeClassifier()
tree = model.fit(X_train, y_train)
pred=model.predict(X_train)
print('Accuracy of your decision tree model on training data:', accuracy_score(y_train,pred))
pred=model.predict(X_test)
print('Accuracy of your decision tree model:', accuracy_score(y_test,pred))