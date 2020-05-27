import numpy as np
import pandas as pd

from nltk.stem import WordNetLemmatizer
import nltk
lm = WordNetLemmatizer()
import re

# converts symbols from nltk format to wordnet format.
# Taken from stackoverflow https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return 'n'

def clean(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'@[\w+]', '@mention', tweet)
    tweet = re.sub(r'(http://)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', '@url',tweet)
    tweet = re.sub(r'[\.\\/\(\),\-!$%^&*~`:0-9\?+=-\[\]\{\};\'\"<>]', '', tweet)
    tweet = tweet.split()
    tweet = list(filter(lambda x: len(x) > 2, tweet))
#     tweet = nltk.pos_tag(tweet) # adds the "part of sentence (noun, verb, adjective, etc )" after each word
    tweet = [lm.lemmatize(x) for x in tweet]
    return tweet
