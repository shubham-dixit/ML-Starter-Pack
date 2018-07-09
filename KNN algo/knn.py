# K-Nearest Neighbours (K-NN)
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/arindam/Desktop/KNN algo/Iris.csv')
X = dataset.iloc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]].values
y = dataset.iloc[:,("Species")].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Fitting KNN to training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric= 'minkowski', p =2)
classifier.fit(X_train, y_train)
#Predicting the test results
y_pred = classifier.predict(X_test)

#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#Visualising the Training Set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train 
X1, X2= np.meshgrid(np.arange(start= X_set[:, 0].min()-1, stop= X_set[:,0].max()+1, step= 0.01),
                    np.arange(start= X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step= 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0],X_set[y_set==j, 1], c= ListedColormap(('red','green'))(i),label=j)
plt.title('Classifier')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()    

#Visualising the Test Set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test 
X1, X2= np.meshgrid(np.arange(start= X_set[:, 0].min()-1, stop= X_set[:,0].max()+1, step= 0.01),
                    np.arange(start= X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step= 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0],X_set[y_set==j, 1], c= ListedColormap(('red','green'))(i),label=j)
plt.title('Classifier')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()   
