# CDSAML

## Functions: ##
### FeatureExtraction ##
1. **HasNGrams(tweet, n=2)** </br>
    tweet : Takes a list or a string as input  </br>
    n : order (2 mean bigram 3 means trigram)  </br>
    =====> returns True/False  </br>

2. **tweet2vec(tweet)** </br>
    takes tweet and returns a 300 by 1 sized numpy array </br>
    similar tweets are closer vectors
    download model at </br>
    https://fasttext.cc/docs/en/english-vectors.html#content </br>
3. **similarity(tweet1, tweet2)** </br>
    takes 2 tweets and returns a number between 0 and 1 representing similarity </br>
    
### Cleaning ###
1. **clean(tweet)**  </br>
    string ----> list  </br>
    (removes URLs, Mentions, Numbers, Emojis, And trims words) </br>
    Special characters are removed </br>
    URLs are replaced with "@url" </br>
    Mentions are replaced with "@mention"</br>
