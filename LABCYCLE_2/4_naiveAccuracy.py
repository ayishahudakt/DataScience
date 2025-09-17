import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#load the iris dataset
iris=datasets.load_iris()
X=iris.data
y=iris.target
#split the data into training and testing sets(80% training,20% testing)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#create a Gaussian Naive Bayes classifier
nb_classifier=GaussianNB()

#Train the classifier using the train data
nb_classifier.fit(X_train,y_train)

#make predictions on the testing data
y_pred=nb_classifier.predict(X_test)

#calculate the accuracy of the classifier
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
