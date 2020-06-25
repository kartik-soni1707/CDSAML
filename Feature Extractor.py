import pandas as pd 
df=pd.read_csv("reviews.csv")
text=df.iloc[:,1].values
polar=df.iloc[:,2].values
target=df.iloc[:,3].values
col1=[]
def non_alphan(sentence):
    alphab=0
    digits=0
    special=0
    upper=0
    
    for chr in sentence:
        

        if(chr.isalpha()):
            alphab+=1
        elif(chr.isdigit()):
            digits+=1
        else:
            special+=1
        if(chr.isupper()):
            upper+=1
          
    return [alphab,digits,special,upper]

vals=[]
for x in range(len(text)):
    res=non_alphan(text[x])
    
    vals.append([len(text[x]),res[0],res[-1],res[1],res[2],polar[x],target[x]])
vals=pd.DataFrame(vals)
vals.columns = ['Length','Alphabets','Upper','Digits','Special Char','Polarity','Spam']
vals.to_csv("Attrib.csv")