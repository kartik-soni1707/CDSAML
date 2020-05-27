#Importing headers
from nltk.corpus import stopwords,words
import numpy as np
import pandas as pd
import nltk
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB,GaussianNB
dataset=pd.read_csv("1-5000.csv")
dataset=dataset.iloc[:,1:3]
df=dataset
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(df.iloc[:,0].values)
targets=df.iloc[:,1].values
classifier=MultinomialNB()
classifier.fit(counts,targets)

cv=CountVectorizer(max_features=3000)
x=cv.fit_transform(df.iloc[:,0].values).toarray()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(targets)   

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)
pred=classifier.predict(X_test)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
print('Accuracy score: {}'.format(accuracy_score(y_test, pred)))
print('Precision score: {}'.format(precision_score(y_test, pred)))
print('Recall score: {}'.format(recall_score(y_test, pred)))
print('F1 score: {}'.format(f1_score(y_test, pred)))
from sklearn.ensemble import RandomForestClassifier#Importing headers
from nltk.corpus import stopwords,words
import numpy as np
import pandas as pd
import nltk
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB,GaussianNB
dataset=pd.read_csv("1-5000.csv")
dataset=dataset.iloc[:,1:3]
df=dataset
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(df.iloc[:,0].values)
targets=df.iloc[:,1].values
classifier=MultinomialNB()
classifier.fit(counts,targets)

cv=CountVectorizer(max_features=3000)
x=cv.fit_transform(df.iloc[:,0].values).toarray()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(targets)   

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
#Random forest
from sklearn.ensemble import RandomForestClassifier
classifier1=RandomForestClassifier(n_estimators=15,criterion='entropy')
classifier1.fit(X_train,y_train)
predRF=classifier1.predict(X_test)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
print('Accuracy score: {}'.format(accuracy_score(y_test, predRF)))
print('Precision score: {}'.format(precision_score(y_test, predRF)))
print('Recall score: {}'.format(recall_score(y_test, predRF)))
print('F1 score: {}'.format(f1_score(y_test, predRF)))

classifier1=RandomForestClassifier(n_estimators=15,criterion='entropy')
classifier1.fit(X_train,y_train)
predRF=classifier1.predict(X_test)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
print('Accuracy score: {}'.format(accuracy_score(y_test, predRF)))
print('Precision score: {}'.format(precision_score(y_test, predRF)))
print('Recall score: {}'.format(recall_score(y_test, predRF)))
print('F1 score: {}'.format(f1_score(y_test, predRF)))
