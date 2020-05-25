#Importing headers
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import string
#Importing data
df1=pd.read_csv("Datasets/Batch1/spam_tweets1.csv")
df2=pd.read_csv("Datasets/Batch1/lgtmt_tweets1.csv")
df1['Ans']=[1]*len(df1)
df2['Ans']=[0]*len(df2)
df1=df1.loc[:,['Tweet','Ans']].values
df2=df2.loc[:,['Tweet','Ans']].values
df3=np.concatenate((df1,df2),axis=0)
np.random.shuffle(df3)
