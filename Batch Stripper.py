import pandas as pd

for x in ["Datasets/lgtmt_users","Datasets/lgtmt_users_followers","Datasets/spam_users","Datasets/spam_users_followers"]:
    df=pd.read_csv(x+".csv")
    df=df.iloc[1:10000,:]
    df.to_csv(x+"1.csv")