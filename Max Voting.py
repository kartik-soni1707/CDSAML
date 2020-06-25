  #Importing headers
from statistics import mode as md
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC as clf3
from sklearn.naive_bayes import MultinomialNB as clf1 
from sklearn.ensemble import RandomForestClassifier as clf2
from sklearn.naive_bayes import BernoulliNB as clf4
df=pd.read_csv("reviews.csv",encoding='latin-1')
vect=CountVectorizer()
x=df.iloc[:,1]
y=df.iloc[:,-1]
X=vect.fit_transform(x)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
clf=clf1()
clf.fit(X_train,y_train)
predRF1=clf.predict(X_test)
clf2=clf2()
clf2.fit(X_train,y_train)
predRF2=clf2.predict(X_test)
clf3=clf3()
clf3.fit(X_train,y_train)
predRF3=clf3.predict(X_test)
clf4=clf4()
clf4.fit(X_train,y_train)
predRF4=clf4.predict(X_test)
predRF=[]
for i in range(len(predRF1)):
    ans=(3*predRF1[i]+1.5*predRF2[i]+predRF3[i]+2*predRF4[i])
    ans/=7.5
    if ans>0.6:
        ans=1
    else:
        ans=0
    predRF.append(ans)
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score as f1
print('F score: {}'.format(f1(y_test, predRF)))
print('F1 score: {}'.format(f1(y_test, predRF1)))
print('F2 score: {}'.format(f1(y_test, predRF2)))
print('F3 score: {}'.format(f1(y_test, predRF3)))
print('F4 score: {}'.format(f1(y_test, predRF4)))

