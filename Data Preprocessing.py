#Importing headers
from nltk.corpus import stopwords,words
import numpy as np
import pandas as pd
import nltk
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#For extracting enligh words
re.compile('<title>(.*)</title>')

#Importing data
df1=pd.read_csv("Datasets/Batch1/spam_tweets1.csv")
df2=pd.read_csv("Datasets/Batch1/lgtmt_tweets1.csv")
df1['Ans']=['spam']*len(df1)
df2['Ans']=['ham']*len(df2)
df1=df1.loc[:,['Tweet','Ans']].values
df2=df2.loc[:,['Tweet','Ans']].values
df3=np.concatenate((df1,df2),axis=0)
np.random.shuffle(df3)
df3=df3[5000:5050,:]
def proc_words(df3):
    dataset=[]
    counter=0
    for sentence in range(len(df3[:,0])):
        res = re.findall(r'\w+', df3[sentence,0]) #Enlgish words only
        ans=''
        exist=0
        for x in res :
            if len(x)>2:#Decisive word
                if x in words.words():
                    ans+=(x+" ")
                    exist=1
        if exist ==1:
            dataset.append([ans,df3[sentence,1]])
            print("Record is :"+ans+"Value is "+df3[sentence,1]+"Counter :"+str(counter))
            counter+=1
    dataset=np.array(dataset)
    df=pd.DataFrame(dataset)
    return df
df=proc_words(df3)
df.to_csv("test.csv")
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(df[0].values)
targets=df[1].values
classifier=MultinomialNB()
classifier.fit(counts,targets)
test_set=proc_words(df3[5000:5050,])
test_set_counts=vectorizer.transform(test_set[0].values)
results=classifier.predict(test_set_counts)
actual=test_set.iloc[:,1].values
count=0
for x in range(len(results)):
    if(results[x]==actual[x]):
        count+=1
      
print(count/len(results))
        