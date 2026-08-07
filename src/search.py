from display import scene_printer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
def process_text(text):
      return {stemmer.stem(word) for word in word_tokenize(text.lower())}
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words=process_text(keyword)
    results=[]
    for element in scenes:
          score=0 
          name = process_text(element.anime)
          description = process_text(element.description)
          for word in search_words:
             if word in name:
                      score=score+3
             if word in description:
                      score=score+1
          if score>0:
             results.append((element,score))
    return results