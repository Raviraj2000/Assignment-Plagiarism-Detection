import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from unidecode import unidecode

import string
import re

def preprocess(corpus):
    corpus = corpus.lower()
    stopset = stopwords.words('english') 
    
    corpus = re.sub(r'[^\w\s]', '', corpus)
    
    corpus = corpus.split()
    
    lemmatizer = WordNetLemmatizer()
    
    corpus = [lemmatizer.lemmatize(word) for word in corpus if word not in set(stopset)]
    
    corpus = ' '.join(corpus)
        
    return corpus