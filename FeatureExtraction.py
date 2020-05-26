import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('./wiki-news-300d-1M.vec', binary=False)

bigrams  = ['check out',
 'for the',
 'the latest',
 'make money',
 'latest news',
 'news about',
 'you can',
 'the best',
 'you have',
 'twitter account']

trigrams = ['the latest news',
 'latest news about',
 'thanks for the',
 'make money online',
 'new blog post',
 'check out for',
 'your twitter account',
 'please check out',
 'out for sale',
 'check this out']

def HasNGrams(tweet, n=2):

    if(type(tweet) == list):
        tweet = ' '.join(tweet)
    
    if n==2:
        for bigram in bigrams:
            if bigram in tweet:
                return True
        return False
    if n==3:
        for trigram in trigrams:
            if trigram in tweet:
                return True
        return False
    
    
def tweet2vec(tweet):
    vec = np.zeros(300,)
    for word in tweet:
        vec += model['word']
    return vec

def similarity(tweet1, tweet2):
    vec1 = tweet2vec(tweet1)
    vec2 = tweet2vec(tweet2)
    return np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))
    