from display import scene_printer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words={stemmer.stem(word) for word in word_tokenize((keyword.lower()))}
    results=[]
    for element in scenes:
          score=0
          name = {stemmer.stem(word) for word in word_tokenize(element.anime.lower())}
          description = {stemmer.stem(word) for word in word_tokenize(element.description.lower())}
          for word in search_words:
             if word in name:
                      score=score+3
             if word in description:
                      score=score+1
          if score>0:
             results.append((element,score))
    return results