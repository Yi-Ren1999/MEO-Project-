import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor, plot_tree
from sklearn import preprocessing




if __name__=='__main__':
    DATASET='test_dataset.npz'


    dataset=np.load(DATASET)
    description=dataset['description']
    label=dataset['label']


    le_description=preprocessing.LabelEncoder()
    description=le_description.fit_transform(description)
    
    le_label=preprocessing.LabelEncoder()
    label=le_label.fit_transform(label)

    print(description.shape,label.shape)
    dt=DecisionTreeClassifier().fit(description.reshape(-1,1),label)

    plot_tree(dt,filled=True)
    plt.show()
