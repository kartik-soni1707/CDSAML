#Importing headers
from nltk.corpus import stopwords,words
import numpy as np
import pandas as pd
import nltk
import string
import re
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer,HashingVectorizer
from sklearn.svm import SVC as clf
#Extracting the data
re.compile('<title>(.*)</title>')
df=pd.read_csv("sms.csv").iloc[1:,1:]
v=CountVectorizer()
x = v.fit_transform(df.iloc[:,0].values.astype('U'))  ## Even astype(str) would work
y=df.iloc[:,1].values
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
classifier=clf(kernel='poly',degree=1)
classifier.fit(X_train,y_train)
predRF=classifier.predict(X_test)
predict=[]
real=[]
for x in range(len(y_test)):
    if predRF[x]=='spam':    
        predict.append(1)
    else:
        predict.append(0)
    if y_test[x]=='spam':    
        real.append(1)
    else:
        real.append(0)

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
print('Accuracy score: {}'.format(accuracy_score(real, predict)))
print('Precision score: {}'.format(precision_score(real, predict)))
print('Recall score: {}'.format(recall_score(real, predict)))
print('F1 score: {}'.format(f1_score(real, predict)))
cm=confusion_matrix(real, predict)
print(cm)
