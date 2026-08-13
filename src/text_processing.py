from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

def process_text(text):
    return [stemmer.stem(word) for word in word_tokenize(text.lower()) if word.isalpha()]