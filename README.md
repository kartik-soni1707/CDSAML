# CDSAML

## Functions: ##
### FeatureExtraction ##
1. **HasNGrams(tweet, n=2)** </br>
    tweet : Takes a list or a string as input  </br>
    n : order (2 mean bigram 3 means trigram)  </br>
    =====> returns True/False  </br>

### Cleaning ###
1. **clean(tweet)**  </br>
    string ----> list  </br>
    (removes URLs, Mentions, Numbers, Emojis, And trims words) </br>
    Special characters are removed </br>
    URLs are replaced with "@url" </br>
    Mentions are replaced with "@mention"</br>
