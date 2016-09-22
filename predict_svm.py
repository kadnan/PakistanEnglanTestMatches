"""
    Labels : Lost, Draw, Won [-1,0,1]
    Features
    ==========
        Toss(Lost,Won) = [-1,1]
        Bat(First, Second) = [-1,1]
"""
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support as score

# Assigning Features
features = np.genfromtxt('train.csv',delimiter=',',usecols=(1,2),dtype=int)
labels = np.genfromtxt('train.csv',delimiter=',',usecols=(0),dtype=int)

features_test = np.genfromtxt('test.csv',delimiter=',',usecols=(1,2),dtype=int)
labels_test = np.genfromtxt('test.csv',delimiter=',',usecols=(0),dtype=int)

# Create a SVM Classifier
model = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
            decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
            max_iter=-1, probability=True, random_state=None, shrinking=True,
            tol=0.001, verbose=False
            )
#
# # Train the model using the training sets
model.fit(features, labels)
#print(model.get_params())
#
# # Predict Output
predicted = model.predict(features_test)
# print(predicted)
acc = accuracy_score(labels_test,predicted)
print(acc)

#precision, recall, fscore, support = score(labels_test, predicted)
# print('precision: {}'.format(precision))
# print('recall: {}'.format(recall))
# print('fscore: {}'.format(fscore))
# print('support: {}'.format(support))